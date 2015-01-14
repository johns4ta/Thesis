import random
import scipy.stats as ss
import scipy as sp
import scipy
import csv
import math
import numpy
import numpy as np
import sys

OUTPUT_FILE = 'page_level_results_total_respSizes.csv'

time_intervals = []
totRespSizes = [[] for x in xrange(0,101)]
totRespSizes_averages = [[] for x in xrange(0,101)]
totRespSizes_final_averages = []
totRespSizes_final_upper_CI = []
totRespSizes_final_lower_CI = []

def gen_numResponses():
	#Gamma distribution parameters
	k = 0.6167 #shape parameter
	alpha =  3.1119 #shape parameter
	beta =  8.2912 #scale
	loc = 0.17238 #loc
	
	return int(math.ceil(ss.gengamma.rvs(alpha,k,loc = loc,scale=beta,size=1)[0]))
	
def gen_respSize():
	#Weibull distribution parameters.	
	a = 0.27 #shape
	scale = 700.0 #scale
	loc = 2.5
	
	#Generate one weibull value and return it
	respSize = ss.weibull_min.rvs(a,scale=scale,loc=loc,size=1)[0]
	while respSize < 1:
		respSize = ss.weibull_min.rvs(a,scale=scale,loc=loc,size=1)[0]
	return respSize
		
def mean_confidence_interval(data, confidence=0.95):
	if len(data) > 0:
		a = 1.0*numpy.array(data)
		n = len(a)
		m, se = numpy.mean(a), scipy.stats.sem(a)
		h = se * scipy.stats.t._ppf((1+confidence)/2., n-1)
		return m, m-h, m+h
	else:
		return 0,0,0

def initLists():
	global time_intervals
	for x in range(0,5050000,50000):
		time_intervals.append(x)
	
def add_data(respSize):
	global totRespSizes
	global time_intervals
	
	for x in range(len(time_intervals)):
		#Add data to corresponding time_interval in the list
		if float(respSize) <=  time_intervals[x]:
			totRespSizes[x].append(1) #Add 1 to indicate 1 respSize falls within that category
			break
	
def get_final_averages():
	global totRespSizes_final_averages
	global totRespSizes_averages
	
	for list in totRespSizes_averages:
		totRespSizes_final_averages.append(numpy.mean(list))
		#totRespSizes_final_standard_devs.append(numpy.std(list))
		CI_info = mean_confidence_interval(list)
		totRespSizes_final_upper_CI.append(CI_info[2])
		totRespSizes_final_lower_CI.append(CI_info[1])
		
	with open(OUTPUT_FILE, 'wb') as csvfile:
		writer = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
		writer.writerow(['Time', 'Average Requests','Upper CI','Lower CI'])
		for x in range(len(totRespSizes_final_averages)):
			writer.writerow([time_intervals[x],totRespSizes_final_averages[x],totRespSizes_final_upper_CI[x],totRespSizes_final_lower_CI[x]])

def get_averages(num_pages):
	global totRespSizes
	global totRespSizes_averages
	
	for x in range(len(totRespSizes)):
		totRespSizes_averages[x].append(float(numpy.sum(totRespSizes[x]))/float(num_pages)) #Add sum of all 1's in list to get number of requests and calculate proportions
	#Clear Lists			
	totRespSizes = [[] for x in xrange(0,101)]

def start_simulation():
	for pageNum in range(0,4776):
		numResp = gen_numResponses()
		
		respSizes = []
		for x in range(0,numResp):
			respSizes.append(gen_respSize())
		add_data(numpy.sum(respSizes))
		
	
	
if __name__ == '__main__':
	initLists()
	for x in range(0,500):
		start_simulation()
		get_averages(4776)
		print "Page " + str(x) + " done."
	get_final_averages()