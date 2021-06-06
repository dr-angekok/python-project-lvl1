#!/usr/bin/env python
"""Even game programm."""

from brain_games.scripts import cli, rnd_engine


def is_even(number):
    """Parity check.

    Args:
        number ([int]): check number

    Returns:
        [bool]: predicate
    """
    return number % 2 == 0


def is_yes(string):
    """Positive answer check.

    Args:
        string (str): answer

    Returns:
        [bool]: predicate
    """
    return string == 'yes'


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
    """Make a user intreface."""
    random_numbers = rnd_engine.get_attempt_numbers()

    user_name = cli.greeting_user('even')

    for random_number in random_numbers:
        answer = cli.ask_user(random_number)
        if is_even(random_number) != is_yes(answer):
            correct_answer = translate_bool(is_even(random_number))
            cli.make_negative_feedback(correct_answer, answer, user_name)
            return
        cli.make_positive_feedback()
    cli.make_congratulation(user_name)


if __name__ == '__main__':
    main()
