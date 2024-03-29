from collections import namedtuple
from abc import ABC, abstractmethod
from core.Cards import Card
from functools import reduce
import numpy as np


"""
A namedtuple to encapsulate basic attributes for decks.
"""
BaseDeck = namedtuple("DeckBase", ["suits", "figures", "wild", "name"])


"""
Abstract class for a card deck.
"""


class AbsDeck(ABC):
    EMPTY_DECK = None

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
    __slots__ = ()

    def __repr__(self):
        """
        The one invoked with: print(deck)
        :return: narrow string representation
        """
        return f"{self.name}"

    def __str__(self):
        """
        The one invoked with: print(str(deck))
        :return: wide string representation
        """
        return f"{self.name} deck"

    def __new__(cls, suits, figures, wild, name, game=None):
        """
        class method, called before init with same arguments
        """
        # used to store suits, figures, wild into self.suits, self.figures, self.wild respectively.
        # this is done by exploiting the namedtuple constructor.
        return super(BaseDeck, cls).__new__(cls, [suits, figures, wild, name])

    def __init__(self, suits, figures, wild, name, game=None):
        """
        Instantiate a deck given suit list, figure list, jolly number
        """
        super().__init__()

        self.n_suits = len(suits)
        self.n_card_per_seed = len(figures)
        self.wild_types = len(wild)
        self.n_wild = self.count_wild()
        self.n_cards = self.n_suits * self.n_card_per_seed + self.n_wild

        self.deck = None

        if game:
            self.for_game(game)
        else:
            self.values = [0] * self.n_card_per_seed
            self.wc_value = 0

        self.shuffle(n_iter=3)

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
            country.wild,
            country.name
        )

    def count_wild(self):
        """
        Count the number of wild cards in the deck.
        :return: the total amount of wild cards
        """

        number = 0

        if self.wild:
            number = reduce(lambda x, y: x.amount + y.amount, self.wild)
            # reduce() returns the first element of iterable if its len == 1
            # if len > 1, the reduced value is returned
            # hence, if reduce returns a Wild obj, extract its amount
            if type(number) is not int:
                number = number.amount

        return number

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
            Get the suit index given a card index
            :param c_idx: next card index
            :return: the suit index
            """
            # The suit index is the integer part of the division
            return int(c_idx / self.n_card_per_seed)

        def get_figure_index(c_idx):
            """
            Get the figure index given a card index
            :param c_idx: next card index
            :return: the figure index
            """
            # The figure index is the module of the division
            return int(c_idx % self.n_card_per_seed)

        def is_wild(s_idx):
            """
            Return true if the next card is wild, false otherwise.
            :param s_idx: the next suit index
            :return: bool
            """
            # Assumption: no deck has more wild cards than cards per seed
            return self.n_wild > 0 and s_idx >= self.n_suits

        def get_wild_index(f_idx):
            """
            Specify which kind of wild card has been drawn.
            :param f_idx: next figure index
            :return: the next wild card index
            """
            return int(f_idx / int(self.n_wild / self.wild_types))

        # get the next card index
        card_idx = next(self.deck, self.EMPTY_DECK)

        # check if deck is empty
        if card_idx == self.EMPTY_DECK:
            return self.EMPTY_DECK

        # if not empty, build a Card instance from the next card index, then return it

        suit_idx, figure_idx = get_suit_index(card_idx), get_figure_index(card_idx)

        if is_wild(suit_idx):  # drawn a wild card!
            wild_index = get_wild_index(figure_idx)
            drawn_card = Card(
                idx=card_idx,
                figure=self.wild[wild_index].suit.name,
                suit=self.wild[wild_index].suit.name,
                symbol=self.wild[wild_index].suit.symbol,
                value=self.wc_value[wild_index] if type(self.wc_value) == list else self.wc_value)

        else:  # drawn a regular card...
            drawn_card = Card(
                idx=card_idx,
                figure=self.figures[figure_idx],
                suit=self.suits[suit_idx][0],
                symbol=self.suits[suit_idx][1],
                value=self.values[figure_idx])

        return drawn_card

    def merge(self, deck):
        """
        Merge two decks together to increase the card number.
        :param deck: a different deck
        :return: the merged deck.
        """
        # TODO: implement it
        pass
