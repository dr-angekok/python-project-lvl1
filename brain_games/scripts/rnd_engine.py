"""Random engine for mind games."""

from random import randrange, choice

try_count = 3


def get_attempt_numbers():
    """Get random attemp numbers.

    Returns:
        [list]: some random numbers
    """
    range_count = 100
    random_numbers = []
    for _ in range(try_count):
        random_numbers.append(randrange(1, range_count))
    return random_numbers


def get_mathematical_operations():
    """Return a sequence of mathematical operations.

    Returns:
        [list]: some random mathematical operations
    """
    types_of_operations = ('+', '-', '*')
    operations = []
    for _ in range(try_count):
        operations.append(choice(types_of_operations))
    return operations
