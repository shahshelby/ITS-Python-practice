import unittest

a = 3
b = 5


class test1(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(3 + 5, a + b)

    def test_greater(self):
        self.assertTrue(a + b > 5 + 10)


if __name__ == '__main__':
    unittest.main()

"""
raise keyword to display actual error message to user
not all syntax errors have red squiggly line, misspelled keyword can go unnoticed too like prnit and print
runtime errors are not result of syntax issues in code
logic error are the toughest to find since they dont crash or stop app from running
else happen when try works successfully,
finally execute everytime
"""