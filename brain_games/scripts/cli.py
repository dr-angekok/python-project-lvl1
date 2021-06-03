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


def greeting():
    """Greeting user."""
    print('Welcome to the Brain Games!\n')
