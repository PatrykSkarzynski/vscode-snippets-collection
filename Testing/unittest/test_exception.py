import unittest

# creating 'divide' function that will be tested:
def divide(x, y):
    # when user try to divide by zero function will return error message "You can't divide by zero!":
    if y == 0:
        raise ValueError("You can't divide by zero!")
    return x / y

# creating 'MockDatabase' class that simulates interaction with external resource like database:
class MockDatabase:
    # mocked database with some values and 'id' parameters:
    def __init__(self):
        self.data = {'id1': 100, 'id2': 200}

    # function that returns data from mocked database by 'id':
    def get_data(self, id):
        return self.data.get(id)
    
# creating test class 'ComplexOperationsTest' which inherits from 'unittest.TestCase':
class ComplexOperationsTest(unittest.TestCase):

    # creating test method 'test_divide' which checks if function 'divide' works properly:
    def test_divide(self):
        # checking whether the function divides numbers correctly:
        self.assertEqual(divide(10, 2), 5)
        # checking whether the function gives back exception 'ValueError' while trying to divide by zero:
        with self.assertRaises(ValueError):
            divide(10, 0)

    # creating test method 'test_mock_database' which checks interaction with simulated database:
    def test_mock_database(self):
        # creating an instance of simulated database:
        db = MockDatabase()
        # checking whether method 'get_data' returns correct values:
        self.assertEqual(db.get_data('id1'), 100)
        # checking whether method 'get_data' returns None for not existing id:
        self.assertIsNone(db.get_data('id3'))

# condition that checks whether the script was run directly and not imported as a module, if so then function 'unittest.main()' runs every test method defined in the class:
if __name__ == '__main__':
    unittest.main()



# Expected result in terminal:
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s
#
# OK