import json
import urllib.parse
import boto3
import logging 
import requests
from datetime import 
print('Loading function')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

s3 = boto3.client('s3')


def lambda_handler(event, context)
    #print(Received event  + json.dumps(event, indent=2))
    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    
    
    metadata=s3.head_object(Bucket=bucket,Key=key)
    print(metadata)
    rek = boto3.client('rekognition')
    labels = rek.detect_labels(
            Image={
                'S3Object' {
                    'Bucket' bucket,
                    'Name' key
                }
            },
            MaxLabels=10
        )
           
    print(IMAGE LABELS --- {}.format(labels['Labels']))
    obj = {}
    obj['objectKey'] = key
    obj[bucket] = bucket
    obj[createdTimestamp] = metadata['ResponseMetadata']['HTTPHeaders']['date']
    obj[labels] = []
    meta_labels=metadata['ResponseMetadata']['HTTPHeaders']['x-amz-meta-customlabels']
    print(meta_labels)
    for label in labels['Labels']
        obj[labels].append(label['Name'])
    for each in meta_labels
        obj[labels].append(each)
    print(JSON OBJECT --- {}.format(obj))
    elastic_search_url=httpssearch-photos-dircg3er2caklwxzea655vnawy.us-east-1.es.amazonaws.comphotos_doc
    di_json=json.dumps(obj)
    response=requests.post(url=elastic_search_url, data=di_json, headers={content-type applicationjson}, auth=('ccbd', 'Ccbd@2021'))