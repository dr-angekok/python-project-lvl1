#!/usr/bin/env python
"""Main programm."""

from brain_games.scripts import cli


def main():
    """Make a user intreface."""
    print('Welcome to the Brain Games!\n')
    cli.welcome_user()


if __name__ == '__main__':
    main()
