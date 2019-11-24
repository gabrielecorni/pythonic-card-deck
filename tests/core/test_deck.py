from core.Deck import Deck
from parametrizations import national_decks
import pytest


"""
fixtures
"""


#


"""
test functions
"""


def count_cards(deck):
    return deck.n_cards


def count_wild(deck):
    return deck.n_wild


def count_wild_types(deck):
    return deck.wild_types


"""
tests
"""


@pytest.mark.parametrize("deck, cards",
                         [(Deck.from_country(national_decks.italy), 40),
                          (Deck.from_country(national_decks.france), 54),
                          (Deck.from_country(national_decks.uno), 108)])
def test_count_cards(deck, cards):
    assert count_cards(deck) == cards


@pytest.mark.parametrize("deck, n_wild",
                         [(Deck.from_country(national_decks.italy), 0),
                          (Deck.from_country(national_decks.france), 2),
                          (Deck.from_country(national_decks.uno), 8)])
def test_count_wild(deck, n_wild):
    assert count_wild(deck) == n_wild


@pytest.mark.parametrize("deck, wild_types",
                         [(Deck.from_country(national_decks.italy), 0),
                          (Deck.from_country(national_decks.france), 1),
                          (Deck.from_country(national_decks.uno), 2)])
def test_count_wild_types(deck, wild_types):
    assert count_wild_types(deck) == wild_types
