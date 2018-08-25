import tweepy
from tweepy import OAuthHandler
import json
import datetime as dt
import time
import os
import sys

class TwitterApi(object):
    def __init__(self, consumer_key, consumer_secret, access_token, access_secret): 
        self.consumer_key = consumer_key 
        self.consumer_secret = consumer_secret 
        self.access_token = access_token
        self.access_secret = access_secret

    def loadapi(self):
        auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_secret)
        return tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

def load_twitter_api_list():
    twitter_api_list = []
    # Jimmy Canteen 0
    twitter_api_list.append(TwitterApi(
        'ogd44qNt9NHukPsUsnKmn1Wm3', 
        'g0PMron4C0eOD7NYpSqekzUwPwRafUpYTOKgiAabA5fkpS2a4l', 
        '936587907007176704-2xAvOIe5u5FTkuAanmWLJRkwKlMPqnD',
        'DTJQl1JjQdbVErGlTGBI7g7wyHeWt8o0eQZJIb4fewn3J'
    ).loadapi())
    # BarberDdddavid 1
    twitter_api_list.append(TwitterApi(
        'Imk26gt1YacAmZqsBvwXNNZp1', 
        'ZTVGMr0B6e8PLaFWFtQFbBSta4e0E3POjZO0Ps4uU7XX2jp08c', 
        '948501581372280832-2Ux6iejRB0Mr7KOyQ2psV5hgN8rCvAW',
        'cwCusThG5QGtLoLusElVWdMKtZ8VHvJmngBGjqCkpO77S'
    ).loadapi())
    # Hu13Steve 2
    twitter_api_list.append(TwitterApi(
        'Lqz4r2UGJ3MALpX7TygEWkdvu', 
        '4irrPlKdKpqdo35PAlqx1g7oTLXL79KGh8ul0Ug3NP7NPnJ5fq', 
        '948494955756052481-HBHi8eC43VnafcgKj1hfQrkiQgdazld',
        '1hfPh52QxAWtku4AqNnjUytGCWyt4AkNllR0RGdNag5wW'
    ).loadapi())
    # james13_david 3
    twitter_api_list.append(TwitterApi(
        'QweR1meYNPziTVMQfnPBw7u7L', 
        'w2imXsR0TKSqafgZP0LU1spudls7SnCcUqskUUubmvmstbah5S', 
        '940722476585312257-i94glXYrPQa4LYqhLz75qNfaDHXrFpU',
        'xezy1i3SKqkiVVBHy25avg1pybkfuR1CIbUzRGj5mq6Mo'
    ).loadapi())
    # hui's crawler 4
    twitter_api_list.append(TwitterApi(
        'FImHy1gMljimQMQxG6432rATE', 
        '8oNc5WX3srEophN8oiGrnBeta1iX1QWPM9IDl3scyuzitHZkTp', 
        '1976839820-bH0EOOIuJQC5yqZRDv5iJo8Gpp3Uerz76OOug99',
        'ntdfl0pjZZYVHsLTDK1wKiEsKHS5B9mAdvyCDhREQqDzG'
    ).loadapi())
    # lzhoudevuk 5 
    twitter_api_list.append(TwitterApi(
        'MP1ydHbs9wSPCvUO0HcJlBd1s', 
        'yeVQtGsq4pgYrX6tBqMtKcscrGULJE9SCPyP38vFDaAhUtSJiw', 
        '959980110588899329-A943y5m9XFhivFJXXw0N1uRSdesdYlY',
        'hP63SwoueduNQSSe4pwlZNhegjJCXVn4qjeZPfv762KsJ'
    ).loadapi())
    # lzhoudevcn 6 
    twitter_api_list.append(TwitterApi(
        'cM2Ket4JdIrFCoFJfZR6dKEJW', 
        'VzewbPMeZcIu8aakQ0cnOmhPnJmHhazFDG9cCSgka01JqT463a', 
        '959978501125402624-iRPiJiSVy7TDihEf1HsV74Ow72iavWO',
        'ZvInw0gQb8xRvMLwoG6PDy18JwM66vhhyFnskeisZBGRe'
    ).loadapi())
    # lzhoudevau passed 7 
    twitter_api_list.append(TwitterApi(
        'pbFZlAThsyleV4IWazYaG6WH0', 
        'w01obwo4ECZfl4aIbhEA8q5GnMGTKVXiWvsDq6D8eE4DiwTpps', 
        '959974918619385856-sGUbwHJQd8YrdoNkJGDTyvpafFjh7wi',
        '676MhvwxiPZoUv6f8Upm2fVaZiPUa5jDvCwFHA05HowiE'
    ).loadapi())
    # ucablz4 passed 8
    twitter_api_list.append(TwitterApi(
        'CeIvDs3UbPO4Yj4XK6ZFHzVIU', 
        'j0eRROwvGFk1CEciSehtUOc2SCVmxzMhWbQd3sUDhztdICPtMW', 
        '930982504596672517-AE7R6i4xaNPUeXME2S4cyeTgSJNBVEv',
        'JEmF4hPSTD65lFmYM1Zm3x4I6Xf7kUQ93NvlodJ2jPrQN'
    ).loadapi())
    # liyi.zhou.17 passed 9
    twitter_api_list.append(TwitterApi(
        'AdCVM7NUpICq9RcYnZiM68FLb', 
        '0hbBfyXK8CBCvl9S6Zu1CkWTlAo1c4rvfsAl8ot4VPehTLpHL4', 
        '930982019672178689-UpCYlSLDFDiwcr44weBZoDO4CY2npyE',
        's3Z5H1cADAMYElfGhYCE27ZQSWNR4EP2n1FcJmcwG80ZB'
    ).loadapi())
    # lzhou1110 10
    twitter_api_list.append(TwitterApi(
        'yom0HoCImxDZobnZzDrJsESke',
        'iPDqeGyq40FbovpFUoLdunLnFINEDB5MQuzFFbo0KBoBiM4mk0',
        '910787059501150208-vvOcHytvhGncJTtuAF23tywLu5UTSbL',
        'lL4vIlZlKMurhhgsZGM11hGh6LG6cUBtaHqbMiLYJTZhj'
    ).loadapi())
    # tao 11
    twitter_api_list.append(TwitterApi(
        'YZD91p9NpWydELrliHkx3FkV2',
        'dchHYkpVxp7Uq1Mi5fA94GfCKWFUrQ1VRp0kQJsI2nXXTJjqUk',
        '960929372206223360-TgkpvCQWqTdf9Po9DaOJCrOCGHiMGVV',
        'pRCYaoy3cKWmzvIZ3rDExlxSBI1SVTVIGLRfvpzFxTaVp'
    ).loadapi())
    # wu api 12
    twitter_api_list.append(TwitterApi(
        '6hDKNKAEVflvc1QiKWRwEvqIU',
        'LAOoZL1qKs4l9VTyWRKOibLj4tm14n6ZziMX9wd9Wo3NJ8ADyC',
        '961193810951856129-nGfaxWcrgS4i0gReDmyg68xOZoWiBPU',
        'xDwZpIXjrvcUZpqxz39e77XM924Ek9tBQ69aC9JtDPMEC'
    ).loadapi())
    # peter.liyi.z api 13
    twitter_api_list.append(TwitterApi(
        'AFRdbq1jpYv5uHzc2XXilJBMY',
        'UvSj6ZnbUG0t3nQASgd7kSHeiCoL14Iadt4f8gI4Y4QhsanovG',
        '2166615014-QcdbmCt252E02I2wAMVgXAJMXtE5tgyQpABuAkr',
        '5nYYyhO1WenLXLuuQ6Kthlg8xOg7wlcX7zEP1aLg6abHT'
    ).loadapi())
    # miao api 14
    twitter_api_list.append(TwitterApi(
        'FlmshcUW970JhOuWCrffznTzM',
        '33oh92E47FaeQm6GNWvC5axvmN3nRm6IKhKwN7UX7Xys7pfCtA',
        '320714154-woEAipLwLvVwkJo2o9i5IYvoSaFGqzV6pN8nTboL',
        'M0UVpBAPdGI3yzfXqXd7vhcx4DRttCLV9LsQTjRR7Fpei'
    ).loadapi())
    # ucl lzhou adlrl account 15
    twitter_api_list.append(TwitterApi(
        '45mvtiqyyq5B1cXi6kPJHq2TO',
        'yrCn2qyWiyYNZXgGX0RhHCAUFV0pjg30twa9txtwltX2CYJvRy',
        '961358756595535873-obN8fa0WJRG7y5ptgtEbO0btCXWagwx',
        'hCKeIKCThs1xmCUsiaMms0jkHXNshVHSVTu1hbUcTa1kz'
    ).loadapi())
    # ucl lzhou adlrl account ucablz4 16
    twitter_api_list.append(TwitterApi(
        '75xtkzO360GjmMgLhaSZ1zH0u',
        '2QM0T8J3Jwy4aJEuaTJk9GT6PxkcFVpGqgwoqWvmkvgvq7mqdr',
        '961359707809157122-EUhutRfRHEBPSeE791pVGzYd2oMMq87',
        'WrgrnvyxVNBFNtkDwD4e1sGw2rQNhvbiOU9YaGkgcK1jA'
    ).loadapi())
    return twitter_api_list

