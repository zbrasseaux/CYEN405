#!/usr/bin/env python3

"""
lab 4: download files from bucket
"""
import boto3

bucket_name = 'zpb004lab42buc'

# Retrieve a bucket's ACL
s3 = boto3.client('s3')
result = s3.get_bucket_acl(Bucket=bucket_name)
print(result)
