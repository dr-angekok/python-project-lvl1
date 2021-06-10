"""Calc game programm."""

from random import choice, randrange

instruction = 'What is the result of the expression?'


def get_round():
    """Make a round number fo game even.

    Returns:
        [str]: random number and correct answer for game
    """
    range_count = 100
    types_of_operation = choice(('+', '-', '*'))
    attempt_set = (randrange(1, range_count), randrange(1, range_count))
    question = '{0} {2} {1}'.format(attempt_set[0],
                                     attempt_set[1],
                                     types_of_operation)
    correct_answer = str(eval(question))
    return question, correct_answer
