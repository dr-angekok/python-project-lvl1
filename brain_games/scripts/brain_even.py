#!/usr/bin/env python
"""Even game programm."""

from random import randrange

from brain_games.scripts import cli


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
    try_count = 3
    random_numbers = []
    for _ in range(try_count):
        random_numbers.append(randrange(1, 100))

    cli.greeting_user()
    user_name = cli.welcome_user()
    cli.instruct_user()

    for random_number in random_numbers:
        cli.ask_question_to_user(random_number)
        answer = cli.ask_user_answer()
        if is_even(random_number) != is_yes(answer):
            correct_answer = translate_bool(is_even(random_number))
            cli.make_negative_feedback(correct_answer, answer, user_name)
            return
        cli.make_positive_feedback()
    cli.make_congratulation(user_name)


if __name__ == '__main__':
    main()
