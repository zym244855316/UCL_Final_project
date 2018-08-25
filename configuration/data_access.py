import pandas as pd
import threading
import datetime
import crawl
import math
import db
import time
from random import shuffle

# Split a into n portions
def split(a, n):
    if (len(a) == 0):
        return []
    else:
        k, m = divmod(len(a), n)
        return list(a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))

# Split a into sublist, with 100 items in each
def split_100(a):
    return split(a, math.ceil(len(a)/100))

class DataAccess(object):
    def __init__(self):
        self._database = db.TwitterDatabase()
        self._crawller = crawl.TwitterCrawlManager()
    
    def get_existing_db_users(self, ids):
        self._database.connect()
        db_result = self._database.queryOrderedTwitterUsers(ids)
        self._database.close()
        return pd.DataFrame(db_result)

    def get_users(self, ids):
        # Shuffle ids
        shuffled_ids = ids.copy()
        shuffle(shuffled_ids)
        # Start multithreading
        number_of_apis = self._crawller.get_number_of_apis()
        splitted_ids = split(shuffled_ids, number_of_apis)
        threads_pool = []
        for index, api in enumerate(self._crawller.get_api_pool()):
            threads_pool.append(
                CrawlThread(api, splitted_ids[index])
            )
            
        for each_thread in threads_pool:
            each_thread.start()
            time.sleep(1)
            
        for each_thread in threads_pool:
            each_thread.join()
        # Retrieve the db objects using the original order
        self._database.connect()
        db_result = self._database.queryOrderedTwitterUsers(ids)
        self._database.close()
        return pd.DataFrame(db_result)

class CrawlThread(threading.Thread):
    def __init__(self, api, ids):
        threading.Thread.__init__(self)
        self._api = api
        self._ids = ids
        self._database = db.TwitterDatabase()
        
    def _log(self, message):
        consumer_key = self._api._consumer_key 
        print('{} - {} - {}'.format(datetime.datetime.utcnow(), consumer_key, message))
        
        
    def run(self):
        if len(self._ids) > 0:
            self._log('Started Thread')
            self._database.connect()
            db_result = self._database.queryUnorderedTwitterUsers(self._ids)
            self._database.close()

            ids_found_in_db = set([x['id'] for x in db_result])
            ids_not_found_in_db = set(self._ids) - ids_found_in_db

            ids_with_no_friends_json = set([x['id'] for x in db_result if x['friends_json'] is None]) | ids_not_found_in_db
            ids_with_no_followers_json = set([x['id'] for x in db_result if x['followers_json'] is None]) | ids_not_found_in_db
            self._log('{} users not found, {} with no firends, {} with no followers'.format(
                len(ids_not_found_in_db),
                len(ids_with_no_friends_json),
                len(ids_with_no_followers_json)
            ))
            # Crawl new users
            # 100 items a time (Check the twitter/tweepy api documentation)
            self._log('Crawl new users')
            splitted_ids_not_found_in_db = split_100(ids_not_found_in_db)
            for ids_not_found_portion in splitted_ids_not_found_in_db:
                crawlled_users = self._api.crawl_list_of_users(list(ids_not_found_portion))
                self._database.connect()
                for tweepyUserObject in crawlled_users:
                    self._database.insertTwitterUser(tweepyUserObject._json)
                self._database.close()
            self._log('Finished crawlling users')

            # Crawl friends
            self._log('Start crawl friends')
            for user_id in ids_with_no_friends_json:
                friends_ids = self._api.crawl_friends(user_id)
                self._database.connect()
                self._database.updateTwitterUserFriends(user_id, friends_ids)
                self._database.close()
            self._log('Finished crawlling friends')
                
            # Crawl followers
            self._log('Start crawl followers')
            if len(ids_with_no_followers_json) > 0 and len(ids_with_no_followers_json) < 5:
                self._log(ids_with_no_followers_json)
            for user_id in ids_with_no_followers_json:
                follower_ids = self._api.crawl_followers(user_id)
                self._database.connect()
                self._database.updateTwitterUserFollowers(user_id, follower_ids)
                self._database.close()
            self._log('Finished crawlling followers')
            
            self._log('Exiting thread')