# in terminal: pip install matplotlib/plotly/

# 1st way (with pyplot, user input,
# change of datetime format and simple graph):
# ---------------------------------------------
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import time

# 2nd way (OFFLINE with plotly, because for almost 6 years plotly is broken,
# with interactive chart for one stock):
# ---------------------------------------------------------------------------
import plotly.graph_objects as go


# measurement of code execution time (Start):
PS_pyplot_input_timeStart = time.perf_counter()

ticker = "TSLA"

# setting up user input for stock ticker:
userTicker = input("Write ticker name:").lower().strip()
if userTicker:
    ticker = userTicker

    # setting up download of stock data for desired ticker:
    data = yf.download(tickers=ticker, start='2017-01-01',
                       end='2022-12-31', rounding=True)
    # can also use: period = "5y", interval = "1mo"

    data.index = pd.to_datetime(data.index, format='%Y-%m-%d %I-%p')
    # changing datetime format
    print("Data from server for ticker:", ticker)
    print(data)

    # setting up graph:
    plt.figure(figsize=(15, 5))
    plt.title('Apple Stock Prizes for 5 years')
    plt.xlabel('Year')
    plt.ylabel('Price')

    plt.plot(data['Close'])

# measurement of code execution time (End):
PS_pyplot_input_timeEnd = time.perf_counter()

# measure code time:
PS_pyplot_input_timeInterval = PS_pyplot_input_timeEnd - PS_pyplot_input_timeStart
print("\nElapsed time for pyplot with user input code:",
      PS_pyplot_input_timeInterval, "second")
# Elapsed time for pyplot with user input code: 2.3920836000033887 seconds


# 2nd way (OFFLINE with plotly, because for almost 6 years plotly is broken,
# with interactive chart for one stock):
# ---------------------------------------------------------------------------
# measurement of code execution time (Start):
PS_iplot_timeStart = time.perf_counter()

# setting up offline download of stock data from .csv:
data = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")
print("Data from server for ticker:", ticker)
print(data)

# setting up graph:
chart = go.Figure(go.Candlestick(x=data.index,
                                 open=data["AAPL.Open"],
                                 high=data["AAPL.High"],
                                 low=data["AAPL.Low"],
                                 close=data["AAPL.Close"],
                                 name="Prize chart"))

chart.update_layout(title=ticker + " share price",
                    yaxis_title="Stock Price (USD)")

chart.show()


# measurement of code execution time (End):
PS_iplot_timeEnd = time.perf_counter()

# measure code time:
PS_iplot_timeInterval = PS_iplot_timeEnd - PS_iplot_timeStart
print("\nElapsed time for iplot code:", PS_iplot_timeInterval, "second")
# Elapsed time for iplot code: 0.3377652000053786 second


# 3rd way (with pyplot, change of datetime format and simple graph):
# ------------------------------------------------------------------
# measurement of code execution time (Start):
PS_pyplot_timeStart = time.perf_counter()

# setting up download of Apple stock data for desired duration:
df = yf.download('AAPL', start='2017-01-01', end='2022-12-31')
df.index = pd.to_datetime(df.index, format='%Y-%m-%d %I-%p')
# changing datetime format
df

# df.head(10) # printing first 10 rows

# setting up graph:
plt.figure(figsize=(15, 5))
plt.title('Apple Stock Prizes for 5 years')
plt.xlabel('Year')
plt.ylabel('Price')

plt.plot(df['Close'])


# measurement of code execution time (End):
PS_pyplot_timeEnd = time.perf_counter()

# measure code time:
PS_pyplot_timeInterval = PS_pyplot_timeEnd - PS_pyplot_timeStart
print("\nElapsed time for pyplot code:", PS_pyplot_timeInterval, "second")
# Elapsed time for pyplot code: 0.031863999989582226 second


# 4th way (with pyplot, change of datetime format and simple graph):
# -------------------------------------------------------------------
# measurement of code execution time (Start):
PS_multi_pyplot_timeStart = time.perf_counter()

# setting up download of Apple stock data for desired duration:
df = yf.download(['AAPL', 'TSLA'], start='2017-01-01', end='2022-12-31')

df.index = pd.to_datetime(df.index, format='%Y-%m-%d %I-%p')
# changing datetime format
df

# df.head(10) # printing first 10 rows

# type(df.index[0]) # pandas._libs.tslibs.timestamps.Timestamp


# setting up graph:
plt.figure(figsize=(15, 5))
plt.title('Apple Stock Prizes for 5 years')
plt.xlabel('Year')
plt.ylabel('Price')

plt.plot(df['Close'])


# measurement of code execution time (End):
PS_multi_pyplot_timeEnd = time.perf_counter()

# measure code time:
PS_multi_pyplot_timeInterval = PS_multi_pyplot_timeEnd - PS_multi_pyplot_timeStart
print("\nElapsed time for multi_pyplot code:",
      PS_multi_pyplot_timeInterval, "second")
# Elapsed time for multi_pyplot code: 0.043490299984114245 second


# 5th way (OFFLINE with plotly, because for almost 6 years plotly is broken,
# with interactive chart for multi stock):
# ---------------------------------------------------------------------------
# measurement of code execution time (Start):
PS_multi_iplot_timeStart = time.perf_counter()

# setting up offline download of stock data from .csv:
data = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")
data2 = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")

print("Data from server for ticker:", ticker)
print(data)

# setting up graph:
chart = go.Figure(go.Candlestick(x=data.index,
                                 open=data["AAPL.Open"],
                                 high=data["AAPL.High"],
                                 low=data["AAPL.Low"],
                                 close=data["AAPL.Close"],
                                 name="Prize chart"))

chart.update_layout(title=ticker + " share price",
                    yaxis_title="Stock Price (USD)")

chart.show()


# measurement of code execution time (End):
PS_multi_iplot_timeEnd = time.perf_counter()

# measure code time:
PS_multi_iplot_timeInterval = PS_multi_iplot_timeEnd - PS_multi_iplot_timeStart
print("\nElapsed time for multi_iplot code:",
      PS_multi_iplot_timeInterval, "second")
# Elapsed time for multi_iplot code: 0.3377652000053786 second
