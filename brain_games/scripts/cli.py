"""Interface for brain-games."""

import prompt


def welcome_user():
    """Get an user name.

    Returns:
        [str]: [name of user]
    """
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name


def greeting_user():
    """Greeting user."""
    print('Welcome to the Brain Games!')


def instruct_user():
    """Instruct the user about the rules of the game."""
    print('Answer "yes" if the number is even, otherwise answer "no".')