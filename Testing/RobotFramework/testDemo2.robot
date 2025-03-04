*** Settings ***
Documentation    To validate Login Form
Library          SeleniumLibrary
Library          Collections
Test Setup       Open the browser with the Mortgage payment url
Test Teardown    Close Browser Session
Resource         resource.robot


*** Variables ***
${Error_Message_Login}    css:.alert-danger
${Shop_Page_Load}         .nav-link


*** Test Cases ***
# Validate UnSuccessful Login
#     Fill the Login Form    ${Login_Text}    ${Invalid_Password_Text}
#     Wait Until Element is Located in the Page    ${Error_Message_Login}
#     Verify Error Message is Correct

Validate Cards Display in the Shopping Page
    Fill the Login Form    ${Login_Text}    ${Valid_Password_Text}
    Wait Until Element Is Located in the Page    css:.nav-link    # Wait until 'css:.nav-link' is located in the page
    Verify Card Titles in the Shop Page
    Select the Card    Nokia Edge

Select the Form and Navigate to Child Window
    Fill the Login Details and Select the User Option


*** Keywords ***
Fill the login Form
    [Arguments]    ${Login_Text}    ${Password_Text}    # Pass arguments to the keyword
    Input Text        ${Login_id}      ${Login_Text}
    Input Password    ${Password_id}   ${Password_Text}
    Click Button      ${Login_Button_id}


Wait Until Element is Located in the Page
    [Arguments]    ${Page_Element}    # Putting 'css:.nav-link' in the new argument
    Wait Until Element Is Visible    ${Page_Element}    # Wait until 'css:.nav-link' is visible


Verify Error Message is Correct
    ${result}=    Get Text    ${Error_Message_Login}    # create variable and get the error message text
    Should Be Equal As Strings   ${result}    Incorrect username/password.    # Verify the error message text
    # # Second way to make this test:
    # # Element Text Should Be    ${Error_Message_Login}    Incorrect username/password.    # Verify the error message text


Verify Card Titles in the Shop Page
    [Documentation]    
    ...    
    ...    Verify the card titles names in the shop page are correct by comparing the expected and actual card titles names in two lists
    ...    
    ...    The expected card titles are: iphone X, Samsung Note 8, Nokia Edge, Blackberry
    ...    The actual card titles are: iphone X, Samsung Note 8, Nokia Edge, Blackberry
    ...    The expected and actual card titles are equal
    ...    
    ...    
    @{expectedList} =    Create List    iphone X    Samsung Note 8    Nokia Edge    Blackberry    # Create a list of expected card titles
    @{elements} =    Get WebElements    css:.card-title    # Get the list of actual card titles
    @{actualList} =      Create List    # Create an empty list to store the actual card titles
    FOR    ${element}    IN    @{elements}    # Iterate through the list of actual card titles
           Log    ${element.text}    # Log the actual card title
           Append To List    ${actualList}    ${element.text}    # Append the actual card title to the list
    END

    Lists Should Be Equal    ${expectedList}    ${actualList}    # Verify the expected and actual card titles are equal


Select the Card
    [Arguments]    ${cardName}    # Pass the argument containing card name to the keyword
    @{elements} =    Get WebElements    css:.card-title    # Get the list of card titles
    ${index} =       Set Variable    1    # Set the index to 1
    FOR    ${element}    IN    @{elements}    # Iterate through the list of card titles
           Exit For Loop If    '${cardName}' == '${element.text}'    # Compare the card name with the card title
           ${index} =    Evaluate    ${index} + 1    # Increment the index
    END
    Click Button    xpath:(//*[@class='card-footer'])[${index}]/button    # Click the button to add the card to the cart

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
    #Click Button                     signInBtn    # Click the sign in button