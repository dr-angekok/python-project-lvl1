"""Engine for brain-games."""

from brain_games.games import cli


def main(game_states, correct_answers, instruction):
    """Engine for brain-games.

    Args:
        game_states (tuple): tuple of str whith game states to be shown
        correct_answer (tuple): tuple of str whith correct answers
        instruction (str): instruction to user about games rules
    """
    user_name = cli.greeting_user(instruction)
    for question, correct_answer in zip(game_states, correct_answers):
        answer = cli.ask_user(question)
        if answer != correct_answer:
            cli.make_negative_feedback(correct_answer, answer, user_name)
            return
        cli.make_positive_feedback()
    cli.make_congratulation(user_name)
