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


def ask_user_answer():
    """Ask user 'Your answer:'.

    Returns:
        [str]: [answer str]
    """
    return prompt.string('Your answer:')


def ask_question_to_user(question):
    """Ask a question to the user: 'Question:...'.

    Args:
        question ([any]): [question]
    """
    print('Question: {0}'.format(question))


def make_positive_feedback():
    """Make positive feedback with 'Correct!' message."""
    print('Correct!')


def make_negative_feedback(correct, incorrect, name_of_user):
    """Make negative feedback with text.

    Args:
        correct ([str]): ['yes' or 'no']
        incorrect ([str]): ['yes', 'no' or other]
        name_of_user ([str]): [Username]
    """
    print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(incorrect, correct)) # noqa E501
    print("Let's try again, {0}!".format(name_of_user))


def make_congratulation(username):
    """Congratulation user.

    Args:
        username (str): Name of the user
    """
    print('Congratulations, {0}!'.format(username))
