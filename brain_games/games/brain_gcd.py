#!/usr/bin/env python
"""GCD game programm."""

from brain_games.games import engine, rnd_engine

instruction = 'Find the greatest common divisor of given numbers.'


def gcd(x, y):
    """Calculate the greatest common divisor.

    Args:
        x (int): some number
        y (int): some number

    Returns:
        [int]: the greatest common divisor
    """
    while(y):
        x, y = y, x % y
    return x


def main():
    """Make a prepiar to game and play."""
    attempt_set = list(zip(rnd_engine.get_attempt_numbers(),
                           rnd_engine.get_attempt_numbers()))
    questions = map(lambda sets: '{0} {1}'.format(sets[0], sets[1]),
                    attempt_set)
    correct_answers = map(lambda item: str(gcd(item[0], item[1])), attempt_set)
    engine.main(questions, correct_answers, instruction)


if __name__ == '__main__':
    main()