def load_twitter_api():
    consumer_key = 'yom0HoCImxDZobnZzDrJsESke'
    consumer_secret = 'iPDqeGyq40FbovpFUoLdunLnFINEDB5MQuzFFbo0KBoBiM4mk0'
    access_token = '910787059501150208-vvOcHytvhGncJTtuAF23tywLu5UTSbL'
    access_secret = 'lL4vIlZlKMurhhgsZGM11hGh6LG6cUBtaHqbMiLYJTZhj'
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return tweepy.API(auth)


def tweet_search(api, query, max_tweets, max_id, since_id, geocode):
    searched_tweets = []
    while len(searched_tweets) < max_tweets:
        remaining_tweets = max_tweets - len(searched_tweets)
        try:
            new_tweets = api.search(q=query,
                                    count=remaining_tweets,
                                    since_id=str(since_id),
                                    max_id=str(max_id - 1),
                                    geocode=geocode)
            print('found', len(new_tweets), 'tweets')
            if not new_tweets:
                print('no tweets found')
                break
            searched_tweets.extend(new_tweets)
            max_id = new_tweets[-1].id
        except tweepy.TweepError:
            print('exception raised, waiting 15 minutes')
            print('(until:', dt.datetime.now() + dt.timedelta(minutes=15), ')')
            time.sleep(15 * 60)
            break  # stop the loop
    return searched_tweets, max_id


