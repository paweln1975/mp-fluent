class ExpressionExt:
    @staticmethod
    def gen_tuple(symbols):
        return tuple(ord(symbol) for symbol in symbols)
    @staticmethod
    def gen_cartesian(list_a, list_b):
        list_ret = []
        for x in (f'{c} {s}' for c in list_a for s in list_b):
            list_ret.append(x)
        return list_ret



