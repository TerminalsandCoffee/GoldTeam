"""
This is a Python script using the Boto3 library that will stop three EC2 instances:
"""

import boto3

# Specify the region where your instances are running
region = 'us-east-1'

# Specify the IDs of the instances you want to stop
instance_ids = ['i-xxx', 'i-xxx', 'i-xxx']

# Create an EC2 client object
ec2 = boto3.client('ec2', region_name=region)

# Stop the instances
ec2.stop_instances(InstanceIds=instance_ids)

print('Stopped instances: ' + ', '.join(instance_ids))


"""
Replace the instance IDs
Note that you will need to have valid AWS credentials configured for the script to be able to access your instances.

"""