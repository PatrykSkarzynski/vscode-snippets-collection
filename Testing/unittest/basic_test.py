import unittest

# creating 'add' function that will be tested:
def add(x, y):
    return x + y

# creating 'subtract' function that also will be tested:
def subtract(x, y):
    return x - y

# creating test class 'ArithmeticOperationsTest' which inherits from 'unittest.TestCase':
class ArithmeticOperationsTest(unittest.TestCase):
    # creating test method 'test_add' which checks if 'add' function works properly:
    def test_add(self): # you should always use "test" in the test method name 
        # once calling method 'assertEqual' to check whether result of the function 'add' matches the expected value:
        self.assertEqual(add(1, 2), 3) # first value is the operation values and second is expected result (fails if the two objects are unequal)

    # similar to method 'test_add', creating test method to check if similarly named function works properly:
    def test_subtract(self):
        # calling method assertEqual three times to check whether result of the function add matches the expected value:
        self.assertEqual(subtract(3, 2), 1)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)

# condition that checks whether the script was run directly and not imported as a module, if so then function 'unittest.main()' runs every test method defined in the class:
if __name__ == '__main__':
    unittest.main()



# Expected result in terminal:
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s
#
# OK