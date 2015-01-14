import random
import scipy.stats as ss
import scipy as sp
import scipy
import math
import csv
import numpy
import numpy as np
import sys

OUTPUT_FILE = 'overall_results_respSizes_march_2014.csv'

time_intervals = []
totRespSizes = [[] for x in xrange(0,101)]
totRespSizes_averages = [[] for x in xrange(0,101)]
totRespSizes_final_averages = []
totRespSizes_final_upper_CI = []
totRespSizes_final_lower_CI = []
	
def gen_respSize():
	#Weibull distribution parameters.
	a = 0.5666
	#a = 0.57264
	#c =  0.50556451275314185
	#loc =  0
	#scale = 8887.5
	scale = 9200.66
	#Generate one weibull value and return it
	return ss.weibull_min.rvs(a,scale=scale,size=1)[0]
		
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
	for x in range(0,101000,1000):
		time_intervals.append(x)
	
def add_data(respSize):
	global totRespSizes
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
			#print len(totRespSizes_final_averages)
def get_averages(num_pages):
	global totRespSizes
	global totRespSizes_averages
	
	for x in range(len(totRespSizes)):
		totRespSizes_averages[x].append(float(numpy.sum(totRespSizes[x]))/float(num_pages)) #Add sum of all 1's in list to get number of requests and calculate proportions
	#Clear Lists			
	totRespSizes = [[] for x in xrange(0,101)]
		
def start():
	for y in range(199734):
		resp = gen_respSize()
		add_data(resp)
	
if __name__ == '__main__':
	initLists()
	for x in range(0,500):
		start()
		get_averages(199734)
		print str(x) + " done"
	get_final_averages()