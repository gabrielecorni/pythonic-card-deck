from core.Deck import BaseDeck, Suit
from core.Cards import Wild
from parametrizations.Param import Param


"""
Creation function
"""


def generate(param):
    return BaseDeck(suits=[Suit(name=s_name, symbol=s_sign)
                           for s_name, s_sign in zip(param.suits, param.symbols)],
                    figures=param.figures,
                    wild=param.wild)


"""
Italian
"""
italian_figures = [str(n) for n in range(2, 8)] + "Knave Knight King Ace".split()
italian_suits = "Coins Cups Swords Clubs".split()
italian_symbols = "\U0001f4b0 \U0001f3c6 \U00002694 \U0001f38b".split()
italian_wild_cards = []

italian_data = Param(figures=italian_figures,
                     suits=italian_suits,
                     symbols=italian_symbols,
                     wild=italian_wild_cards)

italy = generate(italian_data)


"""
French
"""
french_figures = [str(n) for n in range(2, 11)] + list('JQKA')
french_suits = "Hearts Spades Diamonds Clubs".split()
french_symbols = "\U00002665 \U00002660 \U00002666 \U00002663".split()
french_wild_cards = [Wild(suit=Suit(name="Wild Card", symbol="\U0001f0cf"), amount=2)]

french_data = Param(figures=french_figures,
                    suits=french_suits,
                    symbols=french_symbols,
                    wild=french_wild_cards)

france = generate(french_data)


"""
Uno
"""
uno_figures = [str(n) for n in range(0, 10)] + [str(n) for n in range(1, 10)] + 2 * "Skip Reverse +2".split()
uno_suits = "Red Yellow Green Blue".split()
uno_symbols = "\U0001f534 \U0001F49b \U0001F49a \U0001F499".split()  # \U00026AB -> black
uno_wild_cards = [Wild(suit=Suit(name="Wild", symbol="\U000026ab"), amount=4),
                  Wild(suit=Suit(name="Wild+4", symbol="\U000026ab"), amount=4)]

uno_data = Param(figures=uno_figures,
                 suits=uno_suits,
                 symbols=uno_symbols,
                 wild=uno_wild_cards)

uno = generate(uno_data)
