import boto3
import os

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    instance_id = os.environ['INSTANCE_ID']  # ENV VAR NAME, not the actual ID
    action = event.get('action')

    if action == 'start':
        response = ec2.start_instances(InstanceIds=[instance_id])
        return {"status": "started", "response": response}
    elif action == 'stop':
        response = ec2.stop_instances(InstanceIds=[instance_id])
        return {"status": "stopped", "response": response}
    else:
        return {"status": "error", "message": "Invalid action. Use 'start' or 'stop'."}
