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


def greeting_user(game):
    """Greeting user."""
    print('Welcome to the Brain Games!')
    user_name = welcome_user()
    instruct_user(game)
    return user_name


def instruct_user(game):
    """instruct user whith message.

    Args:
        game (str)): type of game.
    """
    if game == 'even':
        message = 'Answer "yes" if the number is even, otherwise answer "no".'
    elif game == 'calc':
        message = 'What is the result of the expression?'
    print(message)


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


def ask_user(question):
    """Asks the user a question and returns the answer.

    Args:
        question (str): question to the user

    Returns:
        [str]: answer
    """
    print('Question: {0}'.format(question))
    return prompt.string('Your answer:')
