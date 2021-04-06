# testing unit
from people.People import Person
import unittest

class SimpleTest(unittest.TestCase):

    test_person = Person() # create an object of our class

    def test_add(self): # naming convention - using 'test' in the name of your function
                        # will let the interpreter know that this needs to be tested
        self.assertEqual(bool(self.test_person.first_name), (not None))
