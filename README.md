# EC2 Lambda Controller

This project uses AWS Lambda and SAM to control EC2 instance state (start/stop) based on input.

## Prerequisites
- AWS CLI configured
- AWS SAM CLI installed
- Python 3.9
- EC2 Instance ID to control

## ✅ Project Structure

```text
ec2-lambda-control/
├── template.yaml             # SAM template
├── README.md                 # Deployment and testing instructions
└── src/
    └── ec2_controller.py     # Lambda function code

```

## Setup & Deploy
Create the EC2 instance want to control **before deploying** the Lambda function.  
Need the **Instance ID** to configure the Lambda environment variable.

 Build and Deploy with SAM
```bash
sam build
sam deploy --guided
```

During the guided deployment, you'll be prompted to:

* Provide a stack name: ec2-lambda-control
* Select AWS region: us-east-1
* Confirm the capabilities
* Set environment variables (e.g. INSTANCE_ID)



<img width="1137" height="585" alt="Screenshot 2025-07-28 at 11 09 46 AM" src="https://github.com/user-attachments/assets/a3a1fe42-4eaf-4e4e-a251-e2c47893c352" />



## Test After Deployment (AWS Console)

* Go to AWS Lambda Console → find your deployed function.
* Click Test tab.
* Configure a test event (JSON), e.g.:
```json
{
  "action": "stop"
}
```
* Save and then click Test.
* Check the response and logs to verify it works.

## Cleanup
To delete the stack: 
```bash
sam delete
```

