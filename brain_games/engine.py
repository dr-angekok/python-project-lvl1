"""Engine for brain-games."""

import prompt

ROUNDS_COUNT = 3


def main(game):
    """Games engine.

    Args:
        game (func): instruction and question
    """
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(user_name))
    print(game.INSTRUCTION)

    for _ in range(ROUNDS_COUNT):
        question, correct_answer = game.get_round()
        print('Question: {0}'.format(question))
        answer = prompt.string('Your answer:')
        if answer != correct_answer:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(answer, correct_answer)) # noqa E501
            print("Let's try again, {0}!".format(user_name))
            return
        print('Correct!')
    print('Congratulations, {0}!'.format(user_name))
