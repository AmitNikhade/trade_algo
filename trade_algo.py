# from twisted.internet import task, reactor
from nsetools import Nse
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import db
import time
# from time import gmtime, strftime
# curr_date_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())

# cred = credentials.Certificate("firebase-sdk.json")

# firebase_admin.initialize_app(cred, {
# 	'databaseURL': 'https://algoguru-d89af-default-rtdb.firebaseio.com/'
# })

# ref = db.reference('/')

def getDataFromNse():
    
    nse = Nse()
    data = nse.get_quote('sbin')

    currDate = data['secDate']
    openPrice = data['open']
    dayLow = data['dayLow']
    dayHigh = data['dayHigh']
    ttv = data['totalTradedVolume']
    lastPrice = data['lastPrice']
    
    return {
        'currDate': currDate,
        'openPrice': openPrice,
        'dayLow': dayLow,
        'dayHigh': dayHigh,
        'lastPrice': lastPrice,
        'ttv': ttv
    }

def doWork():
    
    data_type = "SBIN"
    data = {
    	data_type: getDataFromNse()
    }
    print(data)
    # ref.set(data)

if __name__ == '__main__':

	timeout = 5.0
	while True:
		time.sleep(timeout)
		doWork()
		print("[INFO] Data Fetched!")