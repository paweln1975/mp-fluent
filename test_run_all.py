import doctest
import unittest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocFileSuite("data_structs\\tests\\deck.doctest"))
    return tests


if __name__ == "__main__":
    unittest.main()
