##monitoring for the certificate transpirincy by www.crt.sh
#we are using the unoficial crtsh api and the elastic search
#elastic search databse stores the data and when the program runs after every 12 hrs 
#it checks if there is new certificate has been  generated  it will prompt new certificate found or else it will sleep for next 12 hrs.
#TEST CASE FOR FRIDAY 28 taking domain input from the user
from crtsh import crtshAPI
import json
import requests
from pprint import pprint 
import hashlib
import time

print "=="*50
print "ENTER THE NAME FOR THE DOMAIN TO BE SEARCHED :"
print "**"*50
a = raw_input("") 
print "SEARCHING CERTIFICATES FOR ", a 
jason_data=json.dumps(crtshAPI().search(a))
#pprint(jason_data,indent = 40)
jason_data=json.loads(jason_data)
#print len(jason_data)
for item in jason_data[0]:
		#print item
		print "*"*40
		headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
		hash_object = hashlib.sha1(json.dumps(item)).hexdigest()
		#min_cert_id = item['min_cert_id']
		#for item in jason_data
		print "\n\n\n\n"
		print "="*40
		print "NEW CERTIFICATE FOUND"
		print "="*40
		print "\n"
		print "CERTID: " ,item['min_cert_id']
		print "ISSUER NAME: ",item['issuer_name']
		print "NAME VALUE: ",item ['name_value']
		print "CREATION DATE: ",item['not_before']
		print "EXPIRY DATE: ",item['not_after']