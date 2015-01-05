import json
import csv
import urllib
from pprint import pprint
import sys 
OUTPUT_FILE = "T1_13H5-Nexus5chrome.csv"
INPUT_FILE = "www.spiegel.de.140212_T1_13H5-Nexus5chrome.HAR"




def writeFile(urls,statuses,bodySizes,cacheControls,expires,cacheTimes):
	with open(OUTPUT_FILE, 'wb') as csvfile:
		writer= csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL) 
		writer.writerow(['url','status','bodySize', 'cacheControl', 'expires', 'cacheTimes'])
		print urls[7]
		print statuses[7]
		print bodySizes[7]
		print cacheControls[7]
		print expires[7]
		print cacheTimes[7]
		for x in range(len(bodySizes)):
			writer.writerow([str(urls[x]).replace(',',''),str(statuses[x]),str(bodySizes[x]).replace(',',''),str(cacheControls[x]).replace(',',''),str(expires[x]).replace(',',''),str(cacheTimes[x])])
	print "Done writing CSV."
	
def startReading():
	har_data = open(INPUT_FILE, 'rb').read()
	har = json.loads(har_data)
	expAges = []
	urls = []
	bodySizes = []
	cacheControls = []
	expires = []
	cacheTimes = []
	statuses = []
	
	for x in har["log"]["entries"]:
		cc_found = 0
		exp_found = 0
		lst = x['response']['headers'] #List with header information
		
		#Check header information first
		for n in lst:
			if n['name'] == 'Cache-Control': 
				cacheControls.append(str(n['value']).replace('\n',''))
				cc_found = 1
			elif n['name'] == 'Expires':
				expires.append(n['value'])
				exp_found = 1
		
		#If not in header search response
		if cc_found != 1:
			try:
				if len(str(x['_cacheControl'])) > 0:
					cacheControls.append(str(x['_cacheControl']).replace('\n',''))
				else:
					cacheControls.append("NONE")
			except:
				cacheControls.append('NONE')
				
		if exp_found != 1:
			try:
				if len(str(x['_expires'])) > 0:
					expires.append(x['_expires'])
				else:
					expires.append('NONE')
			except:
				expires.append('NONE')	
		try:
			if len(str(x["response"]["bodySize"])) > 0:
				bodySizes.append(x["response"]["bodySize"])
			else:
				bodySizes.append("NONE")
		except:
			bodySizes.append('NONE')
				
		try:
			if len(str(x['_cache_time'])) > 0:
				cacheTimes.append(x['_cache_time'])
			else:
				cacheTimes.append('NONE')
		except:
			cacheTimes.append('NONE')
			
		try:
			if len(str(x['response']['status'])) > 0:
				statuses.append(x['response']['status'])
			else:
				statuses.append('NONE')
		except:
			statuses.append('NONE')
			
		try:
			if len(str(x["request"]["url"])) > 0:
				urls.append(x["request"]["url"].replace('\n',''))
			else:
				urls.append('NONE')
		except:
			urls.append('NONE')

	writeFile(urls,statuses,bodySizes,cacheControls,expires,cacheTimes)
if __name__ == "__main__":
	startReading()
	
	
	