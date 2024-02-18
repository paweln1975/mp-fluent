import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])
suit_values = dict(kier=3, karo=2, pik=1, trefl=0)


class CardDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'kier karo pik trefl'.split()

    def __init__(self):
        self._cards = [Card(rank=r, suit=s) for s in self.suits
                       for r in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


def card_sort_order(card):
    rank_value = CardDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


if __name__ == "__main__":
    import doctest

    doctest.testfile('tests\\deck.doctest', verbose=True)
