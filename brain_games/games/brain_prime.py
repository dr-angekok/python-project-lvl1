"""Praim game programm."""

from random import randrange

INSTRUCTION = '"yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    """Prime check.

    Args:
        number ([int]): check number

    Returns:
        [bool]: predicate
    """
    prime_sequence = (2, 3, 5, 7, 11, 13,
                      17, 19, 23, 29, 31, 37,
                      41, 43, 47, 53, 59, 61,
                      67, 71, 73, 79, 83, 89, 97)
    return number in prime_sequence


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
    correct_state = is_prime(random_number)
    correct_answer = translate_bool(correct_state)
    return random_number, correct_answer
