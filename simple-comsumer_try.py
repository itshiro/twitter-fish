# coding: utf-8
import boto3
#from botocore.exceptions import ProvisionedThroughputExceededException
import time
import json

## aws creds are stored in ~/.boto
kinesis = boto3.client("kinesis")
shard_id = "shardId-000000000000" #only one shard!
pre_shard_it = kinesis.get_shard_iterator(StreamName="twitter", ShardId=shard_id, ShardIteratorType="LATEST")
shard_it = pre_shard_it["ShardIterator"]
while 1==1:
	try:
		out = kinesis.get_records(ShardIterator=shard_it, Limit=1)
		shard_it = out["NextShardIterator"]
#		print json.dumps(out,ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
#		print json.dumps(out['Records']['text'],ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
		for record in out['Records']:
#			print "record:---------------------------------------------------------------"
#			print record
			data = record["Data"]
#			print "Data:---------------------------------------------------------------"
#			print data
			j_data = json.loads(data)
#			print "text:---------------------------------------------------------------"
			print j_data["text"]
#			print json.dumps(record,ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
#			for item in record['Data']:
#				print item
#	except boto3.kinesis.exceptions.ProvisionedThroughputExceededException:
	except Exception as e:
		print e.message
		time.sleep(5)