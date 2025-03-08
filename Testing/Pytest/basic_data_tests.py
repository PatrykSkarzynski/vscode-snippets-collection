import pytest


# creating function 'reverse_string' which will reverse string and return it:
def reverse_string(s):
    return s[::-1]

# creating function 'add_to_list' which will add an item and return list:
def add_to_list(lst, item):
    lst.append(item)
    return lst

# creating function 'update_dictionary' which will update dictionary with a key-value pair and return the dictionary:
def update_dictionary(dct, key, value):
    dct[key] = value
    return dct


# Tests:
# --------
# creating test method 'test_reverse_string' which checks if 'reverse_string' function works properly:
def test_reverse_string():
    assert reverse_string("Hello") == "olleH" # Test Case 1: tests if simple string is reversed correctly

# usage of parametrization in Pytest for testing of the function 'add_to_list' with data sets:
@pytest.mark.parametrize("lst, item, expected", [
    ([1, 2], 3, [1, 2, 3]), # Test Case 2:  Adding to a list of integers
    (["a", "b"], "c", ["a", "b", "c"]), # Test Case 3:  Adding to a list of strings
])
# creating test method 'test_add_to_list' which checks if 'add_to_list' function works properly:
def test_add_to_list(lst, item, expected):
    assert add_to_list(lst, item) == expected # tests if an item is added correctly to a list

# usage of parametrization in Pytest for testing of the function 'update_dictionary' with data sets:
@pytest.mark.parametrize("dct, key, value, expected", [
    ({"a": 1}, "b", 2, {"a": 1, "b": 2}), # Test Case 4: Adding a new key-value pair
    ({"x": 10}, "x", 20, {"x": 20}) # Test Case 5: Updating an existing key
])
# creating test method 'test_update_dictionary' which checks if 'update_dictionary' function works properly:
def test_update_dictionary(dct, key, value, expected):
    assert update_dictionary(dct, key, value) == expected # tests if a dictionary is correctly updated with a key-value pair


# To start pytest:
# -----------------
# - Right Click on folder direction of your .py file and then click on "Open in integrated terminal"
# - type in the terminal 'pytest'
# - if you've got an error then type 'python -m pytest'
# - and name of your .py file, for example: 'python -m pytest .\basic_data_tests.py'

# expected result in terminal:
# collected 5 items
#
# basic_data_tests.py ....    [100%] 
#
# ============ 5 passed in 0.02s ============