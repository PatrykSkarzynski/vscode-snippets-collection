from unittest.mock import MagicMock, patch
import pytest


# creating function 'fetch_data' which will be sending requests to API:
def fetch_data(api_client, url):
    response = api_client.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
# creating test method 'test_ExternalService' which uses mock to simulate response from external service:
def test_fetch_data():
    mock_api_client = MagicMock()
    mock_api_client.get.return_value.status_code = 200
    mock_api_client.get.return_value.json.return_value = {"data": "Test data"}

    # calling function with mock API client:
    result = fetch_data(mock_api_client, "http://fakeurl.com")

    # checking if result is as expected
    assert result == {"data": "Test data"}

    # verification if mock was called with expected URL:
    mock_api_client.get.assert_called_with("http://fakeurl.com")


# To start pytest:
# -----------------
# - Right Click on folder direction of your .py file and then click on "Open in integrated terminal"
# - type in the terminal 'pytest'
# - if you've got an error then type 'python -m pytest'
# - and name of your .py file, for example: 'python -m pytest .\mocks_pytest.py'

# expected result in terminal:
# collected 1 items
#
# mocks_pytest.py ....    [100%] 
#
# ============ 1 passed in 0.05s ============