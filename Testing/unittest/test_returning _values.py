import unittest

# creating 'is_even' function that will be tested, returns True when number is even, otherwise returns False:
def is_even(number):
    return number % 2 == 0

# creating function 'filter_even' which filters from the list only even numbers: 
def filter_even(numbers_list):
    return[num for num in numbers_list if is_even(num)]

# creating test class 'BooleanAndListOperationsTest' which inherits from 'unittest.TestCase':
class BooleanAndListOperationsTest(unittest.TestCase):
    # creating test method 'test_is_even' which checks if function 'is_even' works properly:
    def test_is_even(self):
        self.assertTrue(is_even(2)) # correct values
        self.assertFalse(is_even(3)) # incorrect values

    # creating test method 'test_filter_even' which checks if function 'filter_even' works properly: 
    def test_filter_even(self):
        input_list = [1, 2, 3, 4, 5, 6] # list of values
        expected_output = [2, 4, 6] # expected output of test case
        # expected_output = [2, 4, 6, 1] # example with incorrect values for expected output
        self.assertEqual(filter_even(input_list), expected_output) # running 'filter_even' on our list

# condition that checks whether the script was run directly and not imported as a module, if so then function 'unittest.main()' runs every test method defined in the class:
if __name__ == '__main__':
    unittest.main()



# Expected result when True in terminal:
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s
#
# OK


# Expected result when True in terminal:
# ----------------------------------------------------------------------
#     self.assertEqual(filter_even(input_list), expected_output) # running 'filter_even' on our list
#     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# AssertionError: Lists differ: [2, 4, 6] != [2, 4, 6, 1]
#
# Second list contains 1 additional elements.
# First extra element 3:
# 1
#
# - [2, 4, 6]
# + [2, 4, 6, 1]
# ?         +++
#
#
#
# ----------------------------------------------------------------------
# Ran 2 tests in 0.001s
#
# FAILED (failures=1)