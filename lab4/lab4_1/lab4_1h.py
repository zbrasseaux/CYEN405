#!/usr/bin/env python3

"""
lab 4: create key pair
"""
import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

try:
    response = ec2.describe_security_groups(GroupIds=['sg-073c34c8297e96056'])
    print("Success: ", response)
except ClientError as e:
    print(e)
    
    