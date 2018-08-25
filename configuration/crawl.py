import tweepy
from tweepy import OAuthHandler
import time
import os
import pandas as pd    
    
class TwitterApi(object):
    def __init__(self, consumer_key, consumer_secret, access_token, access_secret): 
        self._consumer_key = consumer_key 
        self._consumer_secret = consumer_secret 
        self._access_token = access_token
        self._access_secret = access_secret
        
        auth = OAuthHandler(self._consumer_key, self._consumer_secret)
        auth.set_access_token(self._access_token, self._access_secret)
        self._api = tweepy.API(
            auth, 
            wait_on_rate_limit=True, # Making sure this is True, so the data will be complete.
            wait_on_rate_limit_notify=True, # Print notification
            compression=True
        )
    
    def get_api_reference(self):
        return '[key:{}]'.format(self._consumer_key)
 
    def _print_message(self, message):
        print('{}:{}'.format(self.get_api_reference(), message))
        
    def crawl_followers(self, twitter_user_id):
        follower_ids = []
        try:
            c = tweepy.Cursor(self._api.followers_ids, id = twitter_user_id)
            for page in c.pages():
                follower_ids.extend(page)
        except tweepy.TweepError as e:
            self._print_message('TweepError - {}'.format(e))
        except:
            e = sys.exc_info()[0]
            self._print_message('Error - {}'.format(e))
        return follower_ids
        
    def crawl_friends(self, twitter_user_id):
        friends_ids = []
        try:
            c = tweepy.Cursor(self._api.friends_ids, id = twitter_user_id)
            for page in c.pages():
                friends_ids.extend(page)
        except tweepy.TweepError as e:
            self._print_message('TweepError - {}'.format(e))
        except:
            e = sys.exc_info()[0]
            self._print_message('Error - {}'.format(e))
        return friends_ids

    def crawl_list_of_users(self, twitter_user_id_list):
        return self._api.lookup_users(user_ids = twitter_user_id_list)
    
    def crawl_one_user(self, twitter_user_id):
        return self._api.get_user(id = twitter_user_id)
    
    


class TwitterCrawlManager(object):
    def __init__(self):
        root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        keys = pd.read_csv(root_path + '/configuration/twitter_keys.csv')
        self._api_pool = []
        for index, row in keys.iterrows():
            twitterApi = TwitterApi(
                row.consumer_key, row.consumer_secret, row.access_token, row.access_secret)
            self._api_pool.append(twitterApi)
        print('Initialted a total of {} twitter api objects'.format(len(self._api_pool)))
    
    def get_number_of_apis(self):
        return len(self._api_pool)
    
    def get_api_pool(self):
        return self._api_pool