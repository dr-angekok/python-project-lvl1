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
    attempt_set = (randrange(1, range_count), randrange(1, range_count))
    question = '{0} {1}'.format(attempt_set[0], attempt_set[1])
    correct_answer = str(gcd(attempt_set[0], attempt_set[1]))
    return question, correct_answer
