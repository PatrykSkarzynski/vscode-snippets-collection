import pytest


# creating basic math operations class:
class MathOperations:
    def __init__(self, base_value = 0):
        self.base_value = base_value

    def add(self, value):
        return self.base_value + value
    
    @staticmethod
    def subtract(a, b):
        return a - b
    
    @classmethod
    def multiply(cls, a, b):
        return a * b
    
# creating test method 'test_add' which checks if 'add' instance method  of 'MathOperations' class works correctly:
def test_add():
    math_op = MathOperations(10) # initialization of class instance with 'base_value' = 10
    assert math_op.add(5) == 15 # testing 'add' method with adding 5 to 'base_value'

# creating test method 'test_subtract' which checks if 'subtract' static method  of 'MathOperations' class works correctly:
def test_subtract():
    assert MathOperations.subtract(10, 5) == 5 # testing 'subtract' method

# creating test method 'test_multiply' which checks if 'multiply' class method  of 'MathOperations' class works correctly:
def test_multiply():
    assert MathOperations.multiply(3, 4) == 12 # testing 'multiply' method


# To start pytest:
# -----------------
# - Right Click on folder direction of your .py file and then click on "Open in integrated terminal"
# - type in the terminal 'pytest'
# - if you've got an error then type 'python -m pytest'
# - and name of your .py file, for example: 'python -m pytest .\exceptions_pytest.py'

# expected result in terminal:
# collected 3 items
#
# test_classes_pytest.py ....    [100%] 
#
# ============ 3 passed in 0.01s ============