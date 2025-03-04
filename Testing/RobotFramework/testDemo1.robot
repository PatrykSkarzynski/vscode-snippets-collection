*** Settings ***
Documentation    Use 'TAB' on the beginning of the values
...              Test To validate Login Form *Description of the Test Case*
...              To run test: 'python -m robot -filename-'
Library          SeleniumLibrary
Test Teardown    Close Browser Session
Resource         resource.robot


*** Variables ***
${Error_Message_Login}    css:.alert-danger


*** Test Cases ***
Validate UnSuccessful Login
    Open the browser with the Mortgage payment url
    Fill the login Form    ${Login_Text}    ${Invalid_Password_Text}
    Wait until it checks the login or error message
    Verify error message

*** Keywords ***
Open the browser with the Mortgage payment url
    Open Browser    ${url}   ${browser}

Fill the login Form
    [Arguments]    ${Login_Text}    ${Password_Text}
    Input Text        ${Login_id}      ${Login_Text}
    Input Password    ${Password_id}   ${Password_Text}
    Click Button      ${Login_Button_id}

Wait until it checks the login or error message
    Wait Until Element Is Visible    ${Error_Message_Login}    # Wait until the error message is visible

Verify error message
    ${result}=    Get Text    ${Error_Message_Login}    # create variable and get the error message text
    Should Be Equal As Strings   ${result}    Incorrect username/password.    # Verify the error message text
    # Second way to make this test:
    # # Element Text Should Be    ${Error_Message_Login}    Incorrect username/password.    # Verify the error message text