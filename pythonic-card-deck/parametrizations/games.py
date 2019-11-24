from core.Game import Game


"""
briscola
"""
briscola = Game(name="briscola",
                values=[0, 10, 0, 0, 0, 0] + [2, 3, 4, 11],  # keep the index-based card-value mapping
                wc_value=0)
