# -*- coding: utf-8 -*-

import os
from os import listdir
from os.path import isfile, join
import boto3

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_BUCKET_NAME = os.environ.get("AWS_BUCKET_NAME")
AWS_STORAGE_URL = os.environ.get("AWS_STORAGE_URL")
AWS_AUTH_REGION_NAME = os.environ.get("AWS_AUTH_REGION_NAME")

filepath = "test/"

session = boto3.session.Session()
s3 = session.client(
    service_name='s3',
    endpoint_url='https://storage.yandexcloud.net',
    aws_access_key_id = AWS_ACCESS_KEY_ID,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY
)

onlyfiles = [f for f in listdir(filepath) if isfile(join(filepath, f))]

sortfiles = sorted(onlyfiles)

items = []

for item in sortfiles:
    items.append({'item': item})

i = len(items)

for i in range(0, i):
    filename = items[i]['item']
    print('Uploading ' + filename + ' to S3 bucket ' + AWS_BUCKET_NAME + ' as {}'.format(filepath, AWS_BUCKET_NAME, os.path.basename(filepath)))
    s3.upload_file(filepath + filename, AWS_BUCKET_NAME, filepath + filename)

for key in s3.list_objects(Bucket=AWS_BUCKET_NAME)['Contents']:
    print(key['Key'])