*** Settings ***
Documentation    All the page objects and keywords related to the Shop Page
...
Library          SeleniumLibrary
Resource         ../Generic.robot


*** Variables ***
${Shop_Page_Load}      css:.nav-link
${country_location}    //a[text()='India']


*** Keywords ***
Enter the Country and Select the Terms
    [Arguments]    ${country_name}    # Pass the argument containing the country name to the keyword
    Input Text       country    ${country_name}    # Input the country name in the text field
    Sleep            5s    # Wait for 5 seconds
    Generic.Wait Until Element is Located in the Page    //a[text()='${country_name}']    # Wait until the country name is located in the page
    Click Element    //a[text()='${country_name}']    # Click the country name
    Sleep            3s    # Wait for 3 seconds
    Click Element    css:.checkbox label    # Click the checkbox label


Purchase the Products and Confirm the Purchase
    Click Button     css:.btn-success    # Click the purchase button
    Page Should Contain    Success!    # Verify the purchase is successful