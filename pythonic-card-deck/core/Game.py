from collections import namedtuple


"""
A namedtuple to encapsulate basic attributes for card games.
"""
Game = namedtuple("Game", ["name", "values", "wc_value"])
