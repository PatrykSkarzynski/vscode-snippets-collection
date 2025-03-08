*** Settings ***
Documentation
...              When creating a dictionary, use &'s to create a dictionary and pass the key-value pairs'

Library          Collections
Library          RequestsLibrary


*** Variables ***
${base_url}     https://rahulshettyacademy.com
${book_id}
${book_name}    RobotFrameworkLearning


*** Test Cases ***
Play with Dictionary
    [Tags]    API
    &{data}=               Create Dictionary    name=Patryk    age=30    country=Poland    website=https://www.linkedin.com/in/patryk-skarżyński-b20690173/
    Log                              ${data}

    # Check if dictionary contains key
    Dictionary Should Contain Key    ${data}    name

    # Retrieve value from dictionary
    Log                              ${data}[name]    # Returns the value of the key 'name'
    Get From Dictionary              ${data}    name    # Returns the value of the key 'name'
    ${url}=                Get From Dictionary    ${data}    website    # Returns the value of the key 'website'
    Log                              ${url}


Add Book into Library BookDataBase
    [Tags]    API
    # Create a dictionary with key-value pairs
    &{req_body}=           Create Dictionary    name=${book_name}    isbn=9876    aisle=332145    author=Patryk Skarzynski

    ${response}=           POST    ${base_url}/Library/Addbook.php    json=${req_body}    expected_status=200    # Create dictionary from the response of the POST request
    Log                              ${response.json()}    # Returns the response in JSON format

    # Check if JSON response contains key 'ID'
    Dictionary Should Contain Key    ${response.json()}    ID
    ${book_id}=            Get From Dictionary    ${response.json()}    ID
    Set Global Variable              ${book_id}    ${book_id}    # Set the value of the key 'ID' as a global variable
    Log                              ${book_id}    # Returns the value of the key 'ID'

    # Check if the response contains the message 'successfully added'
    Should Be Equal As Strings    successfully added    ${response.json()}[Msg]    # Returns the value of the key 'Msg'
    Status Should Be       200    ${response}    # Check if the status code is 200

Get the Book Details
    [Tags]    API
    # Create dictionary from the response of the GET request
    ${get_response}=       GET    ${base_url}/Library/GetBook.php    params=ID=${book_id}    expected_status=200    # Create dictionary from the response of the GET request
    Log                              ${get_response.json()}    # Returns the response in JSON format

    # Return the value of the key 'book_name' from the first element of the response as list of dictionaries
    Should Be Equal As Strings       ${book_name}    ${get_response.json()}[0][book_name]

Delete the Book From Library DataBase
    [Tags]    API
    # Create dictionary from the response of the DELETE request
    &{delete_req}=         Create Dictionary    ID=${book_id}

    ${delete_response}=    POST    ${base_url}/Library/DeleteBook.php    json=${delete_req}    expected_status=200
    Log                              ${delete_response.json()}    # Returns the response in JSON format

    # Check if the response contains the message 'book is successfully deleted'
    Should Be Equal As Strings    book is successfully deleted    ${delete_response.json()}[Msg]    # Returns the value of the key 'Msg'
