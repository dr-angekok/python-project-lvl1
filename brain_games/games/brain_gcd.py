"""GCD game programm."""

from random import randrange

INSTRUCTION = 'Find the greatest common divisor of given numbers.'


def gcd(x, y):
    """Calculate the greatest common divisor.

    Args:
        x (int): some number
        y (int): some number

    Returns:
        [int]: the greatest common divisor
    """
    while(y):
        x, y = y, x % y
    return x


def get_round():
    """Make a round number fo game GCD.

    Returns:
        [str]: random number and correct answer for game
    """
    range_count = 100
    first, second = (randrange(1, range_count), randrange(1, range_count))
    question = '{0} {1}'.format(first, second)
    correct_answer = str(gcd(first, second))
    return question, correct_answer
