*** Settings ***
Documentation    Use 'TAB' on the beginning of the values
...              Test To validate Login Form *Description of the Test Case*
...              To run test: 'python -m robot -filename-'
Library          SeleniumLibrary
Library          String
Library          Collections
Test Setup       Open the browser with the Mortgage payment url
Test Teardown    Close Browser Session
Resource         resource.robot


*** Variables ***
${Error_Message_Login}    css:.alert-danger


*** Test Cases ***
Validate Child Window Functionality
    Select the Link of Child Window
    Verify the User is Switched to Child Window
    Grab the Email ID in the Child Window
    Switch To Parent Window and Enter the Email ID


*** Keywords ***
Select the Link of Child Window
    Click Element    css:.blinkingText
    Sleep            5s    # Wait for 5 seconds
    
Verify the User is Switched to Child Window
    Switch Window    NEW    # Switch to the new window
    Element Text Should Be    css:h1    DOCUMENTS REQUEST    # Verify the text in the new window is 'Documents requests'

Grab the Email ID in the Child Window
    ${text} =           Get Text    css:.red
    ${words} =          Split String    ${text}
    ${emailNeeded} =    Get From List   ${words}    4
    Log    ${emailNeeded}
    Set Global Variable    ${emailNeeded}    # Set the email ID as a global variable

Switch To Parent Window and Enter the Email ID
    Switch Window      MAIN    # Switch to the main window
    Title Should Be    LoginPage Practise | Rahul Shetty Academy    # Verify the title of the main window is 'LoginPage Practise | Rahul Shetty Academy'
    Input Text         id:username    ${emailNeeded}    # Input the email ID in the main window
