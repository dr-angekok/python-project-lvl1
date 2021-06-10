#!/usr/bin/env python
"""Progression game programm."""

from brain_games import engine
from brain_games.games import brain_prime


def main():
    """Make game start."""
    engine.main(brain_prime)


if __name__ == '__main__':
    main()
