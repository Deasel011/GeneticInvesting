from modules import runnable
import time

# To be at 9h30 eastern america, has to be 1493042400 + 86000 or x % 86000 = 82400
# To be at 16h eastern america, has to be x % 86000 = 18000

start = 1493042400
end = 1493064000
titles = ['ATVI','ADBE','AKAM','ALXN','GOOGL',
	'GOOG','AMZN','AAL','AMGN','ADI'
	'AAPL','AMAT','ADSK','ADP','BIDU']


def initPops(title_list):
    for title in title_list:
        runnable.initPopulation(title,start,end)

initPops(titles)
