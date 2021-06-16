"""Even game programm."""

from random import randint

INSTRUCTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    """Parity check.

    Args:
        number ([int]): check number

    Returns:
        [bool]: predicate
    """
    return number % 2 == 0


def get_round():
    """Make a round number fo game even.

    Returns:
        [str]: random number and correct answer for game
    """
    range_count = 100
    random_number = randint(1, range_count)
    correct_answer = 'yes' if is_even(random_number) else 'no'
    return random_number, correct_answer
