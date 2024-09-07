"""
Comprehensions with unit tests
"""
import timeit
import unittest
import array

TIMES = 50000

SETUP = """
symbols = '$¢£¥€¤'
def non_ascii(c):
    return c > 127
"""


class ListExt:
    """
    Class with static methods extending python comprehensions
    """
    @staticmethod
    def convert_to_codes(s: str, use_comp=False) -> list:
        if use_comp:
            return ListExt.convert_to_codes_use_comp(s)
        symbols = s
        codes = []
        for sym in symbols:
            codes.append(ord(sym))
        return codes

    @staticmethod
    def convert_to_codes_use_comp(s: str) -> list:
        return [ord(sym) for sym in s]

    @staticmethod
    def last_item_use_comp(s: str) -> int:
        last = 0
        [last := ord(sym) for sym in s]
        return last

    @staticmethod
    def create_cartesian(first_list: list, second_list: list) -> list:
        ret_list = [(item1, item2) for item1 in first_list
                    for item2 in second_list]
        return ret_list

    @staticmethod
    def create_tuple(s: str) -> tuple:
        return tuple(ord(symbol) for symbol in s)

    @staticmethod
    def create_array(s: str) -> array.array:
        return array.array("I", (ord(symbol) for symbol in s))

    @staticmethod
    def clock(label, cmd):
        res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
        print(label, *(f'{x:.4f}' for x in res))


class TestListExtComp(unittest.TestCase):
    def setUp(self):
        self.codes_str = '$¢£¥€¤'

    def test_convert_to_codes(self):
        exp_list = [36, 162, 163, 165, 8364, 164]

        codes = ListExt.convert_to_codes(self.codes_str)
        self.assertListEqual(codes, exp_list)

        codes = ListExt.convert_to_codes(self.codes_str, use_comp=True)
        self.assertListEqual(codes, exp_list)

    def test_convert_to_codes_last_code(self):
        exp_last_value = 164

        last_value = ListExt.last_item_use_comp(self.codes_str)
        self.assertEqual(last_value, exp_last_value)

    def test_cartesian(self):
        colors = ['black', 'white']
        sizes = ['S', 'M', 'L']
        lst = ListExt.create_cartesian(colors, sizes)
        exp_list = [('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'), ('white', 'M'), ('white', 'L')]

        self.assertListEqual(lst, exp_list)

    def test_create_tuple(self):
        exp_tuple = (36, 162, 163, 165, 8364, 164)
        tup = ListExt.create_tuple(self.codes_str)

        self.assertTupleEqual(tup, exp_tuple)

    def test_create_array(self):
        arr = ListExt.create_array(self.codes_str)
        exp_list = [36, 162, 163, 165, 8364, 164]

        self.assertListEqual(arr.tolist(), exp_list)
        self.assertEqual(len(arr), len(exp_list))

    def test_performance(self):
        ListExt.clock('list comp       :', '[ord(s) for s in symbols if ord(s) > 127]')
        ListExt.clock('list comp + func:', '[ord(s) for s in symbols if non_ascii(ord(s))]')
        ListExt.clock('filter + lambda :', 'list(filter(lambda c: c > 127, map(ord, symbols)))')
        ListExt.clock('filter + func   :', 'list(filter(non_ascii, map(ord, symbols)))')


if __name__ == "__main__":
    unittest.main()
