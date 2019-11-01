#!/usr/bin/env python3

"""
lab 4: create key pair
"""
import boto3
from botocore.exceptions import ClientError

filename="lab4_2a.py"
bucket_name = 'zpb004lab42buc'

s3_client = boto3.client('s3')
s3_client.upload_file(filename, bucket_name, filename)
    
