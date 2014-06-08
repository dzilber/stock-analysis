#create data structures
import csv
	

class StockDataCollector:
	def __init__(self, ticker):
		self.ticker = str(ticker) #ticker name, MMM, AMZN, etc		
    	# Date,Open,High,Low,Close,Volume,Adj Close
		volume = {}
		adjclose = {}
		# add others as needed
		fileName = str(ticker)+'.csv'
		print fileName
		openFile = open(fileName,'rU')
		tickReader = csv.reader(openFile)
		# # fileReader.next()
    	for row in tickReader:
    		d,o,h,l,c,v,ac = row
    		print d
    		print v
    		volume[d] = v
    		adjclose[d] = ac
    	self.volume = volume
    	self.adjclose = adjclose
