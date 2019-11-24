from core.Deck import Deck
from core.Game import Game
from parametrizations import national_decks, games
import pytest


def count_points(deck):
    empty = False
    s_points = 0

    while not empty:
        card = deck.draw()
        if card:
            s_points = s_points + card.value
        else:
            empty = True

    return s_points


# VALUES
# wild cards = 1000
# normal cards = their index
fake_game_A = Game(name="FakeGame_A",
                   values=list(range(200)),
                   wc_value=1000)
# VALUES
# wild cards = each kind of wild card is 50 + previous value, starting with 50
# normal cards = 0.5
fake_game_B = Game(name="FakeGame_B",
                   values=[0.5]*200,
                   wc_value=list(range(50, 1500, 50)))


@pytest.fixture(params=[fake_game_A, fake_game_B])
def fake_game(request):
    return request.param


@pytest.fixture(params=[national_decks.italy, national_decks.uno, national_decks.france])
def deck(request):
    return Deck.from_country(request.param)


def expected_points(deck, game):
    return {
        "italian": {
            "FakeGame_A": 4 * sum(list(range(10))),
            "FakeGame_B": 40 * 0.5
        },
        "french": {
            "FakeGame_A": 4 * sum(list(range(13))) + 2 * 1000,
            "FakeGame_B": 52 * 0.5 + 2 * 50
        },
        "uno": {
            "FakeGame_A": 4 * sum(list(range(25))) + 8 * 1000,
            "FakeGame_B": 100 * 0.5 + 4 * 50 + 4 * 100
        }
    }[str(deck).split()[0].lower()][game.name]


"""
tests
"""


@pytest.mark.parametrize("deck, points",
                         [(Deck.from_country(national_decks.italy).for_game(games.briscola), 120)])
def test_briscola_points(deck, points):
    assert count_points(deck) == points


@pytest.mark.parametrize("deck, points",
                         [(Deck.from_country(national_decks.italy).for_game(fake_game_A),
                           4*sum(list(range(10)))),
                          (Deck.from_country(national_decks.uno).for_game(fake_game_A),
                           4*sum(list(range(25)))+8*1000),
                          (Deck.from_country(national_decks.france).for_game(fake_game_A),
                           4*sum(list(range(13)))+2*1000)])
def test_fake_game_a_points(deck, points):
    assert count_points(deck) == points


@pytest.mark.parametrize("deck, points",
                         [(Deck.from_country(national_decks.italy).for_game(fake_game_B), 40*0.5+0),
                          (Deck.from_country(national_decks.uno).for_game(fake_game_B), 100*0.5+4*50+4*100),
                          (Deck.from_country(national_decks.france).for_game(fake_game_B), 52*0.5+2*50)])
def test_fake_game_b_points(deck, points):
    assert count_points(deck) == points


# same tests with parametrized features
def test_fake_games_with_fixtures(deck, fake_game):
    curr = deck.for_game(fake_game)
    assert expected_points(curr, fake_game) == count_points(curr)
