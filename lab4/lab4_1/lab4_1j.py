#!/usr/bin/env python3

"""
lab 4: delete security group
"""
import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

try:
    response = ec2.delete_security_group(GroupName='launch-wizard-10')
    print("Success: ", response)
except ClientError as e:
    print(e)
    
    