# in terminal: pip install yfinance

import tkinter as tk
import yfinance as yf


window = tk.Tk()
window.title("Stock info")

# Frame
topWidget = tk.Frame(window)
label = tk.Label(topWidget, text="Write stock ticker:")
label.pack(side=tk.LEFT)
entry = tk.Entry(topWidget)
entry.pack(side=tk.RIGHT)
topWidget.pack()

# Window_TextBox_Attributes
scrollbar = tk.Scrollbar(window)
textBox = tk.Text(window, height=15, width=90,
                  padx=5, pady=5, font="Helvetica 12")
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
textBox.pack(expand=True, fill=tk.BOTH)
scrollbar.config(command=textBox.yview)
textBox.config(yscrollcommand=scrollbar.set)


# Function_for_downloading_stock_data
def downloadData(e):    # e for event
    textBox.delete("1.0", tk.END)
    stock = str(e.widget.get())

    if not stock:
        print("No stock ticker!")
        return

    stock = stock.upper().strip()
    print("download stock data: ", stock)

    stockData = yf.Ticker(stock)
    print(stockData.info)

    textBox.insert(tk.END, "Ticker: " + stock + " \n\n")

    for key in stockData.info.keys():
        try:
            v = str(key) + ": " + stockData.info[str(key)] + " \n\n "
            textBox.insert(tk.END, v)
        except KeyError:
            pass

    history = stockData.history(period="1mo", interval="1d")
    # 1mo, 1m, 1d, 1y, 1wk
    textBox.insert(tk.END, history)


entry.bind("<Return>", downloadData)

window.mainloop()
