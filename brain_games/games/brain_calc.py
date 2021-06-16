"""Calc game programm."""

from operator import add, mul, sub
from random import choice, randint

INSTRUCTION = 'What is the result of the expression?'
RANGE_COUNT = 100


def get_round():
    """Make a round number fo game even.

    Returns:
        [str]: random number and correct answer for game
    """
    types_of_operation = choice(('+', '-', '*'))
    first = randint(1, RANGE_COUNT)
    second = randint(1, RANGE_COUNT)
    question = '{0} {2} {1}'.format(first,
                                    second,
                                    types_of_operation)
    operation = {'+': add,
                 '-': sub,
                 '*': mul}
    correct_answer = str(operation[types_of_operation](first, second))
    return question, correct_answer
