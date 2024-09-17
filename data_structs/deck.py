"""
Card deck implementation
>>> deck = CardDeck()
>>> for card in sorted(deck, key=card_sort_order): # doctest: +ELLIPSIS
...     print(card)
Card(rank='2', suit='trefl')
Card(rank='2', suit='pik')
Card(rank='2', suit='karo')
...
Card(rank='A', suit='pik')
Card(rank='A', suit='karo')
Card(rank='A', suit='kier')

>>> card_1 = Card('Q', 'karo')
>>> card_1 in deck
True
"""
import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])
suit_values = dict(kier=3, karo=2, pik=1, trefl=0)


class CardDeck:
    """
    Card deck class representing playing cards
    """
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'kier karo pik trefl'.split()

    def __init__(self):
        self._cards = [Card(rank=r, suit=s) for s in self.suits
                       for r in self.ranks]

    def __len__(self):
        """
        >>> deck = CardDeck()
        >>> len(deck)
        52
        >>> len(deck[::13])
        4
        """
        return len(self._cards)

    def __getitem__(self, item):
        """
        >>> deck = CardDeck()
        >>> deck[0]
        Card(rank='2', suit='kier')
        >>> deck[:3]
        [Card(rank='2', suit='kier'), Card(rank='3', suit='kier'), Card(rank='4', suit='kier')]

        >>> for card in deck: # doctest: +ELLIPSIS
        ...     print(card)
        Card(rank='2', suit='kier')
        Card(rank='3', suit='kier')
        Card(rank='4', suit='kier')
        ...
        >>> for card in reversed(deck): # doctest: +ELLIPSIS
        ...     print(card)
        Card(rank='A', suit='trefl')
        Card(rank='K', suit='trefl')
        Card(rank='Q', suit='trefl')
        ...
        """
        return self._cards[item]


def card_sort_order(card):
    rank_value = CardDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
