"""
Generate inane game ideas from simple grammars
"""

import random

from gameideabot.word_lists import (
    ADJECTIVES,
    GENRES,
    CHARACTERS,
    CHARACTER_ADJECTIVES,
    THINGS,
    PRESENT_VERBS,
    ACTIONS,
    ART_STYLES,
    SETTINGS,
)


IDEA_TEMPLATES = [
    lambda seen_words: 'In this game you must save the world from {} {} ' \
    'by trying to {}.'.format(
        a_an(pick_word(CHARACTER_ADJECTIVES, seen_words)),
        pick_word(CHARACTERS, seen_words),
        pick_word(ACTIONS, seen_words),
    ),
    lambda seen_words: '{} game where {} {} {} {}.'.format(
        a_an(pick_word(GENRES, seen_words)),
        a_an(pick_word(CHARACTER_ADJECTIVES, seen_words)),
        pick_word(CHARACTERS, seen_words),
        pick_word(PRESENT_VERBS, seen_words),
        a_an(pick_word(THINGS, seen_words)),
    ),
    lambda seen_words: '{} {} {} game set in {}.'.format(
        a_an(pick_word(ADJECTIVES, seen_words)),
        pick_word(GENRES, seen_words),
        pick_word(GENRES, seen_words),
        a_an(pick_word(SETTINGS, seen_words)),
    ),
    lambda seen_words: 'A game about {} set in {} ' \
    'where you can only {}.'.format(
        a_an(pick_word(CHARACTERS, seen_words)),
        a_an(pick_word(SETTINGS, seen_words)),
        pick_word(ACTIONS, seen_words),
    ),
    lambda seen_words: '{} {} game about {} in {} art style.'.format(
        a_an(pick_word(ADJECTIVES, seen_words)),
        pick_word(GENRES, seen_words),
        a_an(pick_word(SETTINGS, seen_words)),
        a_an(pick_word(ART_STYLES, seen_words)),
    ),
    lambda seen_words: '{} {} game where you have to {} before {} ' \
    '{} {}.'.format(
        a_an(pick_word(ADJECTIVES, seen_words)),
        pick_word(GENRES, seen_words),
        pick_word(ACTIONS, seen_words),
        a_an(pick_word(CHARACTERS, seen_words)),
        pick_word(PRESENT_VERBS, seen_words),
        a_an(pick_word(THINGS, seen_words)),
    ),
    lambda seen_words: '{} {} game about {}.'.format(
        a_an(pick_word(ADJECTIVES, seen_words)),
        pick_word(ART_STYLES, seen_words),
        a_an(pick_word(SETTINGS, seen_words)),
    ),
    lambda seen_words: '{} game set in {} {} where you try to {}.'.format(
        a_an(pick_word(ADJECTIVES, seen_words)),
        a_an(pick_word(ART_STYLES, seen_words)),
        pick_word(SETTINGS, seen_words),
        pick_word(ACTIONS, seen_words),
    ),
]

# These idea templates are more "chatty" but get repetative quickly.
# They should be used less often.
CHATTY_IDEA_TEMPLATES = [
    lambda seen_words: 'What if {} game was set in {}?'.format(
        a_an(pick_word(GENRES, seen_words)),
        a_an(pick_word(SETTINGS, seen_words)),
    ),
    lambda seen_words: 'A unique twist on the {} genre. ' \
    'You have to {} while you {} to win the game.'.format(
        pick_word(GENRES, seen_words),
        pick_word(ACTIONS, seen_words),
        pick_word(ACTIONS, seen_words),
    ),
    lambda seen_words: 'This {} game would be interesting - ' \
    'you can only {} once.'.format(
        pick_word(GENRES, seen_words),
        pick_word(ACTIONS, seen_words),
    ),
    lambda seen_words: 'A {} little indie game set in {} {}. ' \
    'Only if you don\'t {} can you {}.'.format(
        pick_word(ADJECTIVES, seen_words),
        a_an(pick_word(ART_STYLES, seen_words)),
        pick_word(SETTINGS, seen_words),
        pick_word(ACTIONS, seen_words),
        pick_word(ACTIONS, seen_words),
    ),
    lambda seen_words: 'Game mechanic idea - before you can {} ' \
    'you must {}.'.format(
        pick_word(ACTIONS, seen_words),
        pick_word(ACTIONS, seen_words),
    ),
]

def pick_word(word_list, seen_words):
    """
    Choose a random word from a given word list being careful not to choose
    the same word twice
    """
    chosen_word = random.choice(word_list)

    while chosen_word in seen_words:
        chosen_word = random.choice(word_list)

    seen_words.add(chosen_word)

    return chosen_word


def a_an(word):
    """
    Add 'a' or 'an' to a word depending on the first letter
    """
    if word[0] in ('a', 'e', 'i', 'o', 'u'):
        return 'an ' + word
    else:
        return 'a ' + word


def generate_game_idea():
    """
    Generate a game idea from a randomly selected template
    """
    if random.randint(0, 10) == 0:
        idea_template = random.choice(CHATTY_IDEA_TEMPLATES)
    else:
        idea_template = random.choice(IDEA_TEMPLATES)

    idea = idea_template(set())
    idea = idea[0].upper() + idea[1:]

    return idea

