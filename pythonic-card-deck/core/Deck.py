from collections import namedtuple
from abc import ABC, abstractmethod
from core.Cards import Card
from functools import reduce
import numpy as np


"""
A namedtuple to encapsulate basic attributes for card suits.
"""
Suit = namedtuple("Suit", ["name", "symbol"])


"""
A namedtuple to encapsulate basic attributes for decks.
"""
BaseDeck = namedtuple("DeckBase", ["suits", "figures", "wild"])


"""
Abstract class for a card deck.
"""


class AbsDeck(ABC):
    """
    Data keys
    """
    EMPTY_DECK = None
    # WILD_CARD = Suit(name="Wild Card", symbol="\U0001f0cf")

    @classmethod
    @abstractmethod
    def from_country(cls, country):
        """
        Initialize a deck given national card style.
        :param country: card style parameters for a specific nation
        :return: a deck instance for the given country
        """
        pass

    @abstractmethod
    def for_game(self, game):
        """
        Given a card game, assign a value for each card.
        :param game: game card-points mapping
        :return: None
        """
        pass

    @abstractmethod
    def shuffle(self, n_iter=1):
        """
        Shuffle the deck.
        :param n_iter: shuffle iterations
        :return: None
        """
        pass

    @abstractmethod
    def draw(self):
        """
        Draw a card from the deck.
        """
        pass

    @abstractmethod
    def merge(self, deck):
        """
        Merge two decks together to increase the card number.
        :param deck: a different deck
        :return: the merged deck.
        """
        pass


"""
Deck implementation
"""


class Deck(AbsDeck, BaseDeck):
    def __new__(cls, suits, figures, wild, game=None):
        """
        class method, called before init with same arguments
        """
        return super(BaseDeck, cls).__new__(cls, [suits, figures, wild])

    def __init__(self, suits, figures, wild, game=None):
        """
        Instantiate a deck given suit list, figure list, jolly number
        """
        super().__init__()
        self.n_suits = len(suits)
        self.n_card_per_seed = len(figures)
        self.n_wild, self.wild_types = self.describe()
        self.n_cards = self.n_suits * self.n_card_per_seed + self.n_wild

        self.deck = None

        if game:
            self.for_game(game)
        else:
            self.values = [0] * self.n_card_per_seed
            self.wc_value = 0

    @classmethod
    def from_country(cls, country):
        """
        Initialize a deck given national card style.
        :param country: card style parameters for a specific nation
        :return: a deck instance for the given country
        """

        # instantiate deck with retrieved constants
        return cls(
            country.suits,
            country.figures,
            country.wild
        )

    def describe(self):
        """
        Count the number of wild cards in the deck.
        :return: the total amount of wild cards
        """

        number, kinds = 0, len(self.wild)

        # reduce for len == 1 returns the first element, and fires exception if len == 0
        if kinds == 1:
            number = 1
        elif kinds > 1:
            number = reduce(lambda x, y: x.amount + y.amount, self.wild)

        return number, kinds

    def for_game(self, game):
        """
        Given a card game, assign a value for each card.
        :param game: game card-points mapping
        :return: a deck instance with valued cards.
        """
        self.values = game.values
        self.wc_value = game.wc_value
        return self

    def shuffle(self, n_iter=1):
        """
        Shuffle the deck.
        :param n_iter: shuffle iterations
        :return: None
        """

        cards = np.arange(0, self.n_cards)
        np.random.shuffle(cards)

        # shuffle more for extra randomness
        for _ in range(n_iter):
            np.random.shuffle(cards)

        self.deck = iter(cards)

    def draw(self):
        """
        Draw a card from the deck.
        If no more cards are available, return EMPTY_DECK.
        :return: the drawn card, or EMPTY_DECK
        """

        def get_suit_index(c_idx):
            """

            :param c_idx:
            :return:
            """
            # The suit index is the integer part of the div
            return int(card_idx / self.n_card_per_seed)

        def get_figure_index(c_idx):
            """

            :param c_idx:
            :return:
            """
            pass

        def is_wild(s_idx):
            """

            :param s_idx:
            :return:
            """
            pass

        def get_wild_index(f_idx):
            """

            :param f_idx:
            :return:
            """
            pass

        # get the next card index
        card_idx = next(self.deck, self.EMPTY_DECK)

        # check if deck is empty
        if card_idx == self.EMPTY_DECK:
            return self.EMPTY_DECK

        # if not empty, build a Card instance from the next card index, then return it

        suit_idx = int(card_idx / self.n_card_per_seed)  # suit index is the integer part of the div
        figure_value_idx = int(card_idx % self.n_card_per_seed)  # figure value is the module of the div

        if self.n_wild > 0 and suit_idx == self.n_suits:  # assumption: no deck has more wild cards than cards per seed
            # drawn a wild card!
            wild_index = int(figure_value_idx / int(self.n_wild / self.wild_types))
            drawn_card = Card(
                idx=card_idx,
                figure=self.wild[wild_index].suit.name,
                suit=self.wild[wild_index].suit.name,
                symbol=self.wild[wild_index].suit.symbol,
                value=self.wc_value)
        else:
            # drawn a regular card...
            drawn_card = Card(
                idx=card_idx,
                figure=self.figures[figure_value_idx],
                suit=self.suits[suit_idx][0],
                symbol=self.suits[suit_idx][1],
                value=self.values[figure_value_idx])

        return drawn_card

    def merge(self, deck):
        """
        Merge two decks together to increase the card number.
        :param deck: a different deck
        :return: the merged deck.
        """
        pass
