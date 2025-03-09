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
  --Converts from CSV, TXT and PY files.


## 2. Crypto Currency Exchange:
  --Simple program that downloads information about picked crypto with REQUESTS lib and measures,
  with perf_counter(), how much time this code require.


## 3. Financial data of listed Companies from the Server:
  --Aggregates data about picked companies and shows it on a graph.
  Used libraries:
  plotly, matplotlib.pyplot, pandas, tkinter, yfinance, selenium, time, traceback.


## 5. Pandas_NumPy:
  --Contains one files made in Jupyter Notebook.


## 6. Testing:
  --Contains all test files made with PyTest, Robot Framework, Selenium, Unitest.


## 7. Exchange Rates:
  --Contains one quick program which downloads exchange rates data to .JSON with request library and
  Unitest with Request to test server response.
