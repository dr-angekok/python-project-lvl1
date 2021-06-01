"""Interface for brain-games."""

import prompt


def welcome_user():
    """Get an user name."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
