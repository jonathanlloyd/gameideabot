"""
A short and simple script that tweets random game ideas
"""

import json
import time
import tweepy

from gameideabot import idea_generator


def load_config():
    """
    Load api secrets from config file
    """
    try:
        with open('config.json', 'rb') as config_file:
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
    seed = time.time()
    idea = idea_generator.generate_game_idea(seed)

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
    api.update_status(idea)


if __name__ == '__main__':
    main()

