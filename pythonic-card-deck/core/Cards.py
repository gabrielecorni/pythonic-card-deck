from collections import namedtuple


"""
We could go with a regular namedtuple, but I want to redefine its native string representations.
They are __str__() and __repr__() methods.
To achieve that, just create a class inheriting from namedtuple, and redefine these methods.

=======
 NOTE:
=======
__slots__ is redefined as well because it is a memory saving technique.
By setting it to an empty tuple we make sure that instances of this class take the same amount of
memory of a regular tuple. 
Without the __slots__ entry, every instance requires its own dictionary (which is much bigger than a tuple).
"""


class Card(namedtuple("Card", ["idx", "figure", "suit", "symbol", "value"])):
    __slots__ = ()

    def __repr__(self):
        """
        The one invoked with: print(card)
        :return: narrow string representation
        """
        return f"{self.symbol} {self.figure}"

    def __str__(self):
        """
        The one invoked with: print(str(card))
        :return: wide string representation
        """
        return f"{self.symbol} {self.figure}"
        # return f"{self.figure} of {self.suit}"


"""
A namedtuple to encapsulate basic parameters for wild cards.
"""


class Wild(namedtuple("Wild", ["suit", "amount"])):
    __slots__ = ()

    def __repr__(self):
        """
        The one invoked with: print(wild)
        :return: narrow string representation
        """
        return f"{self.suit.symbol} {self.suit.figure}"

    def __str__(self):
        """
        The one invoked with: print(str(wild))
        :return: wide string representation
        """
        return f"{self.suit.figure}"
