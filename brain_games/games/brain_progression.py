"""Progression game programm."""
from random import randint

INSTRUCTION = 'What number is missing in the progression?'


def generate_progression():
    """Generate a sequence of the desired length and with a given step.

    Returns:
        [tuple]: tuple of str with progression
    """
    start = randint(1, 50)
    finish = randint(5, 10)
    step = randint(1, 5)

    numbers = []
    for number, _ in enumerate(range(0, finish)):
        numbers.append(str(start + step * number))
    return numbers


def get_round():
    """Make a round number fo game Progression.

    Returns:
        [str]: random number and correct answer for game
    """
    numbers = generate_progression()
    missing_index = randint(1, len(numbers) - 2)

    correct_answer = str(numbers[missing_index])

    numbers[missing_index] = '..'
    question = ' '.join(numbers)

    return question, correct_answer
