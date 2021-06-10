#!/usr/bin/env python
"""Even game programm."""

from brain_games import engine
from brain_games.games import brain_even


def main():
    """Make game start."""
    engine.main(brain_even)


if __name__ == '__main__':
    main()
