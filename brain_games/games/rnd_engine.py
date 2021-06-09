"""Random engine for mind games."""

from random import choice, randrange

try_count = 3

def get_random_question(instructions_list):
    """Give a sequence of calculations based on the sequence of a function.

    Args:
        instructions_list (tuple): tuple of some function.

    Returns:
        [lists]: tuples of str questions and correct answers on it.
    """
    random_numbers = zip(get_attempt_numbers(),
                         get_attempt_numbers())
    questions = []
    for count, numbers in enumerate(random_numbers):
        operator = instructions_list[count]
        questions.append('{0}{1}{2}'.format(numbers[0], operator, numbers[1]))
    int_result = map(eval, questions)
    correct_answers = map(str, int_result)
    return questions, correct_answers


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


def get_multiplication_set(value):
    """Return a sequence of multiplication signs.

    Returns:
        [tuple]: sequence of multiplication signs
    """
    multiplication_set = []
    for _ in range(try_count):
        multiplication_set.append(value)
    return multiplication_set