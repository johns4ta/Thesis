import sqlite3 as lite
import sys
import numpy as np

DATABASE = "/storage/httparchive/httparchive_convert/October_15_2013.db"
OUTPUT = 'total_respSizes_per_page.txt'
INPUT_FILE = "pageids.txt"

pageids = [] 
def readPageIds():
	global pageids
	
	with open(INPUT_FILE) as f:
		pageids_not_cleaned = f.readlines()
		for id in pageids_not_cleaned:
			id_cleaned = id.rstrip()
			if(id_cleaned != None):
				pageids.append(id_cleaned)	
				
def fetchExpAges():
	x = 0
	con = lite.connect(DATABASE)
	with con:
		f = open(OUTPUT, 'w')
		
		for id in pageids:
			x = x + 1
			cur = con.cursor()
			#cur.execute("Select respSize from requestsmobile where pageid = " + id + " and respSize > 0;")
			cur.execute("Select respSize from requestsmobile where pageid = " + id + ";")
			data = cur.fetchall()
			items = [i[0] for i in data]
			sum = np.sum(items)
			f.write(str(sum) + "\n")
			print str(x) + " is done"
		f.close()


def main():	
	readPageIds()
	fetchExpAges()
	print "Done writing to respSizes_per_page.txt"
if __name__ == "__main__":
    main()
	
	