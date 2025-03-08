*** Settings ***
Documentation    All the page objects and keywords related to the Shop Page
...
Library          SeleniumLibrary
Resource         ../Generic.robot


*** Variables ***
${Shop_Page_Load}         css:.nav-link


*** Keywords ***
Wait Until Element is Located in the Page
    Wait Until Element Is Visible    ${Shop_Page_Load}


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