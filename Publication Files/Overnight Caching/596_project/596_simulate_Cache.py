import numpy as np
import csv
import sys
import math
import random 
import bisect 
import math
from itertools import islice

INPUT_FILE = 'resp_comparisons_edited.csv' #Edited version has columns sorted and rank listed as first column
END_TIME = 86400
NUM_ROWS = 4752
NUM_SIMS = 2000

class ZipfGenerator: 

    def __init__(self, n, alpha): 
        # Calculate Zeta values from 1 to n: 
        tmp = [1. / (math.pow(float(i), alpha)) for i in range(1, n+1)] 
        zeta = reduce(lambda sums, x: sums + [sums[-1] + x], tmp, [0]) 

        # Store the translation map: 
        self.distMap = [x / zeta[-1] for x in zeta] 
		
		
    def next(self):
        # Take a uniform 0-1 pseudo-random value: 
        u = random.random()  

        # Translate the Zipf variable: 
        return bisect.bisect(self.distMap, u) - 1

def getRow(reader, position):
	return list(islice(reader,position))[-1]
	
def getParetoValue():
	return math.trunc(np.random.pareto(1.5, 1)[0] + 30) #Conti paper lists shape as 1.5 and scale as 30

def generateFileName(num):
	return "./data/cacheSimData" + str(num) + ".txt"

def start(fileNumber):
	outputFile = generateFileName(fileNumber)
	sum_reqs = 0
	sum_bytes = 0
	time = 0

	zpf = ZipfGenerator(NUM_ROWS-1, 0.85) #Subtract 1 from rows to account for excel starting from 1
	
	with open(outputFile, 'w+') as output:
		output.write("File Format: pageid,time,mobile bytes from page not expired,mobile requests from page not expired,totalmobilebytes,totalmobilerequests\n")
		with open(INPUT_FILE, 'rb') as csvfile:
			reader = csv.reader(csvfile)
			while time < END_TIME:
				info = getRow(reader,zpf.next()+1) #Add 1 in case 0 is generated, avoids index error, csv file starts reading at 1.
				pageid = info[1]
				sumReqs_thisPage = 0
				sumBytes_thisPage = 0
			
				if len(info[7]) > 2: #Make sure there is data in matched fixed requests column otherwise no matching requests data
					expAges = info[10].split(';') #Split matched requests data into groups based on expAge
					for expAge in expAges:
						req_info = expAge.split(':') #Check each expAge group,check if expired, if not, accumulate information
						if len(req_info) > 1:
							if len(req_info) == 4:
								#First element of list empty string due to format of :expAge:numReqs:totBytes:
								if int(req_info[1]) > time: #Accumulate information if items haven't expired yet
									sumReqs_thisPage += int(req_info[2]) #Requests
									sumBytes_thisPage += int(req_info[3]) #Bytes
							else:
								print "Length Problem??????"
								print req_info
								sys.exit(0)
							
				csvfile.seek(0) #Return to start of file
				sum_reqs += sumReqs_thisPage
				sum_bytes += sumBytes_thisPage
				output.write(str(pageid) + "," + str(time) + "," + str(sumBytes_thisPage) + "," + str(sumReqs_thisPage) + "," + str(sum_bytes)+ "," + str(sum_reqs) + '\n')
				time += getParetoValue()
def startSim():
	cur_sim = 0
	
	while cur_sim < NUM_SIMS:
		start(cur_sim)
		print "File " + str(cur_sim) + " done."
		cur_sim += 1
		
if __name__ == "__main__":
	startSim()