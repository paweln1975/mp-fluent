import collections
import unittest
from random import choice

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


class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = CardDeck()

    def test_card_create(self):
        card_1 = Card('7', 'kier')
        self.assertEqual(str(card_1), "Card(rank='7', suit='kier')")

    def test_deck_len(self):
        self.assertEqual(len(self.deck), 52)

    def test_deck_item(self):
        card_1 = self.deck[1]
        self.assertEqual(str(card_1), "Card(rank='3', suit='kier')")

    def test_deck_slicing(self):
        exp_str = "[Card(rank='2', suit='kier'), Card(rank='3', suit='kier'), Card(rank='4', suit='kier')]"
        self.assertEqual(str(self.deck[:3]), exp_str)

    def test_every_card(self):
        exp_str = "[Card(rank='2', suit='kier'), Card(rank='2', suit='karo'), Card(rank='2', suit='pik'), Card(rank='2', suit='trefl')]"
        self.assertEqual(str(self.deck[::13]), exp_str)

    def test_random_choice(self):
        exp_str = "Card"
        self.assertTrue(str(choice(self.deck)).startswith(exp_str))

    def test_deck_iter(self):
        count = 0
        exp = len(self.deck[0:5])
        for _ in self.deck[0:5]:
            count += 1
        self.assertEqual(count, exp)

    def test_check_existence(self):
        card_1 = Card('Q', 'karo')
        self.assertTrue(card_1 in self.deck)

        card_2 = Card('Q', 'beasts')
        self.assertFalse(card_2 in self.deck)

    def test_deck_sorted(self):
        card_1 = None
        for card in sorted(self.deck, key=card_sort_order, reverse=True):
            card_1 = card

        self.assertEqual(str(card_1), "Card(rank='2', suit='trefl')")

if __name__ == "__main__":
    unittest.main()
