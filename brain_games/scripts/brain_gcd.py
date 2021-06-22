#!/usr/bin/env python
"""GCD game programm."""

from brain_games import engine
from brain_games.games import brain_gcd


def main():
    """Make game start."""
    engine.run(brain_gcd)


if __name__ == '__main__':
    main()
