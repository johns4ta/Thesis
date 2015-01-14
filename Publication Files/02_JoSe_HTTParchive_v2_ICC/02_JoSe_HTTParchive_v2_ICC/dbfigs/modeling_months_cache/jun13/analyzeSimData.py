import os
import sys
import csv
import numpy
from scipy import stats
import collections
from collections import Counter
from collections import defaultdict
import math

FILES_PATH = '/home/johns4ta/Sim/June 15 2013 Sim/SimFiles/'
OUTPUT_FILE = '/home/johns4ta/Sim/June 15 2013 Sim/SimFiles2/'

import os
import sys
import numpy
import csv
import scipy
from scipy import stats
import sqlite3 as lite


time_intervals = []
totBytes_proportions = [[] for x in xrange(0,169)]
totBytes_averages = [[] for x in xrange(0,169)]
totBytes_final_averages = []
totBytes_final_std_dev = []
totBytes_final_upper_CI = []
totBytes_final_lower_CI = []

bytes_proportions = dict()

def getFileNames():
	return os.listdir(FILES_PATH)			
	
			
def startAnalyzing():
	fileNames = getFileNames()
	final_respSizes_proportions = defaultdict(list)
	
	for file in fileNames:
		respSizes = []
		expAges = []
		
		print file
		with open(FILES_PATH + file) as f:
			line_separated_data = f.readlines() #Separate into lines
			for line in line_separated_data: 
				# Each line = one page
				request = line.split(',') #Requests separated by ,
				expAges.append(int(request[0].rstrip()))
				respSizes.append(float(request[1].rstrip()))
			
			#sorted_info = sorted(info, key=getKey) #Sort order of tuples based on expAge (first element in tuple)
			d = dict()
			totBytes = numpy.sum(respSizes)
			
			propBytes = 1.0
			bytesSoFar = 0
			
			for indx,expAge in enumerate(expAges):
				if expAge in d:
					d[expAge] += respSizes[indx] #Add respSize to dictionary, key already exists
				else:
					d[expAge] = respSizes[indx] #Create new key, set initial respSize
					
			od = collections.OrderedDict(sorted(d.items())) #Sort dictionary based on key (expAge)
			
			with open(OUTPUT_FILE + file + ".csv", 'wb') as csvfile:
				writer= csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL) 
				for expAge,sumRespSize in od.iteritems():
					if expAge in final_respSizes_proportions:
						final_respSizes_proportions[expAge] += [indx] #Add respSize to dictionary, key already exists
					else:
						final_respSizes_proportions[expAge] = final_respSizes_proportions[indx] #Create new key, set initial respSize
					writer.writerow([expAge,propBytes]) #Outputs expAge and proportion of bytes still left in cache
					bytesSoFar += sumRespSize
					propBytes = float(bytesSoFar)/float(totBytes)

				writer.writerow([expAge+1,0]) # 1 second after last expDate bytes will be 0	
				
if __name__ == "__main__":
	startAnalyzing()
	print "Done Analyzing"
	