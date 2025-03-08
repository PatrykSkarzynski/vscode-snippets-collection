*** Settings ***
Documentation    
...
...              Test To validate Login Form *Description of the Test Case*
...
...              Use 'TAB' on the beginning of the values
...              To run test: 'python -m robot -filename-'
...
...              Test Cases are parameterized with username and password
...
...
Library          SeleniumLibrary
Library          DataDriver    file=../RobotFramework/resources/data.csv    encoding=UTF-8    dialect=unix    # Import the DataDriver library from resources directory
Test Teardown    Close Browser Session
Test Setup       Open the browser with the Mortgage payment url
Test Template    Validate UnSuccessful Login    # Use the template to run the test
Resource         ../Resources/Generic.robot


*** Variables ***
${Error_Message_Login}    css:.alert-danger


*** Test Cases ***
Login with user ${username} and password ${password}    xyz    12345678


*** Keywords ***
Validate UnSuccessful Login
    [Arguments]    ${username}    ${password}
    Open the browser with the Mortgage payment url
    Fill the login Form    ${username}    ${password}
    Wait until it checks the login or error message
    Verify error message

Fill the login Form
    [Arguments]    ${username}    ${password}
    Sleep             2s    # Wait for 5 seconds
    Input Text        ${Login_id}      ${username}
    Input Password    ${Password_id}   ${password}
    Click Button      ${Login_Button_id}

Wait until it checks the login or error message
    Wait Until Element Is Visible    ${Error_Message_Login}    # Wait until the error message is visible

Verify error message
    ${result} =    Get Text    ${Error_Message_Login}    # create variable and get the error message text
    Should Be Equal As Strings   ${result}    Incorrect username/password.    # Verify the error message text
    # Second way to make this test:
    # # Element Text Should Be    ${Error_Message_Login}    Incorrect username/password.    # Verify the error message text
