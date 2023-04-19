import boto3

#service resource
sqs = boto3.resource('sqs', region_name='us-east-1')

#creates the queue, and returns an SQS.Queue instance
queue = sqs.create_queue(QueueName='OrderTracker')

#URL that will be needed for our next code. 
print(queue.url)




"""
import boto3
import datetime

# Get the service resource
sqs = boto3.resource('sqs', region_name='us-east-1')

# Define name
queue_name = 'OrderTracker'

def lambda_handler(event, context):
    #get the URL
    queue_url = sqs.get_queue_url(QueueName=queue_name)['QueueUrl']
    
    # Get the current time as a string
    current_time = str(datetime.datetime.now())
    
    # Send the message to the queue
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=current_time
    )
    
    # Print the response to the log
    print(response)
    

"""