import timeit

TIMES = 50000

SETUP = """
symbols = '$¢£¥€¤'
def non_ascii(c):
    return c > 127
"""


class ListExt:
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
    def clock(label, cmd):
        res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
        print(label, *(f'{x:.4f}' for x in res))


if __name__ == '__main__':
    ListExt.clock('listcomp        :', '[ord(s) for s in symbols if ord(s) > 127]')
    ListExt.clock('listcomp + func :', '[ord(s) for s in symbols if non_ascii(ord(s))]')
    ListExt.clock('filter + lambda :', 'list(filter(lambda c: c > 127, map(ord, symbols)))')
    ListExt.clock('filter + func   :', 'list(filter(non_ascii, map(ord, symbols)))')