# coding: utf-8
from TwitterAPI import TwitterAPI
import boto3
import json
import twitterCreds

## twitter credentials

consumer_key = twitterCreds.consumer_key
consumer_secret = twitterCreds.consumer_secret
access_token_key = twitterCreds.access_token_key
access_token_secret = twitterCreds.access_token_secret

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

kinesis = boto3.client('kinesis')

filter = {'locations':'32.2,29.9,146.2,39.0,138.4,33.5,146.1,46.20','track':u'釣り'}
#filter = {'locations':'32.2,29.9,146.2,39.0,138.4,33.5,146.1,46.20'}

r = api.request('statuses/filter', filter)
keywords = {u'釣り','fishing'}
for item in r:
#	print item['user_name']	
	for keyword in keywords:
		if(item['text'].find(keyword)>0):
			print item['text'].find(keyword),item['text']	
			kinesis.put_record(StreamName="twitter", Data=json.dumps(item), PartitionKey="filler")
