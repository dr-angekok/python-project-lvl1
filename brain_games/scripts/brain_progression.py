#!/usr/bin/env python
"""Progression game programm."""

from brain_games import engine
from brain_games.games import brain_progression


def main():
    """Make game start."""
    engine.main(brain_progression)


if __name__ == '__main__':
    main()
