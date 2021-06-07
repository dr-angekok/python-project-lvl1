#!/usr/bin/env python
"""Even game programm."""

from brain_games.games import engine, rnd_engine

instruction = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    """Parity check.

    Args:
        number ([int]): check number

    Returns:
        [bool]: predicate
    """
    return number % 2 == 0


def translate_bool(state):
    """Human translator.

    Args:
        state: (bool):

    Returns:
        str: 'yes' or 'no'
    """
    if state:
        return 'yes'
    return 'no'


def main():
    """Make a prepiar to game and play."""
    random_numbers = rnd_engine.get_attempt_numbers()
    correct_states = map(is_even, random_numbers)
    correct_answers = map(translate_bool, correct_states)
    engine.main(random_numbers, correct_answers, instruction)


if __name__ == '__main__':
    main()
