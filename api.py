import json
import os
import sys
import re
import boto3
import botocore

import re

# Function to parse the string and create a dictionary
def parse_majors_and_descriptions(output):
    # Define a dictionary to store the parsed data
    majors_dict = {}

    # Regular expression to match major and description pairs
    pattern = r"-MAJOR: (.*?)\nDESCRIPTION: (.*?)(?=\n-MAJOR:|\Z)"

    # Find all matches
    matches = re.findall(pattern, output, re.DOTALL)

    # Process each match and store it in the dictionary
    for match in matches:
        major = match[0].strip()
        description = match[1].strip()
        majors_dict[major] = description
    
    return majors_dict


session = boto3.session.Session()
region = session.region_name
boto3_bedrock = boto3.client(service_name = 'bedrock-runtime',region_name = region)

prompt = "Recommend 3 majors based on personal context."
parameters = "I enjoy programming, science, and working on a team" # Context will be added here
formatting = "\nFormat your response like this: -Make the first word of each major 'MAJOR' -Before the description write 'DESCRIPTION' -Give a description that is around 100 words per major"

body = json.dumps(
    {
    "schemaVersion": "messages-v1",
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "text": prompt+parameters+formatting
                }
            ]
        }
    ],
    "inferenceConfig": {
        "maxTokens": 3000,
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
    llm_output = response_body["output"]["message"]["content"][0]["text"]
 
    # Parse the string and store the results in a dictionary
    majors_data = parse_majors_and_descriptions(llm_output)

    # Print the dictionary to verify
    print(majors_data)   
    
    
    

except botocore.exceptions.ClientError as error:
    if error.response['Error']['Code'] == 'AccessDeniedException':
           print(f"\x1b[41m{error.response['Error']['Message']}\
                \nTo troubeshoot this issue please refer to the following resources.\
                 \nhttps://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_access-denied.html\
                 \nhttps://docs.aws.amazon.com/bedrock/latest/userguide/security-iam.html\x1b[0m\n")
    else:
        raise error