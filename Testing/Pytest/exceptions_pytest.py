import pytest


def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

# creating test method 'test_divide_zero' which checks if 'divide' function raises a ValueError when attempting to divide by zero:
def test_divide_zero():
    with pytest.raises(ValueError) as excinfo:
        divide(10, 0)
    # checks if exception message is correct
    assert "Cannot divide by zero" in str(excinfo.value)

# creating test method 'test_divide_zero' which checks if 'divide' function returns correct result when dividing two correct numbers:
def test_divide_valid():
    assert divide(10, 2) == 5 # checks if 10 divided by 2 equals 5


# To start pytest:
# -----------------
# - Right Click on folder direction of your .py file and then click on "Open in integrated terminal"
# - type in the terminal 'pytest'
# - if you've got an error then type 'python -m pytest'
# - and name of your .py file, for example: 'python -m pytest .\exceptions_pytest.py'

# expected result in terminal:
# collected 2 items
#
# exceptions_pytest.py ....    [100%] 
#
# ============ 2 passed in 0.01s ============