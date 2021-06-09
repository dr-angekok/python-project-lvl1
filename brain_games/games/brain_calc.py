#!/usr/bin/env python
"""Calc game programm."""

from brain_games.games import engine, rnd_engine

instruction = 'What is the result of the expression?'


def main():
    """Make a prepiar to game and play."""
    math_instruction = rnd_engine.get_random_operations(('+', '-', '*'))
    questions, correct_answers = rnd_engine.get_random_question(math_instruction)
    engine.main(questions, correct_answers, instruction)


if __name__ == '__main__':
    main()