def get_tweet_id(api, date='', days_ago=9, query='a'):
    """ The variable 'days_ago' has been initialized to the maximum
        amount we are able to search back in time (9)."""
    if date:
        # return an ID from the start of the given day
        td = date + dt.timedelta(days=1)
        tweet_date = '{0}-{1:0>2}-{2:0>2}'.format(td.year, td.month, td.day)
        tweet = api.search(q=query, count=1, until=tweet_date)
    else:
        # return an ID from __ days ago
        td = dt.datetime.now() - dt.timedelta(days=days_ago)
        tweet_date = '{0}-{1:0>2}-{2:0>2}'.format(td.year, td.month, td.day)
        # get list of up to 10 tweets
        tweet = api.search(q=query, count=10, until=tweet_date)
        print('search limit (start/stop):', tweet[0].created_at)
        # return the id of the first tweet in the list
        return tweet[0].id


def write_tweets(tweets, filename):
    """ Function that appends tweets to a file. """
    with open(filename, 'a') as f:
        for tweet in tweets:
            json.dump(tweet._json, f)
            f.write('\n')


def get_geo_code_usa():
    # this geocode includes nearly all American states (and a large portion of Canada)
    # Refer to: http://thoughtfaucet.com/search-twitter-by-location/examples/
    return '39.8,-95.583068847656,2500km'


def get_file_path(search_query):
    json_file_root = 'stephen/' + search_query
    return json_file_root


