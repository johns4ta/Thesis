import random
import scipy.stats as ss
import scipy as sp
import scipy
import math
import csv
import numpy
import numpy as np
import sys

import random
import scipy.stats as ss
import scipy as sp

OUTPUT_FILE = '/home/johns4ta/Sim/June 15 2013 Sim/SimFiles/'

zero_bin = 122004
three_hundred_bin = zero_bin + 2533
six_hundred_bin = three_hundred_bin + 2361
nine_hundred_bin = six_hundred_bin + 2125
thirty_six_hundred_bin = nine_hundred_bin + 8531
forty_three_thous_two_hund_bin = thirty_six_hundred_bin + 3607
eight_six_thous_four_hund_bin = forty_three_thous_two_hund_bin + 14070
six_hundred_four_thous_eight_hund = eight_six_thous_four_hund_bin + 15644
fourteen_thous_four_hund = six_hundred_four_thous_eight_hund + 1995
one_hundred_seventy_two_thous_eight_hund = fourteen_thous_four_hund + 1762
seventy_two_hund = one_hundred_seventy_two_thous_eight_hund + 1666
twenty_one_thous_six_hundred = seventy_two_hund + 1644

#Generate number between min and max
def gen_rand_val(min,max):
	return random.randint(min,max)
	
def generate_expAge(x):
	if x < zero_bin:
		return 0
	elif x < three_hundred_bin:
		return 300
	elif x < six_hundred_bin:
		return 600
	elif x < nine_hundred_bin:
		return 900
	elif x < thirty_six_hundred_bin:
		return 3600
	elif x < forty_three_thous_two_hund_bin:
		return 43200
	elif x < eight_six_thous_four_hund_bin:
		return 86400
	elif x < six_hundred_four_thous_eight_hund:
		return 604800
	elif x < fourteen_thous_four_hund:
		return 14400
	elif x < one_hundred_seventy_two_thous_eight_hund:
		return 172800
	elif x < seventy_two_hund:
		return 7200
	elif x < twenty_one_thous_six_hundred:
		return 21600
	else:
		expAges_ls = [0,300,600,900,3600,4800,43200,86400,604800,14400,172800,7200,21600]
		x = 0
		#Don't generate a popular expAge
		while x in expAges_ls:
			x = gen_rand_val(0,604800)
		return x

def gen_respSize():
	#Weibull distribution parameters.
	a = 0.5612
	scale = 7300.04
	
	#Generate one weibull value and return it
	return ss.weibull_min.rvs(a,scale=scale,size=1)[0]
		
def start(x):
	f = open(OUTPUT_FILE + "simFile" + str(x) + ".txt",'w')
	
	for y in range(0,199734):
		respSize = gen_respSize()
		expAge = generate_expAge(gen_rand_val(0,199734))
		f.write(str(expAge) + "," + str(respSize) + "\n")
	f.close()
	
if __name__ == '__main__':
	for x in range(0,1000):
		start(x)
		print str(x) + " done"