# My Repo(sitory)



## Example:
``` Stock Info from Yahoo Finance API
# Function_for_downloading_stock_data and_displaying_it in the text box
def downloadData(e):    # e for event
    textBox.delete("1.0", tk.END)
    stock = str(e.widget.get())

    # Check if the stock ticker is empty or not
    if not stock:
        print("No stock ticker!")
        return

    # Get the stock data from Yahoo Finance API
    stock = stock.upper().strip()
    print("download stock data: ", stock)

    stockData = yf.Ticker(stock)
    print(stockData.info)

    textBox.insert(tk.END, "Ticker: " + stock + " \n\n")

    # Display the stock data in the text box widget
    for key in stockData.info.keys():
        try:
            v = str(key) + ": " + stockData.info[str(key)] + " \n\n "
            textBox.insert(tk.END, v)
        except KeyError:
            pass

    # Get the history of the stock data for the last month with daily intervals
    history = stockData.history(period="1mo", interval="1d")
    # 1mo, 1m, 1d, 1y, 1wk
    textBox.insert(tk.END, history)
```
##
## 1. Converter to JSON:

  Simple python script that converts a CSV file to a JSON file.
  The 'csv' library provides the 'DictReader' class which reads the CSV file and returns a dictionary for each row,
  library named 'json' provides the 'dump' function which writes the dictionary to the JSON file. The 'dump' function takes the dictionary and the file handler as arguments.
  'Attrgetter' function from 'operator' library is used to get the value of a key in the dictionary.


## 2. Crypto Currency Exchange:
  
  Program allows to check the current price of crypto currencies and buy them using the CoinGecko API,
  uses ses the 'requests' library to send requests to the CoinGecko API and the 'time' library to measure the time of code execution.


## 3. Financial data of listed Companies from the Server:

  Program is a simple stock information program that uses the Yahoo Finance API to get the stock data of a company,
  uses the 'yfinance' library to get the stock data of a company by entering the stock ticker in the entry widget,
  displays the stock data in the text box widget, also displays the stock data history for the last month with daily intervals in the text box widget.


## 5. Pandas_NumPy:
  --Contains one files made in Jupyter Notebook.


## 6. Testing:
  --Contains all test files made with PyTest, Robot Framework, Selenium, Unitest.


## 7. Exchange Rates:
  --Contains one quick program which downloads exchange rates data to .JSON with request library and
  Unitest with Request to test server response.
