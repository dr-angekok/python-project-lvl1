"""Praim game programm."""

from random import randint

INSTRUCTION = '"yes" if given number is prime. Otherwise answer "no".'
RANGE_COUNT = 100


def is_prime(number):
    """Prime check.

    Args:
        number ([int]): check number

    Returns:
        [bool]: predicate
    """
    if number % 2 == 0:  # Divisibility by 2 test.
        return number == 2  # But 2 is a prime number.
    divider = 3  # Continue from 3.
    while divider * divider <= number and number % divider != 0:
        divider += 2  # We are only interested in odd numbers.
    return divider * divider > number


def get_round():
    """Make a round number fo game even.

    Returns:
        [str]: random number and correct answer for game
    """
    random_number = randint(2, RANGE_COUNT)
    correct_answer = 'yes' if is_prime(random_number) else 'no'
    return random_number, correct_answer
