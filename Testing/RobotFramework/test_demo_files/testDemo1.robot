*** Settings ***
Documentation    Use 'TAB' on the beginning of the values
...              Test To validate Login Form *Description of the Test Case*
...              To run test file: 'python -m robot -filename-'
Library          SeleniumLibrary
Test Teardown    Close Browser Session
Resource         ../Resources/Generic.robot


*** Variables ***
${Error_Message_Login}    css:.alert-danger


*** Test Cases ***
Validate UnSuccessful Login
    Open the browser with the Mortgage payment url
    Fill the login Form    ${username}    ${invalid_password}
    Wait until it checks the login or error message
    Verify error message

*** Keywords ***
Open the browser with the Mortgage payment url
    Open Browser    ${url}   ${browser}

Fill the login Form
    [Arguments]    ${username}    ${invalid_password}
    Input Text        ${Login_id}      ${username}
    Input Password    ${Password_id}   ${invalid_password}
    Click Button      ${Login_Button_id}

Wait until it checks the login or error message
    Wait Until Element Is Visible    ${Error_Message_Login}    # Wait until the error message is visible

Verify error message
    ${result} =    Get Text    ${Error_Message_Login}    # create variable and get the error message text
    Should Be Equal As Strings   ${result}    Incorrect username/password.    # Verify the error message text
    # Second way to make this test:
    # # Element Text Should Be    ${Error_Message_Login}    Incorrect username/password.    # Verify the error message text