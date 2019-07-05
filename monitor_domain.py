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


print "=="*50
print "**"*50
a = raw_input("ENTER THE NAME FOR THE DOMAIN TO BE SEARCHED : ")
print colored('SEARCHING CERTIFICATES FOR ','red'),a
jason_data=json.dumps(crtshAPI().search(a))
jason_data=json.loads(jason_data)

#print jason_data
#print len(jason_data)
epoch_now = int(datetime.datetime.now().strftime('%s'))


while True:
		for item in jason_data[0]:
			# print item
			headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
			hash_object = hashlib.sha1(json.dumps(item)).hexdigest()

			creation_date = (datetime.datetime.strptime(item['not_before'], '%Y-%m-%dT%H:%M:%S'))
			epoch_cert = int(creation_date.strftime('%s'))

			if epoch_now <= epoch_cert :
				print "[+][+][+][+][+][+][+]   NEW CERTIFICATE FOUND	[+][+][+][+][+][+][+][+] "
				time.sleep(1)
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

