from core.Deck import Deck
from parametrizations import national_decks
from parametrizations import games


if __name__ == "__main__":

    deck_ita = Deck.from_country(national_decks.italy).for_game(games.briscola)
    deck_ita.shuffle(n_iter=3)

    deck_fra = Deck.from_country(national_decks.france)
    deck_fra.shuffle()

    s = 0
    for i in range(60):
        card = deck_ita.draw()
        if card:
            s = s + card.value
            print(f"{i + 1}) {card}")
        else:
            break

    print(f"Total points: {s}")

    s = 0
    for i in range(60):
        card = deck_fra.draw()
        if card:
            s = s + 1
            print(f"{i + 1}) {card}")
        else:
            break

    print(f"Total cards: {s}")
