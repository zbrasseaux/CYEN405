#!/usr/bin/env python

"""
lab 4: first boto3 activity
"""
import sys
import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

action = sys.argv[1].upper()

if action == 'ON':
    # dry run to verify permissions
    try:
        ec2.start_instances(InstanceIds=['i-037a7ebc2f630d7b7'], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise
    # dry run succeeded
    try:
        response = ec2.start_instances(InstanceIds=['i-037a7ebc2f630d7b7'], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)  
        
elif action == 'OFF':
    # dry run to verify permissions
    try:
        ec2.stop_instances(InstanceIds=['i-037a7ebc2f630d7b7'], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise
    # dry run succeeded
    try:
        response = ec2.stop_instances(InstanceIds=['i-037a7ebc2f630d7b7'], DryRun=False)
        print(response)
    except ClientError as e:
        print(e) 
        
else:
    print("Invalid option: " + action + "\nPlease try again")
    
    
# else:
#     response = ec2.unmonitor_instances(InstanceIds=['i-037a7ebc2f630d7b7'])
    
# print(response)
