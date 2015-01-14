import os
import sys
import numpy
import csv
import scipy
from scipy import stats
import sqlite3 as lite

FILES_PATH = '/home/johns4ta/596_Project/data/'
OUTPUT_FILE = '/home/johns4ta/596_Project/graphing_info_596.csv'
DATABASE = "/home/johns4ta/httparchive_20131015.sq3"
MOBILE_TABLE = "pagesmobile"

time_intervals = []
totBytes_proportions = [[] for x in xrange(0,169)]
totRequests_proportions = [[] for x in xrange(0,169)]
totBytes_averages = [[] for x in xrange(0,169)]
totRequests_averages = [[] for x in xrange(0,169)]
totBytes_final_averages = []
totRequests_final_averages = []
totBytes_final_std_dev = []
totBytes_final_upper_CI = []
totBytes_final_lower_CI = []
totRequests_final_std_dev = []
totRequests_final_upper_CI = []
totRequests_final_lower_CI = []

def get_totals(con, cur, pageid):
	#Pull columns wanted from requests and put into prequests table
	query = "SELECT reqTotal,bytesTotal FROM  " + MOBILE_TABLE + " where pageid = " + str(pageid) + ";"
	cur.execute(query)
	return cur.fetchall()
	
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
	for x in range(0,608400,3600):
		time_intervals.append(x)
	
def parse_data(data,con,cur):
	page_info = get_totals(con,cur,data[0])
	req_total = page_info[0][0]
	bytes_total = page_info[0][1]
	for x in range(len(time_intervals)):
		#Add data to corresponding time_interval in the list
		if int(data[1]) <  time_intervals[x]:
			if int(bytes_total) == 0 or int(req_total) == 0:
				totBytes_proportions[x].append(1)
				totRequests_proportions[x].append(1)
			else:
				totBytes_proportions[x].append(float(data[2])/float(bytes_total))
				totRequests_proportions[x].append(float(data[3])/float(req_total))
			break;
	
def get_final_averages():
	global totBytes_final_averages
	global totRequests_final_averages
	global totBytes_averages
	global totRequests_averages
	global time_intervals
	global totBytes_final_std_dev
	global totBytes_final_upper_CI
	global totBytes_final_lower_CI
	global totRequests_final_std_dev
	global totRequests_final_upper_CI
	global totRequests_final_lower_CI
	
	for list in totBytes_averages:
		print list
		totBytes_final_averages.append(numpy.mean(list))
		totBytes_final_std_dev.append(numpy.std(list))
		CI_info = mean_confidence_interval(list)
		totBytes_final_upper_CI.append(CI_info[2])
		totBytes_final_lower_CI.append(CI_info[1])
		
	for list in totRequests_averages:
		totRequests_final_averages.append(numpy.mean(list))
		totRequests_final_std_dev.append(numpy.std(list))
		CI_info = mean_confidence_interval(list)
		totRequests_final_upper_CI.append(CI_info[2])
		totRequests_final_lower_CI.append(CI_info[1])
		
	with open(OUTPUT_FILE, 'wb') as csvfile:
		writer = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
		writer.writerow(['Time', 'Total Bytes at this time','Total requests at this time','Bytes Std. Dev', 'Req. Std. Dev','Bytes Upper CI', 'Byters Lower CI', 'Reqs Upper CI', 'Reqs Lower CI'])
		for x in range(len(totBytes_final_averages)):
			writer.writerow([time_intervals[x],totBytes_final_averages[x],totRequests_final_averages[x],totBytes_final_std_dev[x],totRequests_final_std_dev[x],totBytes_final_upper_CI[x],totBytes_final_lower_CI[x],totRequests_final_upper_CI[x],totRequests_final_lower_CI[x]])

def get_averages():
	global totBytes_proportions
	global totRequests_proportions
	global totBytes_averages
	global totRequests_averages
	
	sum_bytes = 0
	sum_requests = 0
	
	for x in range(len(totBytes_proportions)):
		if len(totBytes_proportions[x]) > 0 :
			totBytes_averages[x].append(numpy.mean(totBytes_proportions[x]))

		if len(totRequests_proportions[x]) > 0:
			totRequests_averages[x].append(numpy.mean(totRequests_proportions[x]))

	#Clear Lists			
	totBytes_proportions = [[] for x in xrange(0,169)]
	totRequests_proportions = [[] for x in xrange(0,169)]
	
def getFileNames():
	return os.listdir(FILES_PATH)
	
def startAnalyzing():
	x = 0;
	initLists()
	fileNames = getFileNames()
	
	con = lite.connect(DATABASE)
	with con:
		cur = con.cursor()
		for file in fileNames:
			print file
			with open(FILES_PATH + file) as f:
				line_separated_data = f.readlines()
				#File Format: pageid,time,bytesfrompage,requestsfrompage,totalbytes,totalrequests
				for line in line_separated_data[1:]: #Ignore first line of text file, contains desc of format for file
					data = line.split(',')
					parse_data(data,con,cur)
			get_averages()
		get_final_averages()

if __name__ == "__main__":
	startAnalyzing()
	print "Done Analyzing"