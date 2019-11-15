#!/usr/bin/env python3

"""
lab 4: first boto3 activity
"""
import sys
import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

try:
    ec2.reboot_instances(InstanceIds=['i-037a7ebc2f630d7b7'], DryRun=True)
except ClientError as e:
    if 'DryRunOperation' not in str(e):
        raise
# dry run succeeded
try:
    response = ec2.reboot_instances(InstanceIds=['i-037a7ebc2f630d7b7'], DryRun=False)
    print("Success: ", response)
except ClientError as e:
    print("Error: ", e)  
        

    
    