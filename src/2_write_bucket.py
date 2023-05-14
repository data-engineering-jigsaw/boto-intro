import json
import boto3

s3 = boto3.client('s3')
# bucket = s3.create_bucket(Bucket = 'jigsaw-sample-json')

# s3.upload_file('./yelp-lunch-nyc.csv', 'jigsaw-sample-json', 'lunch.csv')

# obj = s3.get_object(Bucket='jigsaw-sample-json', Key='lunch.csv')

# obj['Body'].read()



# json_obj = {'hello': 'world'}

# s3.put_object(
#      Body=json.dumps(json_obj),
#      Bucket='jigsaw-sample-json',
#      Key='hello_world.json'
# )

# obj = s3.get_object(Bucket='jigsaw-sample-json', Key='hello_world.json')

# text = obj['Body'].read()

# hello_world_dict = json.loads(text)