def get_file_name(root, max_days_old, min_days_old):
    if max_days_old - min_days_old == 1:
        d = dt.datetime.now() - dt.timedelta(days=min_days_old)
        day = '{0}-{1:0>2}-{2:0>2}'.format(d.year, d.month, d.day)
    else:
        d1 = dt.datetime.now() - dt.timedelta(days=max_days_old - 1)
        d2 = dt.datetime.now() - dt.timedelta(days=min_days_old)
        day = '{0}-{1:0>2}-{2:0>2}_to_{3}-{4:0>2}-{5:0>2}'.format(
            d1.year, d1.month, d1.day, d2.year, d2.month, d2.day)
    json_file = root + '_' + day + '.json'
    return json_file


def get_max_id(api, json_file, min_days_old):
    # set the 'starting point' ID for tweet collection
    if os.path.isfile(json_file):
        # open the json file and get the latest tweet ID
        with open(json_file, 'r') as f:
            lines = f.readlines()
            if len(lines) > 0:
                max_id = json.loads(lines[-1])['id']
                print('Searching from the bottom ID in file')
                return max_id

    # get the ID of a tweet that is min_days_old
    if min_days_old == 0:
        return -1
    else:
        return get_tweet_id(api, days_ago=(min_days_old - 1))


def main():
    """ This is a script that continuously searches for tweets
        that were created over a given number of days. The search
        dates and search phrase can be changed below. """
    nyc_bombing_phrases = [
        'nyc%20explosion',
        'nyc%20bombing',
        'nyc%20attack',
        'nyc%20terror',
        'new%20york%20explosion',
        'new%20york%20bombing',
        'new%20york%20attack',
        'new%20york%20terror',
        'manhattan%20explosion',
        'manhattan%20bombing',
        'manhattan%20attack',
        'manhattan%20terror',
        'port%20authority%20explosion',
        'port%20authority%20bombing',
        'port%20authority%20attack',
        'port%20authority%20terror']
    
    florida_shooting_phrases = [
        'florida%20shooting',
        'florida%20massacre',
        'Stoneman%20Douglas%20High%20School%20shooting',
        'Stoneman%20Douglas%20High%20School%20massacre',
        'Parkland%20shooting',
        'Parkland%20massacre']
    
    givenchy_death_phrases = [
        'givenchy%20passed%20away',
        'givenchy%20die',
        'givenchy%20death']
    
    stephen_death_phrases = [
        'stephen%20hawking%20passed%20away',
        'stephen%20hawking%20die',
        'stephen%20hawking%20death']
    
    search_phrases = stephen_death_phrases


    geo_code_usa = get_geo_code_usa()
    time_limit = 1.5  # runtime limit in hours
    max_tweets = 100  # number of tweets per search (will be iterated over) - maximum is 100
    # search limits
    # e.g., from 7 to 8 gives current weekday from last week, min_days_old = 0 will search from right now
    min_days_old, max_days_old = 8, 9

    # loop over search items, creating a new file for each
    for search_phrase in search_phrases:
        api_list = load_twitter_api_list()

        print('Search phrase = {}'.format(search_phrase))
        json_file_root = get_file_path(search_phrase)
        os.makedirs(os.path.dirname(json_file_root), exist_ok=True)

        json_file = get_file_name(json_file_root, max_days_old, min_days_old)

        max_id = get_max_id(api_list[0], json_file, min_days_old)
        print('max id (starting point) =', max_id)

        since_id = get_tweet_id(api_list[0], days_ago=(max_days_old - 1))
        print('since id (ending point) =', since_id)

        start = dt.datetime.now()
        end = start + dt.timedelta(hours=time_limit)
        count, exit_count = 0, 0
        while dt.datetime.now() < end:
            count += 1
            print('count =', count)
            # collect tweets and update max_id
            tweets, max_id = tweet_search(
                api_list[count % len(api_list)],
                search_phrase,
                max_tweets,
                max_id=max_id,
                since_id=since_id,
                geocode=geo_code_usa)
            # write tweets to file in JSON format
            write_tweets(tweets, json_file)
            if tweets:
                print(tweets[0].created_at)
                exit_count = 0
            else:
                exit_count += 1
                if exit_count == 4:
                    if search_phrase == search_phrases[-1]:
                        sys.exit('Maximum number of empty tweet strings reached - exiting')
                    else:
                        print('Maximum number of empty tweet strings reached - breaking')
                        break


if __name__ == "__main__":
    main()
