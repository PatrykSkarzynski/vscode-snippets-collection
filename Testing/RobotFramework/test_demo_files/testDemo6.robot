*** Settings ***
Documentation    To validate Login Form
...
...              PO = Page Object
...              'country_name' requires exact match from the dropdown list of countries from the website
...
Library          SeleniumLibrary
Library          Collections
Library          ../customlibraries/Shop.py
Test Setup       Open the browser with the Mortgage payment url
Suite Setup
Suite Teardown
Test Teardown    Close Browser Session
Resource         ../Resources/PageObjects/PO_LandingPage.robot
Resource         ../Resources/PageObjects/PO_ShopPage.robot
Resource         ../Resources/PageObjects/PO_CheckoutPage.robot
Resource         ../Resources/PageObjects/PO_ConfirmationPage.robot


*** Variables ***
${List_of_products}       iphone X    Samsung Note 8    Nokia Edge    Blackberry
${country_name}           India


*** Test Cases ***
Validate UnSuccessful Login
    [Tags]    SMOKE    REGRESSION
    PO_LandingPage.Fill the Login Form       ${username}    ${invalid_password}
    PO_LandingPage.Wait Until Element is Located in the Page
    PO_LandingPage.Verify Error Message is Correct

Validate Cards Display in the Shopping Page
    [Tags]    REGRESSION
    PO_LandingPage.Fill the Login Form       ${username}    ${password}
    PO_ShopPage.Wait Until Element is Located in the Page
    PO_ShopPage.Verify Card Titles in the Shop Page
    Shop.add_item_to_cart_and_checkout       ${List_of_products}
    PO_CheckoutPage.Verify items in the Checkout Page and Proceed
    PO_ConfirmationPage.Enter the Country and Select the Terms    ${country_name}
    PO_ConfirmationPage.Purchase the Products and Confirm the Purchase

# Select the Form and Navigate to Child Window
#     PO_LandingPage.Fill the Login Details and Select the User Option
