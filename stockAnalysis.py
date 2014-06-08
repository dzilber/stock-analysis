import numpy as np
import datetime
import csv
import matplotlib.pyplot as plt

def getMyTickers():
    tickerList = []
    stockFile = open('mystock.txt', 'rU')
    for row in stockFile:
        tickerList.append(row.rstrip())      
    return tickerList


myStk = getMyTickers()
dataSet = {} #stock, date, adjcl

beginDate = datetime.date(2000,06,01)

for t in myStk:
	fileOpen = open(str(t)+'.csv', 'rU')
	dataSet[t]=[]
	csvRd= csv.reader(fileOpen)
	csvRd.next()
	print 'reading',t
	for row in csvRd:
		d,o,h,l,c,v,ac = row
		y,m,dom  =  d.split('-')
		s=datetime.date(int(y),int(m),int(dom))
		if s>= beginDate:
			dataSet[t].append((s,float(v)))



dataSet['MMM'].sort()
date,pr = zip(*dataSet['MMM'])

print np.var(pr)
delta = [pr[i]-pr[i-1] for i in range(1,len(pr))]

plt.hist(delta)
plt.show()
plt.close()
plt.plot(date[1:],delta)
plt.show()
			


