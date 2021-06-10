"""Even game programm."""

from random import randrange

instruction = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    """Parity check.

    Args:
        number ([int]): check number

    Returns:
        [bool]: predicate
    """
    return number % 2 == 0


def translate_bool(state):
    """Human translator.

    Args:
        state: (bool):

    Returns:
        str: 'yes' or 'no'
    """
    if state:
        return 'yes'
    return 'no'


def get_round():
    """Make a round number fo game even.

    Returns:
        [str]: random number and correct answer for game
    """
    range_count = 100
    random_number = randrange(1, range_count)
    correct_state = is_even(random_number)
    correct_answer = translate_bool(correct_state)
    return random_number, correct_answer
