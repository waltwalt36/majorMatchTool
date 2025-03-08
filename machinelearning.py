import boto3
import json

# Initialize Amazon Bedrock Runtime client
bedrock_runtime = boto3.client("bedrock-runtime", region_name="us-west-2")

def test_bedrock():
    """Send a test prompt to Nova and print the response."""
    
    prompt = "What is the capital of Japan?"

    payload = {
  "modelId": "amazon.nova-lite-v1:0",
  "contentType": "application/json",
  "accept": "application/json",
  "body": {
    "inferenceConfig": {
      "max_new_tokens": 1000
    },
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "text": prompt
          }
        ]
      }
    ]
  }
}

    # Invoke the Titan Lite model
    response = bedrock_runtime.invoke_model(
        modelId="amazon.nova-lite-v1:0",  # Titan lite id copied from website
        body=json.dumps(payload)
    )

    # Parse response
    response_body = json.loads(response["body"].read().decode("utf-8"))
    print("AI Response:", response_body["outputText"])

# Run test
if __name__ == "__main__":
    test_bedrock()