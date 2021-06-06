#!/usr/bin/env python
"""Even game programm."""

from brain_games.scripts import cli, rnd_engine


def main():
    """Make a user intreface."""
    user_name = cli.greeting_user('calc')

    random_numbers = zip(rnd_engine.get_attempt_numbers(),
                         rnd_engine.get_attempt_numbers())
    random_operators = rnd_engine.get_mathematical_operations()

    for count, numbers in enumerate(random_numbers):
        number1, number2 = numbers
        operator = random_operators[count]
        question = '{0} {1} {2}'.format(number1, operator, number2)
        answer = int(cli.ask_user((question)))
        operation_result = eval(question)
        if operation_result != answer:
            cli.make_negative_feedback(operation_result, answer, user_name)
            return
        cli.make_positive_feedback()
    cli.make_congratulation(user_name)


if __name__ == '__main__':
    main()
