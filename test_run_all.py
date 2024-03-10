import doctest
import unittest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocFileSuite("data_structs\\tests\\deck.doctest"))
    tests.addTests(doctest.DocFileSuite("data_structs\\tests\\vector2d.doctest"))
    return tests


if __name__ == "__main__":
    unittest.main()




