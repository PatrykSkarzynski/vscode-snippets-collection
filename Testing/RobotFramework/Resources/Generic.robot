*** Settings ***
Documentation    
...              --------------------------------------------
...              Resource file with reusable keywords and variables
...              --------------------------------------------
...              The resource file 'Generic.robot' is used to store the common keywords and variables,
...              they utilize the SeleniumLibrary.
...
...              Use 'TAB' on the beginning of the values.
...              --------------------------------------------
...
...
...              robot framework:
...              -----------------
...              To RUN test file:
...              'python -m robot filename.robot'
...
...              To RUN ALL test files:
...              'python -m robot .',
...
...              To run a specific test file with PICKED Browser:
...              'python -m robot --variable browservariablename:browsername filename.robot',
...
...              To run a specific test case for PICKED Test File:
...              'python -m robot -t "Validate Cards Display in the Shopping Page" filename.robot',
...
...              To run a search for specific test case in entire folder:
...              'python -m robot -t "Validate Cards Display in the Shopping Page"  .',
...
...              To run a search for specific test case in entire folder, which starts with 'Validate':
...              'python -m robot -t "Validate*"  .',
...
...              To run a specific tests which include One test tag in entire folder:
...              'python -m robot --include SMOKE    .',
...
...              To run a specific tests with PICKED Browser, which include One test tag:
...              'python -m robot --variable browservariablename:browsername --include SMOKE filename.robot',
...
...
...              To run a specific tests which include Multiple test tag with 'OR' in entire folder:
...              'python -m robot --include SMOKE --include SMOKEORREGRESSION    .',
...              # The above command will not work if the test case has both tags
...
...              To run a specific tests which include Multiple test tag with 'AND' in entire folder:
...              'python -m robot --include SMOKE --include SMOKEANDREGRESSION    .',
...              # The above command will not work if tester use filename.robot which contains no matching tags
...
...              To run a specific tests which exclude tag in entire folder:
...              'python -m robot --exclude SMOKE    .',
...
...              To run a specific test for picked different test folder:
...              'python -m robot --suite tests    .', 
...              # The above command will not work if the test folder doesn't exist
...
...              To run a only failed tests in entire folder:
...              'python -m robot --rerunfailed output.xml    .'
...              # The above command will not work if 'output.xml' file doesn't contain any failed tests
...
...
...              pabot:
...              -----------------
...              To run all test files after installing pabot plugin: 'pabot .'
...
...              To split execution on test level: 'pabot --testlevelsplit filename.robot'
...
...
...              Run in the terminal the following commands:
...              --------------------------------------------
...              pip install --upgrade robotframework-datadriver
...              pip install --upgrade robotframework-seleniumlibrary
...              pip install -U robotframework-pabot
...              pip install robotframework-requests
...              --------------------------------------------

Library          SeleniumLibrary



*** Variables ***
${url}                      https://rahulshettyacademy.com/loginpagePractise/
${browser}                  chrome

${Login_id}                 id:username
${Password_id}              id:password

${username}                 rahulshettyacademy
${invalid_password}         12345678
${password}                 learning

${Login_Button_id}          id:signInBtn



*** Keywords ***
Open the browser with the Mortgage payment url
    Open Browser    ${url}    ${browser}

Open the browser with the url
    Open Browser    ${url}    ${browser}    executable_path=../resources/webdrivers/${browser}

Wait Until Element is Located in the Page
    [Arguments]    ${page_locator}
    Wait Until Element Is Visible    ${page_locator}


Close Browser Session
    Close Browser
