# Copyright (c) 2016 Jonathan Lloyd - copyright@thisisjonathan.com
#
# The MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""Entry point for the gameideabot twitter bot"""

import json
import os
import tweepy

from gameideabot import idea_generator

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE_PATH = os.path.join(FILE_DIR, 'config.json')


def main():
    """Generate a game idea and post it to twitter"""
    idea = None
    while idea is None or len(idea) > 140:
        idea = idea_generator.generate_game_idea()

    config = load_config()
    twitter_client = tweepy.Client(
        consumer_key=config['consumer_key'],
        consumer_secret=config['consumer_secret'],
        access_token=config['access_key'],
        access_token_secret=config['access_secret'],
    )

    print(idea)

    try:
        twitter_client.create_tweet(text=idea)
    except Exception as e:
        print(f'Failed trying to post idea to twitter: {e}')


def load_config():
    """Load api secrets from config file"""
    try:
        with open(CONFIG_FILE_PATH, 'rb') as config_file:
            config_string = config_file.read()
    except IOError:
        print('Could not find config file (./config.json)')
        exit(1)

    try:
        config = json.loads(config_string)
    except ValueError:
        print('Could not load config file (invalid JSON)')
        exit(1)

    is_valid_config = all([
        'consumer_key' in config,
        'consumer_secret' in config,
        'access_key' in config,
        'access_secret' in config
    ])

    if not is_valid_config:
        print('Could not read config properties from config file')
        exit(1)

    return config


if __name__ == '__main__':
    main()
