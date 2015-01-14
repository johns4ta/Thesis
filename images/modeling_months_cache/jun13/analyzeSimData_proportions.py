import os
import sys
import csv
import numpy
import scipy
from scipy import stats
import collections
from collections import Counter
from collections import defaultdict
import math

FILES_PATH = '/home/johns4ta/Sim/June 15 2013 Sim/SimFiles2/'
OUTPUT_FILE = 'results.csv'


time_intervals = []
totBytes_proportions = [[] for x in xrange(0,169)]
totBytes_averages = [[] for x in xrange(0,169)]
totBytes_final_averages = []
totBytes_final_std_dev = []
totBytes_final_upper_CI = []
totBytes_final_lower_CI = []

d = defaultdict(list)

def getFileNames():
	return os.listdir(FILES_PATH)			

def mean_confidence_interval(data, confidence=0.95):
	if len(data) > 0:
		a = 1.0*numpy.array(data)
		n = len(a)
		m, se = numpy.mean(a), scipy.stats.sem(a)
		h = se * scipy.stats.t._ppf((1+confidence)/2., n-1)
		return m, m-h, m+h
	else:
		return 0,0,0
			
def startAnalyzing():
	fileNames = getFileNames()
	final_respSizes_proportions = defaultdict(list)

	for file in fileNames:
		byte_proportions = []
		expAges = []
		
		print file
		with open(FILES_PATH + file) as f:
			line_separated_data = f.readlines() #Separate into lines
			for line in line_separated_data: 
				request = line.split(',') #Request data separated by ,
				expAge = int(request[0].rstrip())
				respSize_proportion = float(request[1].rstrip())
				d[expAge].append(respSize_proportion)
			
	with open(OUTPUT_FILE, 'wb') as csvfile:
		writer= csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
		
		for expAge in d:
			CI_info = mean_confidence_interval(d[expAge])
			upper_ci = CI_info[2]
			lower_ci = CI_info[1]
		
			writer.writerow([str(expAge),str(numpy.mean(d[expAge])),str(upper_ci),str(lower_ci)])
		
if __name__ == "__main__":
	startAnalyzing()
	print "Done Analyzing"
	