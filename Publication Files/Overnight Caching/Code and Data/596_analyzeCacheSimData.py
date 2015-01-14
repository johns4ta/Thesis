import os
import sys
import numpy
from scipy import stats

FILES_PATH = '/home/johns4ta/596_Project/data/'

def calcStats(total_bytes,total_requests):
	average_bytes = numpy.mean(total_bytes)
	average_requests = numpy.mean(total_requests)
	
	stddev_bytes = numpy.std(total_bytes)
	stdev_requests = numpy.std(total_requests)
	
	ci_bytes = stats.norm.interval(0.95,loc=average_bytes,scale=stddev_bytes)
	ci_requests = stats.norm.interval(0.95,loc=average_requests,scale=stdev_requests)

	with open('results.txt', 'w+') as outputfile:
		outputfile.write('Average Bytes: ' + str(average_bytes) + '\n')
		outputfile.write('Average Requests: ' + str(average_requests) + '\n')
		outputfile.write('Standard Dev. Bytes: ' + str(stddev_bytes) + '\n')
		outputfile.write('Standard Dev. Requests: ' + str(stdev_requests) + '\n')
		outputfile.write('95% CI Bytes: ' + str(ci_bytes[0]) + ',' + str(ci_bytes[1]) + '\n')
		outputfile.write('95% CI Requests: ' + str(ci_requests[0]) + ',' + str(ci_requests[1]) + '\n')
	sys.exit(0)
	
def getFileNames():
	return os.listdir(FILES_PATH)
	
def startAnalyzing():
	total_bytes = []
	total_requests = []
	
	fileNames = getFileNames()
	for file in fileNames:
		print file
		with open(FILES_PATH + file) as f:
			line_separated_data = f.readlines()
			last_line_of_data = line_separated_data[-1].split(',')
			total_bytes.append(int(last_line_of_data[4].rstrip()))
			total_requests.append(int(last_line_of_data[5].rstrip()))
	calcStats(total_bytes,total_requests)

			#for line in line_separated_data[1:]: #Ignore first line of text file, contains desc of format for file
				#File Format: pageid,time,bytesfrompage,requestsfrompage,totalbytes,totalrequests
					
if __name__ == "__main__":
	startAnalyzing()
	print "Done Analyzing"