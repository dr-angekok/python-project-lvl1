"""Progression game programm."""
from random import randrange

INSTRUCTION = 'What number is missing in the progression?'


def generate_progression(first, diff, count):
    """Generate a sequence of the desired length and with a given step.

    Args:
        first (int): start number
        diff (int): step number
        count (int): count of the steps

    Returns:
        [tuple]: tuple of the progression
    """
    numbers_set = []
    for number, _ in enumerate(range(0, count)):
        numbers_set.append(first + diff * number)
    return numbers_set


def get_question(numbers_set, missing_count):
    """Generate a question to the user.

    Args:
        numbers_set (itereble): tuple of numbers (int)
        missing_count (int): Element to replace with ..

    Returns:
        [str]: question
    """
    question = ''
    for number, item in enumerate(numbers_set):
        if number == missing_count:
            question += ' ..'
        else:
            question += ' {0}'.format(item)
    return question


def get_round():
    """Make a round number fo game Progression.

    Returns:
        [str]: random number and correct answer for game
    """
    range_count = randrange(5, 10)
    step_range = randrange(1, 5)
    start_range = randrange(1, 50)

    numbers_set = generate_progression(start_range, step_range, range_count)
    missing_count = randrange(1, len(numbers_set) - 1)
    question = get_question(numbers_set, missing_count)
    correct_answer = str(numbers_set[missing_count])

    return question[1:], correct_answer
