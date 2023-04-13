"""
This is a Python script that uses the Boto3 library to locate and stop EC2 instances.
"""

import boto3

# Create an EC2 client object
ec2 = boto3.client('ec2')

# Get all running instances
instances = ec2.describe_instances(
    Filters=[
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        }
    ]
)

# Stop each instance
for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        print(f"Stopping instance {instance['InstanceId']}")
        ec2.stop_instances(InstanceIds=[instance['InstanceId']])







