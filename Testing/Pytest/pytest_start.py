import pytest


def multiply(x, y):
    return x * y

# usage of parametrization in Pytest for testing of the function 'multiply' with data sets:
## @pytest.mark.parametrize() is used to make data sets (test parameters) and expected results
@pytest.mark.parametrize("x, y, expected", [
    (2, 3, 6), # Test Case 1:  2 * 3 = 6
    (3, 7, 21), # Test Case 2:  3 * 7 = 21
    (5, 5, 25), # Test Case 3:  5 * 5 = 25
    (0, 4, 0) # Test Case 4:  0 * 4 = 0
])

# creating test method 'test_multiply' which checks if 'multiply' function is correct:
def test_multiply(x, y, expected):
    # verification of 'multiply(x, y)' results in expected output:
    assert multiply(x, y) == expected

# To start pytest:
# -----------------
# - Right Click on folder direction of your .py file and then click on "Open in integrated terminal"
# - type in the terminal 'pytest'
# - if you've got an error then type 'python -m pytest'
# - and name of your .py file, for example: 'python -m pytest .\pytest_start.py'

# expected result in terminal:
# collected 4 items                                                                                                                                                                          
#
# pytest_start.py ....    [100%] 
#
# ===== 4 passed in 0.01s =====