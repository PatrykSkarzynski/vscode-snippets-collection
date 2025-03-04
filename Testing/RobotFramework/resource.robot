*** Settings ***
Documentation    Resource file with reusable keywords and variables
... 
...              The system specific variables and keywords.
...              They utilize the SeleniumLibrary.
...    
Library          SeleniumLibrary


*** Variables ***
${url}                      https://rahulshettyacademy.com/loginpagePractise/
${browser}                  chrome

${Login_id}                 id:username
${Password_id}              id:password

${Login_Text}               rahulshettyacademy
${Invalid_Password_Text}    12345678
${Valid_Password_Text}      learning

${Login_Button_id}          id:signInBtn




*** Keywords ***
Open the browser with the Mortgage payment url
    Open Browser    ${url}    ${browser}

Close Browser Session
    Close Browser