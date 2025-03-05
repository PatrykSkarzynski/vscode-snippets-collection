import plotly.graph_objects as go
import pandas as pd


ticker = "TSLA"
userTicker = input("Write ticker name:").lower().strip()

if userTicker:
    ticker = userTicker
    data = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")
    print("Data from server for ticker:", ticker)
    print(data)

    chart = go.Figure(go.Candlestick(x=data.index,
                                     open=data["AAPL.Open"],
                                     high=data["AAPL.High"],
                                     low=data["AAPL.Low"],
                                     close=data["AAPL.Close"],
                                     name="Prize chart"))

    chart.update_layout(title=ticker + " share price",
                        yaxis_title="Stock Price (USD)")

    chart.show()
