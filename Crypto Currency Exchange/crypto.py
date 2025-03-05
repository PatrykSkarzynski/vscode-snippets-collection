"""
Using 'PS' in front of variables

List of functions:
 - getCoinsList
 - findCoinBySymbol
 - getCoinLastMarketData
 - getCoinPriceInCurrency

Get some information using for example:
----------------------------------------
help(getCoinPriceInCurrency)
print(help(getCoinPriceInCurrency).__doc__)

Documentation from coingecko website:
https://docs.coingecko.com/reference/introduction

"""
from requests import get
from time import perf_counter

# base currency
PScurrency = "pln"
PScoinsList = None

# measurement of code execution time (Start):
PStimeStart = perf_counter()


def getCoinsList():
    """
    'getCoinsList' is a function that downloads list of crypto coins currencies
     |
     | response: crypto coin format <dict>:
     | ---------------------------------------
     | [ {'id': '01coin', 'symbol': 'zoc',
     | 'name': '01coin', 'platforms': {}}, ... ]
     |
    """
    global PScoinsList
    PSresponse = get("https://api.coingecko.com/api/v3/coins/list?include_platform=true")
    if PSresponse.ok is True:
        # printing information about response from the server if ok is True
        print("Server Response: OK")
        # when the server response  is ok, then show data in JSON
        PSCoinData = PSresponse.json()

        print("\n", PSCoinData[0])
        print("\nAmount of crypto currencies: " + str(len(PSCoinData)))
        PScoinsList = PSCoinData


def findCoinBySymbol(symbol):
    """
    'findCoinBySymbol' function that returns coins
     by provided 'symbol' if they're the same
     |
     | Makes sure that symbol of crypto coin is made with low characters
     | and there's no white characters
     |
    """
    symbol = symbol.lower().strip()
    for PScoin in PScoinsList:
        if PScoin["symbol"] == symbol:
            return PScoin
    else:
        return None


def getCoinLastMarketData(coinId):
    """
    'getCoinLastMarketData' function that downloads list of market data
     for crypto based on 'coinId'
     |
     | Crypto market data coin format <dict>:
     | ------------------------------------------
     | {'bitcoin': {'pln': 196445, 'pln_market_cap': 3673378580174.0874,
     |              'pln_24h_vol': 174245706368.16504,
     |              'pln_24h_change': 5.183517675973496,
     |              'last_updated_at': 1615110843}}
     |
     | When response from the server is ok, then shows that data in JSON format
     |
    """
    PSresponse = get("https://api.coingecko.com/api/v3/simple/price?ids="+coinId+"&vs_currencies="+PScurrency+"&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true")
    if PSresponse.ok:
        PSdata = PSresponse.json()
        return PSdata
    else:
        return None


def getCoinPriceInCurrency(coinId, PScurrency):
    """
    'getCoinPriceInCurrency' function that downloads coins price in
     earlier determined currency based on 'coinId' and
     base currency ('PScurrency')
     |
     | Makes sure that symbol of currency is made with low characters
     | and that there's no white characters
     |
    """
    PScurrency = PScurrency.lower().strip()
    # appealing by 'coinId' and base currency
    PSmarketData = getCoinLastMarketData(coinId)
    return PSmarketData[coinId][PScurrency]


getCoinsList()

# test if data for 'coinId'('btc') is downloaded correctly by appealing to 'id'
PSbtcData = findCoinBySymbol("btc")
print("\n", PSbtcData)

# test if data for 'coinId' from last test is downloaded correctly
# by appealing to 'id' with 'coinId'
PSmarketData = getCoinLastMarketData(PSbtcData["id"])
print("\n", "marketData: ", PSmarketData)

# test if data for 'coinId' from last tests is downloaded correctly
# by appealing to 'id' with 'coinId' and base currency, also show elapsed time
PScoinPrice = getCoinPriceInCurrency(PSbtcData["id"], PScurrency)
print("\nCoin price in " + PScurrency, PScoinPrice)


# measurement of code execution time (End):
PStimeEnd = perf_counter()
# measure code time:
PStimeInterval = PStimeEnd - PStimeStart
print("\nElapsed time:", PStimeInterval, "second")


# start of the program if everything went ok
print("\nWelcome to crypto currencies list!")

while True:
    # if that's true, then ask user to put symbol of crypto
    PScryptoSymbolToBuy = input("\nChoose symbol of crypto currencies to buy for example: btc or type \'exit\' to end: ")
    # allow user to exit the program, if he does so, then break the program
    if PScryptoSymbolToBuy == "exit":
        break

    # comparing data with the function that checks coins
    # by provided symbol if they are the same
    # by appealing with user provided symbol
    PScoinData = findCoinBySymbol(PScryptoSymbolToBuy)

    # inform user that there's no such crypto currency,
    # if he picks some that doesn't equal to any from the server
    if PScoinPrice is None:
        print("\nThere's no such crypto currency")
        continue

    # downloading coin price by appealing with 'coinId' and base currency
    PScoinPrice = getCoinPriceInCurrency(PScoinData["id"], PScurrency)
    print("\nPrice " + str(PScoinData["id"]),  PScoinPrice, PScurrency)

    # ask user how much he would like to spend and
    # get information about how much he can get with his money
    # (total amount of money divided by coin price)
    PSmoneyToBuyCrypto = float(input("\nHow much would You like to spend: "))
    PSboughtCrypto = PSmoneyToBuyCrypto / PScoinPrice

    # inform user how much he just bought
    print("\nCongratulations! You just bought " + str(PSboughtCrypto) + " " + PScryptoSymbolToBuy)
