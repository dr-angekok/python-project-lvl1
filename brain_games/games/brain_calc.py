#!/usr/bin/env python
"""Calc game programm."""

from brain_games.games import engine, rnd_engine

instruction = 'What is the result of the expression?'


def main():
    """Make a prepiar to game and play."""
    random_numbers = zip(rnd_engine.get_attempt_numbers(),
                         rnd_engine.get_attempt_numbers())
    random_operators = rnd_engine.get_mathematical_operations()
    questions = []

    for count, numbers in enumerate(random_numbers):
        operator = random_operators[count]
        questions.append('{0}{1}{2}'.format(numbers[0], operator, numbers[1]))
    int_result = map(eval, questions)
    correct_answers = map(str, int_result)

    engine.main(questions, correct_answers, instruction)


if __name__ == '__main__':
    main()
