#stcok value scraper

import matplotlib.pyplot as plt
import urllib

base_url = "http://ichart.finance.yahoo.com/table.csv?s="


def make_url(ticker_symbol):
    return base_url + ticker_symbol

def write_historical_data(ticker_symbol):
    
    filename =  ticker_symbol + ".csv"
    try:
        urllib.urlretrieve(make_url(ticker_symbol),filename)
    except urllib.ContentTooShortError as e:
        outfile = open(filename, "w")
        outfile.write(e.content)
        outfile.close()
    


def getTickersFromSP(qty=500):
    tickerList = []
    openedFile = open('tickers.txt', 'rU')
    openedFile.next()
    for row in openedFile:
        tickerList.append(row.rstrip())      
    return tickerList[:qty]

def getMyTickers():
    tickerList = []
    openedFile = open('mystock.txt', 'rU')
    for row in openedFile:
        tickerList.append(row.rstrip())      
    return tickerList


# read tickers, get list



tickList = getTickersFromSP(qty=10)
myTickList = getMyTickers()

print myTickList
for ticker in myTickList:
 print 'Pulling data for', ticker
 write_historical_data(ticker)

 
'''
 Writing Format: Date,Open,High,Low,Close,Volume,Adj Close

#for ticker in tickList:
# write_historical_data(ticker)
 
  
plotCsco = []  
#for ticker in tickList:
openedFile = open('CSCO.csv', 'rU')
next(openedFile) #skip header
for row in openedFile:
    splitUp = row.split(',')
    closePr = splitUp[6].rstrip()
    plotCsco.append(closePr)


samples = len(plotCsco)
plt.plot(range(samples), plotCsco[::-1])
plt.show()

    '''

   
