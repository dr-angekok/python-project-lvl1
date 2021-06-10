#!/usr/bin/env python
"""Calc game programm."""

from brain_games import engine
from brain_games.games import brain_calc


def main():
    """Make game start."""
    engine.main(brain_calc)


if __name__ == '__main__':
    main()
