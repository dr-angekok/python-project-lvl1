"""Calc game programm."""

from operator import add, mul, sub
from random import choice, randint

INSTRUCTION = 'What is the result of the expression?'
RANGE_COUNT = 100


def calc(first, second, operation):
    """Calculate the result of an operation

    Args:
        first (int): number
        second (inc): number
        operation (func): operation

    Returns:
        str: result of the operation
    """
    return str(operation(first, second))


def get_round():
    """Make a round number fo game calc.

    Returns:
        [str]: random number and correct answer for game
    """
    operations = {'+': add,
                  '-': sub,
                  '*': mul}
    operation = choice(list(operations.keys()))
    first = randint(1, RANGE_COUNT)
    second = randint(1, RANGE_COUNT)
    question = '{0} {2} {1}'.format(first, second, operation)
    correct_answer = calc(first, second, operations[operation])
    return question, correct_answer
