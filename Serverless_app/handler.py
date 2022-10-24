import json


def Text(event, context):
   return dict(
        statusCode = 200,
        body = "First sevrerless app function run as service by aws lambda"
   )

 
