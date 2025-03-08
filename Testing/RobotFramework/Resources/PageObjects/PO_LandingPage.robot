*** Settings ***
Documentation    All the page objects and keywords related to the Landing Page
...
Library          SeleniumLibrary
Resource         ../Generic.robot


*** Variables ***
${Error_Message_Login}    css:.alert-danger


*** Keywords ***
Fill the login Form
    [Arguments]    ${username}    ${password}    # Pass arguments to the keyword
    Input Text        ${Login_id}      ${username}
    Input Password    ${Password_id}   ${password}
    Click Button      ${Login_Button_id}

Wait Until Element is Located in the Page
    Wait Until Element Is Visible    ${Error_Message_Login}


Verify Error Message is Correct
    ${result}=    Get Text    ${Error_Message_Login}    # create variable and get the error message text
    Should Be Equal As Strings   ${result}    Incorrect username/password.    # Verify the error message text
    # # Second way to make this test:
    # # Element Text Should Be    ${Error_Message_Login}    Incorrect username/password.    # Verify the error message text


Fill the Login Details and Select the User Option
    Input Text                       id:username    rahulshettyacademy
    Input Password                   id:password    learning
    Click Element                    css:input[value='user']    # Click the user option
    Wait Until Element Is Visible    css:.modal-body    # Wait until the pop up is visible
    Click Element                    id:okayBtn    # You can skip using the locator strategy and directly use the id
    Click Element                    id:okayBtn
    Wait Until Element Is Visible    css:.modal-body
    Select From List By Value        css:select.form-control    teach    # Select the option with value 'teach'
    Select Checkbox                  id:terms    # Select the checkbox
    Checkbox Should Be Selected      id:terms    # Verify the checkbox is selected
    # Click Button                     signInBtn    # Click the sign in button