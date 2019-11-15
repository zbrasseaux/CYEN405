#!/usr/bin/env python

"""
lab 4: first boto3 activity
"""
import sys
import boto3

ec2 = boto3.client('ec2')

if sys.argv[1] == 'ON':
    response = ec2.monitor_instances(InstanceIds=['i-0209a281dd8fe0123'])
else:
    response = ec2.unmonitor_instances(InstanceIds=['i-0209a281dd8fe0123'])
    
print(response)
