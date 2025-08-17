"""
Comprehensions with doc tests
>>> import sys; sys.tracebacklimit = 0
"""
import timeit
import unittest
import array
from collections import deque

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
            return [ord(sym) for sym in s]
        symbols = s
        codes = []
        for sym in symbols:
            codes.append(ord(sym))
        return codes

    @staticmethod
    def as_list(s: str, use_comp=False, min_value:int=127) -> list:
        """
        >>> sym_list = ListExt.as_list(SYMBOLS)
        >>> sym_list
        [162, 163, 165, 8364, 164]

        >>> sym_list = ListExt.as_list(SYMBOLS, True)
        >>> sym_list
        [162, 163, 165, 8364, 164]
        >>> sym_list = ListExt.as_list(SYMBOLS, True, 162)
        >>> sym_list
        [163, 165, 8364, 164]
        """
        if use_comp:
            return list(ord(sym) for sym in s if ord(sym) > min_value)

        return list(filter(lambda c: c > min_value, map(ord, s)))

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

    @staticmethod
    def unpack_nested_tuple(values_list):
        """
        >>> metro_areas = [ \
                ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),\
                ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),\
                ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),\
                ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),\
                ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),\
            ]
        >>> value = ListExt.unpack_nested_tuple(metro_areas)
        >>> print(value)
                        |  latitude | longitude
        Mexico City     |   19.4333 |  -99.1333
        New York-Newark |   40.8086 |  -74.0204
        São Paulo       |  -23.5478 |  -46.6358
        <BLANKLINE>
        """
        result = ''
        result += f'{"":15} | {"latitude":>9} | {"longitude":>9}\n'
        for name, _, _, (lat, lon) in values_list:
            if lon <=0:
                result += f'{name:15} | {lat:9.4f} | {lon:9.4f}\n'
        return result

    @staticmethod
    def unpack_nested_values_with_pattern(values_list):
        """
        >>> metro_areas = [ \
                ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),\
                ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),\
                ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),\
                ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),\
                ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),\
            ]
        >>> value = ListExt.unpack_nested_values_with_pattern(metro_areas)
        >>> print(value)
                        |  latitude | longitude
        Mexico City     |   19.4333 |  -99.1333
        New York-Newark |   40.8086 |  -74.0204
        São Paulo       |  -23.5478 |  -46.6358
        <BLANKLINE>
        """
        result = ''
        result += f'{"":15} | {"latitude":>9} | {"longitude":>9}\n'
        for record in values_list:
            match record:
                case (name, _, _, (float(lat), float(lon))):
                    if lon <= 0:
                        result += f'{name:15} | {lat:9.4f} | {lon:9.4f}\n'
        return result

    @staticmethod
    def named_slice(source_list: list, start: int = 0, end: int = None) -> list:
        """
        >>> source_list = [1, 2, 3, 4, 5]
        >>> sliced_list = ListExt.named_slice(source_list, 0, 2)
        >>> sliced_list
        [1, 2]
        """
        if end is None:
            end = len(source_list)

        nslice = slice(start, end)
        return source_list[nslice]

    @staticmethod
    def modify_with_slice(source_list: list, start: int, step: int, add_list: list) -> list:
        """
        >>> source_list = [1, 0, 3, 0, 5, 0, 7, 0, 9, 0]
        >>> modified_list = ListExt.modify_with_slice(source_list, 1, 2, [2, 4, 6, 8, 10])
        >>> modified_list
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        """
        source_list[start::step] = add_list
        return source_list

class ArrayExt:
    """
    Class with static methods extending python array operations
    """
    @staticmethod
    def store_floats_to_file(count: int, filename: str) -> None:
        """
        Store random floats to a binary file
        >>> ArrayExt.store_floats_to_file(10**5, 'test_floats.bin')
        True
        """
        from random import random
        floats = array.array('d', (random() for _ in range(count)))
        with open(filename, 'wb') as f:
            floats.tofile(f)

        floats2 = array.array('d')
        with open(filename, 'rb') as f:
            floats2.fromfile(f, count)

        return floats == floats2

class DequeExt:
    @staticmethod
    def create_deque_from_list(source_list: list) -> deque:
        """
        Create a deque from a list
        >>> from collections import deque
        >>> source_list = [1, 2, 3, 4, 5]
        >>> d = DequeExt.create_deque_from_list(source_list)
        >>> d
        deque([1, 2, 3, 4, 5])
        """
        return deque(source_list)

    @staticmethod
    def created_sized_deque_from_list(source_list: list, maxlen: int) -> deque:
        """
        Create a sized deque from a list
        >>> from collections import deque
        >>> source_list = [1, 2, 3, 4, 5]
        >>> d = DequeExt.created_sized_deque_from_list(source_list, 3)
        >>> d
        deque([3, 4, 5], maxlen=3)
        """
        return deque(source_list, maxlen=maxlen)

    @staticmethod
    def append_list_right_to_deque_with_lenght(source_deque: deque, added_list: list) -> int:
        """
        Append a list to the right of a deque and return its length
        >>> source_list = [1, 2, 3]
        >>> d = DequeExt.created_sized_deque_from_list([4, 5, 6, 7], maxlen=4)
        >>> dq = DequeExt.append_list_right_to_deque_with_lenght(d, source_list)
        >>> dq
        deque([7, 1, 2, 3], maxlen=4)

        """
        source_deque.extend(added_list)
        return source_deque


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
