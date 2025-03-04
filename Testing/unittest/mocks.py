import unittest
from unittest.mock import MagicMock


# creating function 'reverse_string' which will reverse string:
def reverse_string(s):
    return s[::-1]

# creating function 'capitalize_string' which will capitalize string:
def capitalize_string(s):
    return s.capitalize()

# creating class 'ExternalService' which simulates for example weather service:
class ExternalService:
    # creating empty method to be mocked:
    def get_weather(self, city):
        pass

# creating test class 'StringAndMockOperationsTest' which inherits from 'unittest.TestCase':
class StringAndMockOperationsTest(unittest.TestCase):
    # creating test method 'test_reverse_string' which checks if 'reverse_string' function works properly:
    def test_reverse_string(self):
        self.assertEqual(reverse_string("abc"), "cba")
        self.assertEqual(reverse_string("Hello"), "olleH")

    # creating test method 'test_capitalize_string' which checks if 'capitalize_string' function works properly:
    def test_capitalize_string(self):
        self.assertEqual(capitalize_string("hello"), "Hello")
        self.assertEqual(capitalize_string("test"), "Test")

    # creating test method 'test_ExternalService' which uses mock to simulate response from external service:
    def test_ExternalService(self):
        # creating mock for ExternalService:
        mock_service = ExternalService()
        # using "Sunny" result in mock service as external result:
        mock_service.get_weather = MagicMock(return_value = "Sunny")

        # checking whether mock returns expected result:
        self.assertEqual(mock_service.get_weather("Warsaw"), "Sunny")

        # checking whether method 'get_weather' was called with expected argument:
        mock_service.get_weather.assert_called_with("Warsaw")

# condition that checks whether the script was run directly and not imported as a module, if so then function 'unittest.main()' runs every test method defined in the class:
if __name__ == '__main__':
    unittest.main()



# Expected result when True in terminal:
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s
#
# OK