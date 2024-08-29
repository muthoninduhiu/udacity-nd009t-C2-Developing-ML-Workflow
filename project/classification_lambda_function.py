import json
import boto3
import base64

# Initialize SageMaker runtime client
runtime = boto3.Session().client('sagemaker-runtime')

# Fill this in with the name of your deployed model
ENDPOINT = 'trial5-endpoint'

def lambda_handler(event, context):
    print("Incoming image data:", event.get('image_data'))
    image = base64.b64decode(event['image_data'])
        # Invoke the SageMaker endpoint
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT,ContentType='image/png',Body=image)
    
    
    # Extract and decode the inferences
    inferences = json.loads(response['Body'].read().decode('utf-8'))
        
        # Add inferences to the response
    event["inferences"] = inferences
        
        # Return the response with status code 200
   # We return the data back to the Step Function    
    return {
        'statusCode': 200,
        'body': {
            "image_data": event['image_data'],
            "s3_bucket": event['s3_bucket'],
            "s3_key": event['s3_key'],
            "inferences": event['inferences'],
        }
        
    }
  