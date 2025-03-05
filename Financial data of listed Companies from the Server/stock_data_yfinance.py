"""
Extra code that can be used (TEST LATER):
==========================================

setting up user input for stock ticker:
----------------------------------------
ticker = "TSLA"
userTicker = input("Write ticker name:").lower().strip()
if userTicker:
    ticker = userTicker

setting up download of stock DataFrame based on user input and
setting up printing user input ticker DataFrame:
---------------------------------------------------------------
df = yf.download(ticker, start = '2017-01-01', end = '2022-12-31')
df.index = pd.to_datetime(df.index, format = '%Y-%m-%d %I-%p')
# changing datetime format
df

print("DataFrame from server for ticker:", ticker)
print(df)

"""

from yfinance import download
from plotly.graph_objects import Figure, Candlestick
from time import localtime, strftime
from traceback import print_exc, format_exc
# from datetime import time


timeStrStart = '2017-01-01'
ticker = 'AAPL'


def yf_stockData():
    timeData = localtime()
    timeStrEnd = strftime("%Y-%m-%d", timeData)
    # print(timeStrEnd) # Example result: 2025-01-07
    '''
    strftime() formats date and time:
    ----------------------------------
    %Y - years,
    %m - months,
    %d - days,
    %H - hours,
    %M - minutes,
    %S - seconds

    '''
    # setting up download of Apple stock data for desired duration:
    # --------------------------------------------------------------
    df = download(ticker, start=timeStrStart, end=timeStrEnd)
    # list of every ticker available for yfinance is in "yf_allTickers.yml"
    '''
    | remove the Ticker column multi-index, Pandas will use MultiIndexing if you put data downloaded from yahoo finance into a dataframe,
    | which will cause 'plotly.graph_objects.Figure(plotly.graph_objects.Candlestick())' graph to not show any candle
    |
    |
    | df.head(10) # printing first 10 rows
    |
    | type(df.index[0]) # pandas._libs.tslibs.timestamps.Timestamp
    |
    '''
    # removing ticker multi-index column:
    # ------------------------------------
    df.columns = df.columns.droplevel(1)
    print("\n", "Data from server for ticker:", ticker, "\n")
    # printing information for which ticker data stock was downloaded
    """
    converting dataframe to CSV:
    -----------------------------
    stockData_CSV = df.to_csv(ticker + '_stock_data.csv',
    encoding='utf-8', index=False)
    print("\n", "DataFrame from server saved to .csv for:", ticker, "\n")
    # DataFrame from server saved to .csv for: TSLA


    converting dataframe to JSON:
    ------------------------------
    stockData_JSON = df.to_json(ticker + '_stock_data.json', indent=4)
    print(" DataFrame from server saved to .json for:", ticker, "\n")
    # DataFrame from server saved to .json for: TSLA

    print("\n", df)

    """
    # setting up more advanced chart:
    # --------------------------------
    try:
        chart = Figure(Candlestick(x=df.index,
                                   open=df["Open"],
                                   high=df["High"],
                                   low=df["Low"],
                                   close=df["Close"],
                                   name="Prize chart"))

        chart.update_layout(title=ticker + " share price",
                            yaxis_title="Stock Price (USD)")

        chart.show()

    except UnicodeError:
        print_exc()  # prints to stdout
        my_traceback = format_exc()  # returns a str
        print(my_traceback)


# yf_stockData() # Run function to get yFinance data
