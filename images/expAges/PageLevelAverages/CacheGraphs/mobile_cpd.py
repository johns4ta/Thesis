
import csv
import sqlite3 as lite
import sys
from collections import defaultdict
from collections import Counter
import collections
import numpy

#Input/Output sources
OUTPUT_FILE = "mobile_cpd.csv"
DATABASE = "/storage/httparchive/httparchive_convert/October_15_2013.db" #Database tables are located in.
PARSED_TABLE = "requestsmobile" #Table created when columns are stripped from original table.
		
def startReading():
	cumu_prob = 0.0
	prob = 0.0
	with open(OUTPUT_FILE, 'wb') as csvfile:
		writer= csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL) 
		writer.writerow(['expAge','respSize'])
		con = lite.connect(DATABASE)
		with con:
			cur = con.cursor()
			#Pull expAges and respSizes
			cur.execute("SELECT expAge FROM " + PARSED_TABLE + " where expAge <= 604800;")
			expAges = cur.fetchall()
			expAges = [float(i[0]) for i in expAges]
			size = float(len(expAges))
			count_expAges = Counter(expAges) #Counter returns dictionary object
			ordered_count_expAges = collections.OrderedDict(sorted(count_expAges.items()))
			for expAge in ordered_count_expAges:
				prob = float(count_expAges[expAge] / size)
				cumu_prob += prob
				writer.writerow([expAge,cumu_prob])
	print "Done writing CSV."
if __name__ == "__main__":
	startReading()