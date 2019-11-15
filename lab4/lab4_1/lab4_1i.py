#!/usr/bin/env python3

"""
lab 4: create security group
"""
import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

try:
    response = ec2.create_security_group(GroupName='launch-wizard-10', Description='na')
    print("Success: ", response)
except ClientError as e:
    print(e)
    
    