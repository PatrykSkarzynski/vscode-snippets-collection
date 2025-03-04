import pytest
from account_manager import AccountManager


@pytest.fixture
def account_manager():
    return AccountManager()

def test_register(account_manager):
    result = account_manager.register("user1", "password123")
    assert result == "User registered successfully."
    assert "user1" in account_manager.user_data

def test_register_existing_user(account_manager):
    account_manager.register("user1", "password123")
    result = account_manager.register("user1", "newpassword")
    assert result == "Username already exists."

def test_login(account_manager):
    account_manager.register("user1", "password123")
    result = account_manager.login("user1", "password123")
    assert result == "Logged in successfully."
    assert account_manager.is_logged_in() == True

def test_login_with_wrong_password(account_manager):
    account_manager.register("user1", "password123")
    result = account_manager.login("user1", "wrongpassword")
    assert result == "Incorrect password."

def test_logout(account_manager):
    account_manager.register("user1", "password123")
    account_manager.login("user1", "password123")
    result = account_manager.logout()
    assert result == "Logged out successfully."
    assert account_manager.is_logged_in() == False

def test_change_password(account_manager):
    account_manager.register("user1", "password123")
    result = account_manager.change_password("user1", "password123", "newpassword")
    assert result == "Password changed successfully."
    assert account_manager.user_data["user1"] == "newpassword"

def test_change_password_with_incorrect_old_password(account_manager):
    account_manager.register("user1", "password123")
    result = account_manager.change_password("user1", "wrongpassword", "newpassword")
    assert result == "Incorrect old password."


# To start pytest:
# -----------------
# - Right Click on folder direction of your .py file and then click on "Open in integrated terminal"
# - type in the terminal 'pytest'
# - if you've got an error then type 'python -m pytest'
# - and name of your .py file, for example: 'python -m pytest .\mocks_pytest.py'

# expected result in terminal:
# collected 7 items
#
# .\account_manager_tests.py ....    [100%] 
#
# ============ 7 passed in 0.02s ============