"""
Comprehensions with doc tests
>>> import sys; sys.tracebacklimit = 0
"""
import timeit
import unittest
import array

TIMES = 50000
SYMBOLS = '$¢£¥€¤'

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
        """
        >>> sym_list = ListExt.convert_to_codes(SYMBOLS)
        >>> sym_list
        [36, 162, 163, 165, 8364, 164]
        >>> sym_list = ListExt.convert_to_codes(SYMBOLS, True)
        >>> sym_list
        [36, 162, 163, 165, 8364, 164]
        """
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
        """
        >>> last_value = ListExt.last_item_use_comp(SYMBOLS)
        >>> last_value
        164
        """
        last = 0
        last_comph = [last := ord(sym) for sym in s]
        return last

    @staticmethod
    def create_cartesian(first_list: list, second_list: list) -> list:
        """
        >>> colors = ['black', 'white']
        >>> sizes = ['S', 'M', 'L']
        >>> cartesian = ListExt.create_cartesian(colors, sizes)
        >>> cartesian
        [('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'), ('white', 'M'), ('white', 'L')]
        """
        ret_list = [(item1, item2) for item1 in first_list
                    for item2 in second_list]
        return ret_list

    @staticmethod
    def create_tuple(s: str) -> tuple:
        """
        >>> codes_tuple = ListExt.create_tuple(SYMBOLS)
        >>> codes_tuple
        (36, 162, 163, 165, 8364, 164)
        """
        return tuple(ord(symbol) for symbol in s)

    @staticmethod
    def create_array(s: str) -> array.array:
        """
        >>> arr = ListExt.create_array(SYMBOLS)
        >>> arr.tolist()
        [36, 162, 163, 165, 8364, 164]
        """
        return array.array("I", (ord(symbol) for symbol in s))

    @staticmethod
    def clock(label, cmd):
        res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
        print(label, *(f'{x:.4f}' for x in res))

    @staticmethod
    def unpack_first_value(source_tuple):
        """
        >>> value = ListExt.unpack_first_value((1, 2, 3, 4))
        >>> value
        1
        """
        first_item, second_item, *rest_args = source_tuple
        return first_item

    @staticmethod
    def unpack_last_value(source_tuple):
        """
        >>> value = ListExt.unpack_last_value((1, 2, 3, 4))
        >>> value
        [3, 4]
        """
        first_item, second_item, *rest_args = source_tuple
        return rest_args

    @staticmethod
    def grab_excess_items(first, second, *args, **kwargs):
        """
        >>> value = ListExt.grab_excess_items(1, 2, 3, 4, 5)
        >>> value
        (1, (3, 4, 5))
        """
        return first, args

class TestListExtComp(unittest.TestCase):
    def setUp(self):
        self.codes_str = '$¢£¥€¤'

    def test_performance(self):
        ListExt.clock('list comp       :', '[ord(s) for s in symbols if ord(s) > 127]')
        ListExt.clock('list comp + func:', '[ord(s) for s in symbols if non_ascii(ord(s))]')
        ListExt.clock('filter + lambda :', 'list(filter(lambda c: c > 127, map(ord, symbols)))')
        ListExt.clock('filter + func   :', 'list(filter(non_ascii, map(ord, symbols)))')


if __name__ == "__main__":
    unittest.main()
