import unittest
import doctest
import data_structs.deck
import data_structs.vector
import sequences.list_comp
import sequences.num_py


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(data_structs.deck))
    tests.addTests(doctest.DocTestSuite(data_structs.vector))
    tests.addTests(doctest.DocTestSuite(sequences.list_comp))
    tests.addTests(doctest.DocTestSuite(sequences.num_py))
    return tests


if __name__ == "__main__":
    unittest.main(verbosity=2)