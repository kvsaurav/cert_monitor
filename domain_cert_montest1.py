#python 2.7
#certificate monitoring tool 
#enter the domain you want to monitor the certificate for and you are all set 

from crtsh import crtshAPI
import json
import requests
from pprint import pprint 
import hashlib
from termcolor import colored
from datetime import datetime
import datetime
import time 
import gtfe
import csv

from collections import defaultdict


columns = defaultdict(list) # each value in each column is appended to a list

with open('cywareoutout.csv') as f:
		reader = csv.DictReader(f) # read rows into a dictionary format
		for row in reader: # read a row as {column1: value1, column2: value2,...}
				for (k,v) in row.items(): # go over each column name and value 
						columns[k].append(v) # append the value into the appropriate list
																 # based on column name k

fuzzed_domain =columns['domain-name']
print fuzzed_domain



print "=="*50
print "**"*50

for item in fuzzed_domain:
	print item
	a = item
	# a = raw_input("ENTER THE NAME FOR THE DOMAIN TO BE SEARCHED : ")
	print colored('SEARCHING CERTIFICATES FOR ','red'),item
	jason_data=json.dumps(crtshAPI().search(a))
	jason_data=json.loads(jason_data)

	print jason_data
	print len(jason_data)
	epoch_now = int(datetime.datetime.now().strftime('%s'))


	# while 1==1:
	for item in jason_data[0]:
		# print item
		headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
		hash_object = hashlib.sha1(json.dumps(item)).hexdigest()

		creation_date = (datetime.datetime.strptime(item['not_before'], '%Y-%m-%dT%H:%M:%S'))
		epoch_cert = int(creation_date.strftime('%s'))

		if epoch_now <= epoch_cert :  #change it as >= if you want to view the certs which are old 
			print "[+][+][+][+][+][+][+]   NEW CERTIFICATE FOUND  [+][+][+][+][+][+][+][+] "
			# time.sleep(1)
		else:
			break

		print "\n\n"
		print "="*40
		print colored(' NEW CERTIFICATE FOUND ','blue')
		print "="*40
		print "\n"
		print colored('CERTID: ','red'),item['min_cert_id']
		print colored('ISSUER NAME: ','red'),item['issuer_name']
		print colored('DOMAIN NAME VALUE: ','red'),item ['name_value']
		print colored("CREATION DATE: ",'red'),item['not_before']
		print colored("EXPIRY DATE: ",'red'),item['not_after']
		print colored("[+]"*80,'white')
