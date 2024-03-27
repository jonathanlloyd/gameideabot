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
"""Generate inane game ideas from simple grammars"""

import random

from gameideabot import util
from gameideabot.idea_templates import (
    CHATTY_IDEA_TEMPLATES,
    NORMAL_IDEA_TEMPLATES,
)
from gameideabot.word_lists import HASHTAGS

MAX_HASH_TAGS = 3
PROBABILITY_OF_CHATTY_IDEA = 0.1


def generate_game_idea():
    """Generate a game idea from a randomly selected template"""
    #Pick template for game idea
    should_use_chatty_idea = random.random() < PROBABILITY_OF_CHATTY_IDEA

    if should_use_chatty_idea:
        template_list = CHATTY_IDEA_TEMPLATES
    else:
        template_list = NORMAL_IDEA_TEMPLATES

    idea_template = random.choice(template_list)

    #Generate idea from template
    idea = make_idea_from_template(idea_template)

    #Append hashtags
    number_of_hash_tags = random.randint(0, MAX_HASH_TAGS)
    used_hash_tags = set()
    for _ in range(0, number_of_hash_tags):
        idea += ' #{}'.format(util.pick_word(HASHTAGS, used_hash_tags))

    return idea


def make_idea_from_template(template):
    """Generate an idea string from a given idea template"""
    return uppercase_first_letter(
        template(set())
    )


def uppercase_first_letter(string):
    """Return a copy of the given string with the first letter in uppercase"""
    return string[0].upper() + string[1:]


if __name__ == '__main__':
    for _ in range(0, 10):
        print(generate_game_idea())
