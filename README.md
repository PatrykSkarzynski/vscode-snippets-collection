# vscode-snippets-collection

[![LinkedIn](https://img.shields.io/badge/LinkedIn-PatrykSkarżyński-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/patryk-skarżyński-b20690173/)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)
![PyTest](https://img.shields.io/badge/PyTest-3.8%2B-yellow)
![RobotFramework](https://img.shields.io/badge/RobotFramework-5.0%2B-orange)
![Selenium](https://img.shields.io/badge/Selenium-4.0%2B-red)

*Welcome to **vscode-snippets-collection** repository! This project demonstrates the use of **Python**, **Selenium WebDriver**, and **Robot Framework** for automated testing and web scraping.*

##

### Features 🚀
- **Automated Testing**
- **Cross-Browser Support**
- **Scalable**
- **Easy Setup**

---

### Table of Contents

- [Technologies Used](#technologies-used)

---

## Sample of .robot test file 🛠️
```bash
*** Settings ***
Library          Collections
Library          RequestsLibrary


*** Variables ***
${base_url}     https://rahulshettyacademy.com
${book_id}
${book_name}    RobotFrameworkLearning


*** Test Cases ***
Add Book into Library BookDataBase
    [Tags]    API
    # Create a dictionary with key-value pairs
    &{req_body}=           Create Dictionary    name=${book_name}    isbn=9874    aisle=332145    author=Patryk Skarzynski

    ${response}=           POST    ${base_url}/Library/Addbook.php    json=${req_body}    expected_status=200    # Create dictionary from the response of the POST request
    Log                              ${response.json()}    # Returns the response in JSON format

    # Check if JSON response contains key 'ID'
    Dictionary Should Contain Key    ${response.json()}    ID
    ${book_id}=            Get From Dictionary    ${response.json()}    ID
    Set Global Variable              ${book_id}    ${book_id}    # Set the value of the key 'ID' as a global variable
    Log                              ${book_id}    # Returns the value of the key 'ID'

    # Check if the response contains the message 'successfully added'
    Should Be Equal As Strings    successfully added    ${response.json()}[Msg]    # Returns the value of the key 'Msg'
    Status Should Be       200    ${response}    # Check if the status code is 200

Get the Book Details
    [Tags]    API
    # Create dictionary from the response of the GET request
    ${get_response}=       GET    ${base_url}/Library/GetBook.php    params=ID=${book_id}    expected_status=200    # Create dictionary from the response of the GET request
    Log                              ${get_response.json()}    # Returns the response in JSON format

    # Return the value of the key 'book_name' from the first element of the response as list of dictionaries
    Should Be Equal As Strings       ${book_name}    ${get_response.json()}[0][book_name]
```

---

<details>
<summary>Content (Expandable)</summary>

##

**1. Converter to JSON:**

> Simple python script that converts a CSV file to a JSON file.
> The 'csv' library provides the 'DictReader' class which reads the CSV file and returns a dictionary for each row,
> library named 'json' provides the 'dump' function which writes the dictionary to the JSON file. The 'dump' function takes the dictionary and the file handler as arguments.
> 'Attrgetter' function from 'operator' library is used to get the value of a key in the dictionary.

## 

**2. Crypto Currency Exchange:**
  
> Program allows to check the current price of crypto currencies and buy them using the CoinGecko API,
> uses ses the 'requests' library to send requests to the CoinGecko API and the 'time' library to measure the time of code execution.

## 

**3. Financial data of listed Companies from the Server:**

> Program is a simple stock information program that uses the Yahoo Finance API to get the stock data of a company,
> uses the 'yfinance' library to get the stock data of a company by entering the stock ticker in the entry widget,
> displays the stock data in the text box widget, also displays the stock data history for the last month with daily intervals in the text box widget.

## 

**4. Pandas_NumPy:**
  
> Contains one file made in Jupyter Notebook, basicaly a notebook with some useful code.

## 

**5. Testing:**
  
> Contains all test files made with PyTest, Robot Framework, Selenium and Unitest.
> Example above shows partialy one of the files from Testing/RobotFramework/test_demo_files directory.

## 

**6. Exchange Rates:**
  
> Program is used to get the latest exchange rates from the exchange_rates_api website, provides the latest exchange rates for free:
>   * using the 'latest' endpoint, for 'USD', 'AUD', 'CAD', 'PLN', and 'MXN'
>   * using the 'symbols' parameter,
>   * using for a specific base currency using the 'base' parameter.

</details>

---

### Technologies Used

  * **Python**: programming language used for scripting and automation.
  * **Selenium WebDriver**: browser automation tool for interacting with web elements and performing actions like clicking, typing, and navigating.
  * **Robot Framework**: test automation framework for acceptance testing and acceptance test-driven development (ATDD).
