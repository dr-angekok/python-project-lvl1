#!/usr/bin/env python
"""Main programm."""

from brain_games.scripts import cli


def main():
    """Make a user intreface."""
    cli.greeting()
    cli.welcome_user()


if __name__ == '__main__':
    main()
