import pytest


# creating fixture that will return lists for tests:
@pytest.fixture(params = [
    ([1, 2, 3], True), # Test Case 1: sorted list
    ([3, 2, 1], False), # Test Case 2: unsorted list
    ([], True), # Test Case 3: empty list
])
# creating 'list_data' function with information about fixture returning lists and expected result if they are sorted
def list_data(request):
    return request.param

# creating 'is_sorted' function for testing if a list is sorted
def is_sorted(lst):
    # all will return "True" if every element is true
    return all(lst[1] <= lst[i + 1] for i in range(len(lst) - 1))

# creating test method 'test_is_sorted' which is using fixture for checking if 'is_sorted' function identifies correctly lists as sorted or not:
def test_is_sorted(list_data):
    lst, expected = list_data
    assert is_sorted(lst) == expected


# To start pytest:
# -----------------
# - Right Click on folder direction of your .py file and then click on "Open in integrated terminal"
# - type in the terminal 'pytest'
# - if you've got an error then type 'python -m pytest'
# - and name of your .py file, for example: 'python -m pytest .\fixtures_pytest.py'

# expected result in terminal:
# collected 3 items
#
# fixtures_pytest.py ....    [100%] 
#
# ============ 3 passed in 0.01s ============