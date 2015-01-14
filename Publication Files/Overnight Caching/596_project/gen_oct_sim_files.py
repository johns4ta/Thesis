import scipy as sp
import math
import numpy as np
import sys
import scipy.stats as ss
import random

zero_bin = 122004 # 0 bin
forty_three_thous_two_hundred_bin = zero_bin + 3607#43200 bin
range_bin_1 = forty_three_thous_two_hundred_bin + 2345 #Bin range 43200 < expAge < 86400
eighty_six_thous_four_hundred_bin = range_bin_1 + 14070 + 34770 #86400 bin
range_bin_2 = eighty_six_thous_four_hundred_bin + 774 #Bin range 86400 < expAge < 172800
one_hundred_seventy_two_thous_eight_hundred_bin = range_bin_2 + 1762#172800
range_bin_3 = one_hundred_seventy_two_thous_eight_hundred_bin + 496 #Bin range 172800 < expAge < 259200
two_hundred_fifty_nine_thousand_two_hundred_bin = range_bin_3 + 1492 #Bin 259200
range_bin_4 = two_hundred_fifty_nine_thousand_two_hundred_bin + 2770 #Bin range 259200 < expAge < 604800
six_hundred_four_thous_eight_hundred_bin = range_bin_4 + 15644 #604800 bin
fisk_bin = 38377

def generate_fisk_value():
	a = 0.88945
	b =  2600.7
	loc =1 
	y = ss.fisk.rvs(a,loc=loc,scale=b,size=1)[0]
	while y > 43200:
		y = ss.fisk.rvs(a,loc=loc,scale=b,size=1)[0]
	return y
		
	
def gen_numResponses():
	#Gamma distribution parameters
	k = 0.6167 #shape parameter
	alpha =  3.1119 #shape parameter
	beta =  8.2912 #scale
	loc = 0.17238 #loc
	
	#Generate number of responses on page and return it
	return int(math.ceil(ss.gengamma.rvs(alpha,k,loc = loc,scale=beta,size=1)[0]))

def gen_rand_val(min,max):
	return random.randint(min,max)
	
def gen_respSize():
	#Weibull distribution parameters.	
	a = 0.27 #shape
	scale = 700.0 #scale
	loc = 2.5
	#Generate one weibull value and return it
	return ss.weibull_min.rvs(a,scale=scale,loc=loc,size=1)[0]
	
def gen_rand_val(min,max):
	return random.randint(min,max)

def gen_zeros():
	num = np.random.normal(0.629075947,0.300892868)
	while num > 1 or num < 0:
		num = np.random.normal(0.629075947,0.300892868)
	return num
	
def generate_expAge(x):

	if x < zero_bin:
		return 0
	elif x < fisk_bin:
		return generate_fisk_value()
	elif x < forty_three_thous_two_hundred_bin:
		return 43200
	elif x <  range_bin_1:
		return gen_rand_val(43201,86400)		
	elif x < eighty_six_thous_four_hundred_bin:
		return 86400	
	elif x <  range_bin_2:
		return gen_rand_val(86401,172800)
	elif x < one_hundred_seventy_two_thous_eight_hundred_bin:
		return 172800
	elif x <  range_bin_3:
		return gen_rand_val(172801,259200)
	elif x <  two_hundred_fifty_nine_thousand_two_hundred_bin:
		return 259200
	elif x <  range_bin_4:
		return gen_rand_val(259201,604800)
	elif x < six_hundred_four_thous_eight_hundred_bin:
		return 604800
	else:
		return gen_rand_val(0,604801)
	
def gen_low_expAge():
	three_hundred = 530
	twelve_hundred = three_hundred + 400
	eighteen_hundred = twelve_hundred + 500
	thirty_six_hundred = eighteen_hundred + 600
	seventy_two_hundred = thirty_six_hundred + 300
	fourteen_four_hundred = seventy_two_hundred + 300
	twenty_one_six_hundred = fourteen_four_hundred + 100

	x = gen_rand_val(0,twenty_one_six_hundred + 3000)
	
	if x < three_hundred:
		return 300
	elif x < twelve_hundred:
		return 1200
	elif x < eighteen_hundred:
		return 1800
	elif x < thirty_six_hundred:
		return 3600
	elif x < seventy_two_hundred:
		return 7200
	elif x < fourteen_four_hundred:
		return 14400
	elif x <= twenty_one_six_hundred:
		return 21600
	else:
		return gen_rand_val(0,604800)
		
def gen_expAge_value():
	expAge = generate_expAge(gen_rand_val(0,199734))
	return expAge
	
def startSim():
	for pageNum in range(0,4776):
	
		numResp = gen_numResponses()
		
		expAges = []
		respSizes = []
			
		page_category = gen_rand_val(0,4776)
		
		if(page_category < 300): #200#633
			while numResp < 1:
				numResp = gen_numResponses()
					
			#Generate rest of zero value expAges
			for x in range(0,int(numResp)):
				expAges.append(0)
				respSizes.append(gen_respSize())
		elif(page_category < 1350):
			while numResp < 1:
				numResp = gen_numResponses()
					
			expAge = gen_low_expAge()
			#Generate rest of zero value expAges
			for x in range(0,int(numResp)):
				expAges.append(expAge)
				respSizes.append(gen_respSize())
		elif(page_category < 1650):
			while numResp < 1:
				numResp = gen_numResponses()
					
			expAge = generate_fisk_value()
			#Generate rest of zero value expAges
			for x in range(0,int(numResp)):
				expAges.append(expAge)
				respSizes.append(gen_respSize())		
		else:
			while numResp < 1:
				numResp = gen_numResponses()
		
			prop_expAge_zeros = gen_zeros()
			num_zero_expAges = math.ceil(prop_expAge_zeros * numResp)
			num_non_zero_expAges = numResp - num_zero_expAges #Number of expAges to be generated besides the zero values
		
			#Generate respSizes
			for x in range(0,numResp):
				respSizes.append(gen_respSize())
				
			#Generate zero value expAges
			for x in range(0,int(num_zero_expAges)):
				expAges.append(0)
			
			#Generate rest of zero value expAges
			for x in range(0,int(num_non_zero_expAges)):
				expAges.append(gen_expAge_value())
				respSizes.append(gen_respSize())
		
		#Write output in format that cache analyzer script will be able to read
		out_str = ""
		for expAge,respSize in zip(expAges,respSizes):
			out_str = out_str + str(expAge) + "," + str(respSize) + ";"
		
		cache_output.write(out_str)
		page_level_output.write(str(np.mean(expAges)) + "\n")
if __name__ == "__main__":
	startSim()