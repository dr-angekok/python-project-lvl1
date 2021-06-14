"""Engine for brain-games."""

from brain_games import cli

TRY_COUNT = 3


def main(game):
    """Games engine.

    Args:
        game (func): instruction and question
    """
    user_name = cli.greeting_user(game.INSTRUCTION)
    for _ in range(TRY_COUNT):
        question, correct_answer = game.get_round()
        answer = cli.ask_user(question)
        if answer != correct_answer:
            cli.make_negative_feedback(correct_answer, answer, user_name)
            return
        cli.make_positive_feedback()
    cli.make_congratulation(user_name)
