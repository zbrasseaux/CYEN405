#!/usr/bin/env python3

"""
lab 4: describe buckets
"""
import boto3
from botocore.exceptions import ClientError

s3_client = boto3.client('s3')
response = s3_client.list_buckets()

print("Existing Buckets:")
for bucket in response['Buckets']:
    print('\t' + f' {bucket["Name"]} ')
    
