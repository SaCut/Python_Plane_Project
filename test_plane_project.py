# testing unit
from People import Person
import unittest

class SimpleTest(unittest.TestCase):

    test_person = Person() # create an object of our class

    def test_add(self): # naming convention - using 'test' in the name of your function
                        # will let the interpreter know that this needs to be tested
        self.assertEqual(self.test_person.(2, 4), 6)
    # this test is checking if 2

    def test_subtract(self):
        self.assertEqual(self.test_person.subtract(4, 2), 2)
        # if true the test passes

    def test_multiply(self):
        self.assertEqual(self.test_person.multiply(2, 2), 4)
        # this thest assesses if 2 * 2 = 4

    def test_divide(self):
        self.assertEqual(self.test_person.divide(12, 3), 4)

# pytest looks for any file with name including 'test*.py'