import json
import boto3
from datetime import datetime

def lambda_handler(event, context):
    
    current_time = datetime.now()  # gets the current time 
    
    date_time = current_time.strftime("%m/%d/%Y, %H:%M:%S") #coverts current time into string and unicode
    
    sqs = boto3.client('sqs') # gets the service client 
    
    response = sqs.send_message(
    
    QueueUrl='https://sqs.us-east-1.amazonaws.com/397758027793/OrderTracker',  # adding URL of the SQS queue
    
    MessageBody= date_time) # body of the message 
    
    return {
        'statusCode': 200,
        'body': json.dumps(date_time)
    }