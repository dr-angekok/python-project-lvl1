"""Progression game programm."""
from random import randrange

INSTRUCTION = 'What number is missing in the progression?'


def get_round():
    """Make a round number fo game Progression.

    Returns:
        [str]: random number and correct answer for game
    """
    range_count = randrange(5, 10)
    step_range = randrange(1, 5)
    start_range = randrange(1, 50)

    numbers_set = []
    for number, _ in enumerate(range(0, range_count)):
        numbers_set.append(start_range + step_range * number)

    missing_count = randrange(1, len(numbers_set) - 1)

    question = ''
    for number, item in enumerate(numbers_set):
        if number == missing_count:
            question += ' ..'
        else:
            question += ' {0}'.format(item)

    correct_answer = str(numbers_set[missing_count])
    return question[1:], correct_answer
