"""Random engine for mind games."""

from random import choice, randrange

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


def get_random_operations(operations):
    """Return a sequence of random operations operations.

    Args:
        operations (iter): sequence of operation

    Returns:
        [list]: some random mathematical operations

    """
    types_of_operations = operations
    random_operations = []
    for _ in range(try_count):
        random_operations.append(choice(types_of_operations))
    return random_operations
