"""
A short and simple script that tweets random game ideas
"""
import json
import os
import random
import sys
import time
import tweepy

sys.path.insert(0, "./")

from gameideabot import idea_generator

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE_PATH = os.path.join(FILE_DIR, 'config.json')


def load_config():
    """
    Load api secrets from config file
    """
    try:
        with open(CONFIG_FILE_PATH, 'rb') as config_file:
            config_string = config_file.read()
    except IOError:
        print 'Could not find config file (./config.json)'
        exit(1)

    try:
        config = json.loads(config_string)
    except ValueError:
        print 'Could not load config file (invalid JSON)'
        exit(1)

    try:
        assert(
            'consumer_key' in config
            and 'consumer_secret' in config
            and 'access_key' in config
            and 'access_secret' in config
        )
    except AssertionError:
        print 'Could not read config properties from config file'
        exit(1)

    return config

def main():
    """
    Generate a game idea and post it to twitter
    """
    idea = None
    while idea is None or len(idea) > 140:
        seed = time.time()
        random.seed(seed)
        idea = idea_generator.generate_game_idea()

    config = load_config()
    auth = tweepy.OAuthHandler(
        config['consumer_key'],
        config['consumer_secret'],
    )
    auth.set_access_token(
        config['access_key'],
        config['access_secret'],
    )
    api = tweepy.API(auth)

    print idea

    try:
        api.update_status(idea)
    except tweepy.error.TweepError, error:
        print 'Failed trying to post idea to twitter: {}'.format(
            error.message[0]['message']
        )

if __name__ == '__main__':
    main()

