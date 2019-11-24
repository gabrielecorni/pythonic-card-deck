from core.Deck import Deck
from parametrizations import national_decks
from parametrizations import games


def print_deck(deck):
    print("==========")
    print(str(deck))
    print()

    empty = False
    idx = 0
    while not empty:
        card = deck.draw()
        if card:
            idx = idx + 1
            print(f"{idx}) {card}")
        else:
            empty = True

    print()
    print()


if __name__ == "__main__":

    decks = [Deck.from_country(national_decks.italy).for_game(games.briscola),
             Deck.from_country(national_decks.france),
             Deck.from_country(national_decks.uno)]

    for deck_of_cards in decks:
        print_deck(deck_of_cards)
