#!/usr/bin/env python3

"""
lab 4: download files from bucket
"""
import boto3
import botocore
import logging

s3 = boto3.resource('s3')

filename="lab4_2a.py"
key = "new_" + filename
bucket_name = 'zpb004lab42bucket'

url = s3.generate_presigned_url(ClientMethod='get-object', Params={
    "Bucket": bucket_name,
    "Key": filename
})

print(url)
