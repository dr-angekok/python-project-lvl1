#!/usr/bin/env python
"""Main programm."""

from brain_games import cli


def main():
    """Make a user intreface."""
    cli.greeting_user()
    cli.welcome_user()


if __name__ == '__main__':
    main()
