#!/usr/bin/env python
"""Even game programm."""

from brain_games.scripts import cli


def main():
    """Make a user intreface."""
    cli.greeting_user()
    user_name = cli.welcome_user()


if __name__ == '__main__':
    main()
