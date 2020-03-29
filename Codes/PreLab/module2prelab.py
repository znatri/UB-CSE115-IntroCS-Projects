import csv

def quantities_owned(tradefilename):
    # csv header: buy_or_sell,quantity,ticker,date
    # returns a dictionary with no. of stocks owned
    # eg: {'AAPL': 2600, 'XOM':1000}
    retVal = {}
    with open(tradefilename, 'r') as f:
        reader = csv.reader(f)
        for record in reader:
            ticker = record[2]
            quantity = int(record[1])
            if ticker not in retVal:
                retVal[ticker] = quantity
            else:
                if record[0] == 'buy':
                    retVal[ticker] += quantity
                elif record[0] == 'sell':
                    retVal[ticker] -= quantity
    return retVal

# print(quantities_owned('tradefile.csv'))

def read_prices(tickerList):
    retVal = {}
    for eachTicker in tickerList:
        filename = eachTicker + ".csv" # header: date,price,volume
        with open(filename, 'r') as f:
            rates = {}
            reader = csv.reader(f)
            for record in reader:
                dateKey = record[0]
                price = float(record[1])
                rates[dateKey] = price
            retVal[eachTicker] = rates
    return retVal

def portfolio_value(filename):
    totalVal = 0
    stocksOwned = quantities_owned(filename) # get total stocks owned as key-value pair (ticker: quantity)
    tickerList = [] 
    for key in stocksOwned.keys(): # get all the tickers and append them to a list
        tickerList.append(key)
    stockPrices = read_prices(tickerList)
    for ticker, priceRecord in stockPrices.items(): # find cost for each ticker on date# and calculate the totalamount by multiplying with quantity. Add the totalamount to portfolio value. 
        quantity = stocksOwned.get(ticker) #no. of particular stock owner
        stockPrice = priceRecord.get("2015-12-31") # price of one stock
        amount = quantity * stockPrice # total amount of stock owned
        totalVal += amount # adding amount to portfolio value
    return totalVal
