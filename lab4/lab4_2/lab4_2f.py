#!/usr/bin/env python3

"""
lab 4: download files from bucket
"""
import boto3
import json

s3 = boto3.client('s3')

filename="lab4_2a.py"
key = "new_" + filename
bucket_name = 'zpb004lab42buc'

bucket_policy = {
    'Verion': '2012-10-17',
    'Statement': [{
        'Sid': 'AddPerm',
        'Effect': 'Allow',
        'Principal': '*',
        'Action': ['s3:GetObject'],
        'Resource': "arn:aws:s3:::%s/*" % bucket_name
    }]
}

bucket_policy = json.dumps(bucket_policy)
s3.put_bucket_policy(Bucket=bucket_name,Policy=bucket_policy)

response = s3.get_bucket_policyl(Bucket=bucket_name)

print(response['Policy'])
