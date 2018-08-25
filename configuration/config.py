import builtins
import os
import configparser
import pickle
from pprint import pprint
import pandas as pd

# Importing the project name from global namespace
# Options are: GIVENCHY, HAWKING, NYC, FLORIDA
profile = builtins.uclresearch_topic
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Import code configurations
config = configparser.RawConfigParser()
configFilePath = '{}/configuration/env.properties'.format(root_path)
pprint('Reading config file from location: {}'.format(configFilePath))
config.read(configFilePath)

BASE = 'BASE'
settings = {}
settings['timeframe'] = config.get(BASE, 'timeframe')
settings['save_to_file'] = config.get(BASE, 'save_to_file')
settings['calculate'] = {}
settings['calculate']['uniquetweets'] = config.get(BASE, 'calculate.uniquetweets') == 'True'
settings['calculate']['uniqueusers'] = config.get(BASE, 'calculate.uniqueusers') == 'True'
settings['calculate']['network'] = config.get(BASE, 'calculate.network') == 'True'
settings['calculate']['analysis'] = config.get(BASE, 'calculate.analysis') == 'True'
# settings['calculate']['friends'] = config.get(BASE, 'calculate.friends') == 'True'

settings['path'] = {}
settings['path']['cwd'] = root_path + config.get(profile, 'path.project')
settings['path']['twitter'] = settings['path']['cwd'] + config.get(BASE, 'path.twitter')
settings['path']['result'] = settings['path']['cwd'] + config.get(BASE, 'path.result')
# Crawling paths
settings['path']['crawl'] = {}
settings['path']['crawl']['friends'] = root_path + config.get(BASE, 'path.crawl.friends')
settings['path']['crawl']['followers'] = root_path + config.get(BASE, 'path.crawl.followers')

pickle_path = settings['path']['cwd'] + config.get(BASE, 'path.pickle')
settings['path']['pickle'] = {}
settings['path']['pickle']['tweets'] = pickle_path+ config.get(BASE, 'path.pickle.tweets')
settings['path']['pickle']['users'] = pickle_path+ config.get(BASE, 'path.pickle.users')
settings['path']['pickle']['network'] = pickle_path+ config.get(BASE, 'path.pickle.network')
settings['path']['pickle']['friends'] = pickle_path + config.get(BASE, 'path.pickle.friends')
settings['path']['pickle']['followers'] = pickle_path + config.get(BASE, 'path.pickle.followers')
settings['path']['pickle']['needcrawl'] = pickle_path + config.get(BASE, 'path.pickle.needcrawl')
settings['path']['pickle']['followersneedcrawl'] = pickle_path + config.get(BASE, 'path.pickle.followersneedcrawl')
settings['path']['pickle']['infected_user_ids'] = pickle_path + '/infected_user_ids.dat'
settings['path']['pickle']['exposed_user_ids_selected'] = pickle_path + '/exposed_user_ids_selected.dat'
def dump_infected_user_ids(data):
    save_pickle_file(settings['path']['pickle']['infected_user_ids'], data)
def load_infected_user_ids():
    return load_pickle_file(settings['path']['pickle']['infected_user_ids'])
def dump_exposed_user_ids_selected(data):
    save_pickle_file(settings['path']['pickle']['exposed_user_ids_selected'], data)
def load_exposed_user_ids_selected():
    return load_pickle_file(settings['path']['pickle']['exposed_user_ids_selected'])


settings['path']['networkx'] = {}
settings['path']['networkx']['all'] = pickle_path + config.get(BASE, 'path.networkx.all')
settings['path']['networkx']['friends'] = pickle_path + config.get(BASE, 'path.networkx.friends')
settings['path']['networkx']['potential'] = pickle_path + config.get(BASE, 'path.networkx.potential')

settings['path']['ml'] = pickle_path

settings['data'] = {}
settings['data']['starttime'] = config.get(profile, 'data.starttime')
settings['data']['eventname'] = config.get(profile, 'data.eventname')
settings['data']['dates'] = config.get(profile, 'data.dates').split(',')
settings['data']['phrases'] = config.get(profile, 'data.phrases').split(',')
pprint(settings)


def load_pickle_file(path):
    print('Loading data file from path {}'.format(path))
    try:
        with open(path, 'rb') as file:
            data = pickle.load(file)
            pprint('Loaded {} entires'.format(len(data)))
            return data
    except Exception as e: raise
    
def save_pickle_file(path, data):
    print('Dumping data to path {}'.format(path))
    with open(path, 'wb') as file:
        pickle.dump(data, file)
    print('Finished dumping data to path {}'.format(path))
    

def load_tweets_dataframe():
    return load_pickle_file(settings['path']['pickle']['tweets'])

def dump_tweets_dataframe(data):
    save_pickle_file(settings['path']['pickle']['tweets'], data)

def load_users_dataframe():
    return load_pickle_file(settings['path']['pickle']['users'])

def dump_users_dataframe(data):
    save_pickle_file(settings['path']['pickle']['users'], data)
    
def load_network_dataframe():
    return load_pickle_file(settings['path']['pickle']['network'])

def dump_network_dataframe(data):
    save_pickle_file(settings['path']['pickle']['network'], data)
    
def load_friends_dictionary():
    return load_pickle_file(settings['path']['pickle']['friends'])

def dump_friends_dictionary(data):
    save_pickle_file(settings['path']['pickle']['friends'], data)
    
def load_followers_dictionary():
    return load_pickle_file(settings['path']['pickle']['followers'])

def dump_followers_dictionary(data):
    save_pickle_file(settings['path']['pickle']['followers'], data) 

def load_followers_needcrawl_set():
    return load_pickle_file(settings['path']['pickle']['followersneedcrawl'])
    
def dump_followers_needcrawl_set(data):
    save_pickle_file(settings['path']['pickle']['followersneedcrawl'], data)

def load_needcrawl_set():
    return load_pickle_file(settings['path']['pickle']['needcrawl'])
    
def dump_needcrawl_set(data):
    save_pickle_file(settings['path']['pickle']['needcrawl'], data)
    
def load_new_friends_dictionary(filename):
    return load_pickle_file('{}/{}'.format(settings['path']['crawl']['friends'], filename))
    
def dump_new_friends_dictionary(data, filename):
    save_pickle_file('{}/{}'.format(settings['path']['crawl']['friends'], filename), data)

def load_new_followers_dictionary(filename):
    return load_pickle_file('{}/{}'.format(settings['path']['crawl']['followers'], filename))

def dump_new_follwers_dictionary(data, filename):
    save_pickle_file('{}/{}'.format(settings['path']['crawl']['followers'], filename), data)
    
def load_networkx_all():
    return load_pickle_file(settings['path']['networkx']['all'])
    
def dump_networkx_all(data):
    save_pickle_file(settings['path']['networkx']['all'], data)
    
def load_networkx_friends():
    return load_pickle_file(settings['path']['networkx']['friends'])
    
def dump_networkx_friends(data):
    save_pickle_file(settings['path']['networkx']['friends'], data)

def load_networkx_potential():
    return load_pickle_file(settings['path']['networkx']['potential'])
    
def dump_networkx_potential(data):
    save_pickle_file(settings['path']['networkx']['potential'], data)
    
def load_ml_data(interval):
    dataframe = load_pickle_file(settings['path']['ml'] + '/{}_data.dat'.format(interval))
    return dataframe

def dump_ml_data(data, interval):
    save_pickle_file(settings['path']['ml'] + '/{}_data.dat'.format(interval), data)
    
def dump_ml_model(data, name):
    save_pickle_file(settings['path']['ml'] + '/{}_model.dat'.format(name), data)
    
