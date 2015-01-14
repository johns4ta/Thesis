import csv
import sqlite3 as lite
import sys
from collections import defaultdict
import collections
import numpy

#Input/Output sources
OUTPUT_FILE = "mobile_total_bytes_over_time.csv"
DATABASE = "Oct_15_2013.db" #Database tables are located in.
PARSED_TABLE = "requestsmobile" #Table created when columns are stripped from original table.	
	
def startReading():
	propBytes = 1.0
	bytesSoFar = 0
	with open(OUTPUT_FILE, 'wb') as csvfile:
		writer= csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL) 
		con = lite.connect(DATABASE)
		with con:
			cur = con.cursor()
			#Pull expAges and respSizes
			cur.execute("SELECT expAge,respSize FROM " + PARSED_TABLE + " where expAge <= 604800;")
			info = cur.fetchall()
			expAges = [float(i[0]) for i in info]
			respSizes = [float(i[1]) for i in info]
			#sorted_info = sorted(info, key=getKey) #Sort order of tuples based on expAge (first element in tuple)
			
			d = dict()
			totBytes = numpy.sum(respSizes)
			for indx,expAge in enumerate(expAges):
				if expAge in d:
					d[expAge] += respSizes[indx] #Add respSize to dictionary, key already exists
				else:
					d[expAge] = respSizes[indx] #Create new key, set initial respSize
					
			od = collections.OrderedDict(sorted(d.items())) #Sort dictionary based on key (expAge)
			
			for expAge,sumRespSize in od.iteritems():
				writer.writerow([expAge,1.0 - propBytes]) #Outputs expAge and proportion of bytes still left in cache
				bytesSoFar += sumRespSize
				propBytes = float(bytesSoFar)/float(totBytes)
			writer.writerow([expAge+1,0]) # 1 second after last expDate bytes will be 0	
	print "Done writing CSV."
	
if __name__ == "__main__":
	startReading()