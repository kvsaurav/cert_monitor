##monitoring for the certificate transpirincy by www.crt.sh
#we are using the unoficial crtsh api and the elastic search
#elastic search databse stores the data and when the program runs after every 12 hrs 
#it checks if there is new certificate has been  generated  it will prompt new certificate found or else it will sleep for next 12 hrs.
#TEST CASE FOR FRIDAY 28 taking domain input from the user
#updated on july 2 19

from crtsh import crtshAPI
import json
import requests
from pprint import pprint 
import hashlib
import time
from termcolor import colored

print "=="*50
print "**"*50
a = raw_input("ENTER THE NAME FOR THE DOMAIN TO BE SEARCHED : ")
print colored('SEARCHING CERTIFICATES FOR ','red'),a
jason_data=json.dumps(crtshAPI().search(a))
jason_data=json.loads(jason_data)
#print len(jason_data)
for item in jason_data[0]:
		#print item
		print "*"*40
		headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
		hash_object = hashlib.sha1(json.dumps(item)).hexdigest()
		#min_cert_id = item['min_cert_id']
		#for item in jason_data
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