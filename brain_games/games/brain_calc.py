#!/usr/bin/env python
"""Calc game programm."""

from brain_games.games import engine, rnd_engine

instruction = 'What is the result of the expression?'


def main():
    """Make a prepiar to game and play."""
    attempt_set = zip(rnd_engine.get_attempt_numbers(),
                      rnd_engine.get_attempt_numbers(),
                      rnd_engine.get_random_operations(('+', '-', '*')))
    questions = list(map(lambda st: '{0} {2} {1}'.format(st[0], st[1], st[2]),
                         attempt_set))
    correct_answers = list(map(lambda x: str(eval(x)), questions))
    engine.main(questions, correct_answers, instruction)


if __name__ == '__main__':
    main()
