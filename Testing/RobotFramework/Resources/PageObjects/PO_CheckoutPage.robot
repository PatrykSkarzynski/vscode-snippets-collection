*** Settings ***
Documentation    All the page objects and keywords related to the Checkout Page
...
Library          SeleniumLibrary
Resource         ../Generic.robot


*** Variables ***
${Shop_Page_Load}         css:.nav-link


*** Keywords ***
Verify items in the Checkout Page and Proceed
    Click Element    css:.btn-success
    