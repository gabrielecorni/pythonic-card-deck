from core.Deck import BaseDeck, Suit
from parametrizations.Param import Param


"""
Creation function
"""


def generate(param):
    return BaseDeck(suits=[Suit(name=s_name, symbol=s_sign)
                           for s_name, s_sign in zip(param.suits, param.symbols)],
                    figures=param.figures,
                    n_wild=param.nb_wc)


"""
Italian
"""
italian_figures = [str(n) for n in range(2, 8)] + "Knave Knight King Ace".split()
italian_suits = "Coins Cups Swords Clubs".split()
italian_symbols = "\U0001f4b0 \U0001f3c6 \U00002694 \U0001f38b".split()
italian_wild_cards = 0

italian_data = Param(figures=italian_figures,
                     suits=italian_suits,
                     symbols=italian_symbols,
                     nb_wc=italian_wild_cards)

italy = generate(italian_data)


"""
French
"""
french_figures = [str(n) for n in range(2, 11)] + list('JQKA')
french_suits = "Hearts Spades Diamonds Clubs".split()
french_symbols = "\U00002665 \U00002660 \U00002666 \U00002663".split()
french_wild_cards = 2

french_data = Param(figures=french_figures,
                    suits=french_suits,
                    symbols=french_symbols,
                    nb_wc=french_wild_cards)

france = generate(french_data)
