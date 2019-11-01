#!/usr/bin/env python

"""
lab 4: first boto3 activity
"""

import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_instances()

print(response)
