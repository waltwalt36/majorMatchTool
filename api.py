import json
import os
import sys

import boto3
import botocore

session = boto3.session.Session()
region = session.region_name
boto3_bedrock = boto3.client(service_name = 'bedrock-runtime',region_name = region)

prompt = f"""
What major would you recommend for a student who loves to program and would like to be an entrepreneur?
"""

body = json.dumps(
    {
    "schemaVersion": "messages-v1",
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "text": prompt
                }
            ]
        }
    ],
    "inferenceConfig": {
        "maxTokens": 300,
        "temperature": 0.3,
        "topP": 0.1,
        "topK": 20
    }
})

modelId = "us.amazon.nova-lite-v1:0"  # Nova Lite model ID
accept = 'application/json'
contentType = 'application/json'

try:
    response = boto3_bedrock.invoke_model(
        body=body, 
        modelId=modelId, 
        accept=accept, 
        contentType=contentType
    )
    response_body = json.loads(response.get('body').read())
    
    # Nova models return response in a different format
    content_text = response_body["output"]["message"]["content"][0]["text"]
    print(content_text)

except botocore.exceptions.ClientError as error:
    if error.response['Error']['Code'] == 'AccessDeniedException':
           print(f"\x1b[41m{error.response['Error']['Message']}\
                \nTo troubeshoot this issue please refer to the following resources.\
                 \nhttps://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_access-denied.html\
                 \nhttps://docs.aws.amazon.com/bedrock/latest/userguide/security-iam.html\x1b[0m\n")
    else:
        raise error