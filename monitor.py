##monitoring for the certificate transpirincy by www.crt.sh
#we are using the unoficial crtsh api and the elastic search
#elastic search databse stores the data and when the program runs after every 12 hrs 
#it checks if there is new certificate has been  generated  it will prompt new certificate found or else it will sleep for next 12 hrs.
from crtsh import crtshAPI
import json
import requests
from pprint import pprint 
import hashlib
import time

data_feed=json.dumps(crtshAPI().search('cyware.com'))

while True:

	cyware=json.loads(data_feed) 
	es_url="http://127.0.0.1:9200/cert_new/cywar/"
	dummp_post  = requests.get(es_url)
	for item in cyware[0]:
		headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
		hash_object = hashlib.sha1(json.dumps(item)).hexdigest()
		min_cert_id = item['min_cert_id']
		#print json.dumps(item)	
		dummp_post  = requests.post(es_url+str(item['min_cert_id']),headers=headers,data=json.dumps(item))
		view=json.loads(dummp_post.text)
		if view["_version"] <= 1:	
			print "="*40
			print "NEW CERTIFICATE FOUND"
			print "="*40
			print "CERTID: " ,item['min_cert_id']
			print "ISSUER NAME: ",item['issuer_name']
			print "NAME VALUE: ",item ['name_value']
			print "CREATION DATE: ",item['not_before']
			print "EXPIRY DATE: ",item['not_after']
			print "\n\n"

	time.sleep(43200)
	#curl -XDELETE http://127.0.0.1:9200/cert_new/
