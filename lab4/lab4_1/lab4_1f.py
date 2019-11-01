#!/usr/bin/env python3

"""
lab 4: create key pair
"""
import boto3

ec2 = boto3.client('ec2')


response = ec2.create_key_pair(KeyName='zpb004_lab41f_key')
print("Success: ", response)

    
    