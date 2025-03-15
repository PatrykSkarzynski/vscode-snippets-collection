<div align="center">
  <h1>vscode-snippets-collection</h1>

  ![Python](https://img.shields.io/badge/Python-3.10%2B-green?style=plastic&labelColor=000000&logo=python&logoColor=20a7db)
  ![PyTest](https://img.shields.io/badge/PyTest-3.8%2B-green?style=plastic&logo=pytest&labelColor=000000&logoColor=20a7db)
  ![HTML](https://img.shields.io/badge/HTML-5-orange?style=plastic&logoSize=auto&logo=html5&labelColor=000000&logoColor=20a7db)
  ![Selenium](https://img.shields.io/badge/Selenium-4.0%2B-orange?style=plastic&logoSize=auto&logo=selenium&labelColor=000000&logoColor=20a7db)
  ![RobotFramework](https://img.shields.io/badge/Robot%20Framework-5.0%2B-orange?style=plastic&logoSize=auto&logo=robotframework&labelColor=000000&logoColor=20a7db)
  ![JupyterNotebook](https://img.shields.io/badge/Jupyter%20Notebook-7.3%2B-red?style=plastic&logo=jupyter&labelColor=000000&logoColor=20a7db)

  [![LinkedIn](https://img.shields.io/badge/LinkedIn-Patryk%20Skar%C5%BCy%C5%84ski-skyblue?style=plastic&labelColor=000000&logoSize=auto&logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiA/PjxzdmcgaGVpZ2h0PSI3MiIgdmlld0JveD0iMCAwIDcyIDcyIiB3aWR0aD0iNzIiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGcgZmlsbD0ibm9uZSIgZmlsbC1ydWxlPSJldmVub2RkIj48cGF0aCBkPSJNOCw3MiBMNjQsNzIgQzY4LjQxODI3OCw3MiA3Miw2OC40MTgyNzggNzIsNjQgTDcyLDggQzcyLDMuNTgxNzIyIDY4LjQxODI3OCwtOC4xMTYyNDUwMWUtMTYgNjQsMCBMOCwwIEMzLjU4MTcyMiw4LjExNjI0NTAxZS0xNiAtNS40MTA4MzAwMWUtMTYsMy41ODE3MjIgMCw4IEwwLDY0IEM1LjQxMDgzMDAxZS0xNiw2OC40MTgyNzggMy41ODE3MjIsNzIgOCw3MiBaIiBmaWxsPSIjMDA3RUJCIi8+PHBhdGggZD0iTTYyLDYyIEw1MS4zMTU2MjUsNjIgTDUxLjMxNTYyNSw0My44MDIxMTQ5IEM1MS4zMTU2MjUsMzguODEyNzU0MiA0OS40MTk3OTE3LDM2LjAyNDUzMjMgNDUuNDcwNzAzMSwzNi4wMjQ1MzIzIEM0MS4xNzQ2MDk0LDM2LjAyNDUzMjMgMzguOTMwMDc4MSwzOC45MjYxMTAzIDM4LjkzMDA3ODEsNDMuODAyMTE0OSBMMzguOTMwMDc4MSw2MiBMMjguNjMzMzMzMyw2MiBMMjguNjMzMzMzMywyNy4zMzMzMzMzIEwzOC45MzAwNzgxLDI3LjMzMzMzMzMgTDM4LjkzMDA3ODEsMzIuMDAyOTI4MyBDMzguOTMwMDc4MSwzMi4wMDI5MjgzIDQyLjAyNjA0MTcsMjYuMjc0MjE1MSA0OS4zODI1NTIxLDI2LjI3NDIxNTEgQzU2LjczNTY3NzEsMjYuMjc0MjE1MSA2MiwzMC43NjQ0NzA1IDYyLDQwLjA1MTIxMiBMNjIsNjIgWiBNMTYuMzQ5MzQ5LDIyLjc5NDAxMzMgQzEyLjg0MjA1NzMsMjIuNzk0MDEzMyAxMCwxOS45Mjk2NTY3IDEwLDE2LjM5NzAwNjcgQzEwLDEyLjg2NDM1NjYgMTIuODQyMDU3MywxMCAxNi4zNDkzNDksMTAgQzE5Ljg1NjY0MDYsMTAgMjIuNjk3MDA1MiwxMi44NjQzNTY2IDIyLjY5NzAwNTIsMTYuMzk3MDA2NyBDMjIuNjk3MDA1MiwxOS45Mjk2NTY3IDE5Ljg1NjY0MDYsMjIuNzk0MDEzMyAxNi4zNDkzNDksMjIuNzk0MDEzMyBaIE0xMS4wMzI1NTIxLDYyIEwyMS43Njk0MDEsNjIgTDIxLjc2OTQwMSwyNy4zMzMzMzMzIEwxMS4wMzI1NTIxLDI3LjMzMzMzMzMgTDExLjAzMjU1MjEsNjIgWiIgZmlsbD0iI0ZGRiIvPjwvZz48L3N2Zz4=)](https://www.linkedin.com/in/patryk-skarżyński-b20690173/)
  [![Confluence](https://img.shields.io/badge/Confluence-Patryk%20Skarżyński-skyblue?style=plastic&labelColor=000000&logo=confluence&logoColor=20a7db)](https://skarzyn.atlassian.net/wiki/spaces/~61fc8a73aab3620070f6d2b6/overview)
</div>

---

<div align="center">

  <h3>🛠️ Sample of .robot test file</h3>
</div>

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

<div align="center">
  <h3>⚠️ Fun Fact 1</h3>
  This project was built while listening to Power Metal 🎶
</div>

  ---

<details>
  <summary align="center">
    <h3>Content (Expandable)</h3>
  </summary>

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
   > * using the 'latest' endpoint, for 'USD', 'AUD', 'CAD', 'PLN', and 'MXN'
   > * using the 'symbols' parameter,
   > * using for a specific base currency using the 'base' parameter.
  
</details>

---

<h3>🟡 Technologies</h3>

   * **Python**: programming language used for scripting and automation.
   * **Selenium WebDriver**: browser automation tool for interacting with web elements and performing actions like clicking, typing, and navigating.
   * **Robot Framework**: test automation framework for acceptance testing and acceptance test-driven development (ATDD).

##

<h3>🔴 Features</h3>

- **Automated Testing**
- **Cross-Browser Support**
- **Scalable**
- **Easy Setup**

---

<div align="center">
  <h3>📸 Screenshots</h3>
  
  ![Screenshot 1](https://i.imgur.com/rKNyKot.jpeg)
</div>

---

<div align="center">
  <h3>⚠️ Fun Fact 2</h3>
  This project will be updated while listening to Power Metal 🎶🎶
</div>
