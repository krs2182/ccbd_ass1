import json
import logging 
import boto3
import requests


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def get_slots(intent_request):
    return intent_request['currentIntent']['slots']


def sendToLex(message):
    
    return response
    
def lambda_handler(event, context):
    # TODO implement
    photos = []
    print("Printing event",event, len(event))
    print("Printing Context",context)
    logger.debug(event)
    #API gateway connection is required to pass the querystring
    message = event["queryStringParameters"]['q']
    print("event")
    logger.debug("event")
    #message="I want pictures of balls"
    lex = boto3.client('lex-runtime')
    response = lex.post_text(
        botName='PhotoAlbumQueries',
        botAlias='photoalbum',
        userId='lf1',
        inputText=message)
    print("LEX Response:", response)
    keywords=[]
    keywords.append(response['slots']['keyword'])
    if(response['slots']['keyword_']):
        keywords.append(response['slots']['keyword_'])
    
    photos = []
    for keyword in keywords:
        elastic_url='https://search-photos-dircg3er2caklwxzea655vnawy.us-east-1.es.amazonaws.com/photos/_search?q='+keyword
        resp = requests.get(elastic_url, headers={"Content-Type": "application/json"},auth=('ccbd', 'Ccbd@2021')).json()
        # res = json.loads(res.content.decode('utf-8'))
        print(resp)
        for item in resp["hits"]["hits"]:
            bucket = item["_source"]["bucket"]
            key = item["_source"]["objectKey"]
            photoURL = "https://{0}.s3.amazonaws.com/{1}".format(bucket,key)
            if photoURL not in photos:
                photos.append(photoURL)
    print(photos)
    return {
        'statusCode': 200,
        'isBase64Encoded': False,
        'headers':
            {
                'Access-Control-Allow-Origin':'*'
            },
        'body': json.dumps(photos)
    }