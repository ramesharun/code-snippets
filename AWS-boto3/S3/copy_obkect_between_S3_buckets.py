"""
#            .___    .___               __________        __         .__
#            |   | __| _/____    ____   \______   \ _____/  |_  ____ |  |
#            |   |/ __ |\__  \  /    \   |     ___// __ \   __\/ __ \|  |
#            |   / /_/ | / __ \|   |  \  |    |   \  ___/|  | \  ___/|  |__
#            |___\____ |(____  /___|  /  |____|    \___  >__|  \___  >____/
#                    \/     \/     \/                 \/          \/

Code Description:       Copy object from one S3 bucket to other S3 bucket (in AWS)
Auther:                 Idan Petel
Date:                   Dec 2020
Version:                1.0
Script Logic:           None
Environment Variables:  None
"""

import boto3
import logging

# logging config
LOG_LEVEL = logging.INFO
logging.basicConfig(level=LOG_LEVEL, format='### %(levelname)s ### - line: %(lineno)s, msg: %(message)s')
logger = logging.getLogger()

# --------------------- Using Resource (high-level) Client ---------------------
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.copy

# boto3 config
'''
# uncomment if this code will run on your local with existing AWS config is set up by AWS cli
session = boto3.Session(profile_name='<PROFILE-NAME>')
s3_resourceClient = session.resource('s3')
'''
# uncomment if this code will run on Lambda with IAM role
s3_resourceClient = boto3.resource('s3')


def copy_obj_between_buckets_usingResourceClient(source_bucket_name, target_bucket_name, obj_key):
    try:
        s3_resourceClient.Bucket(target_bucket_name).copy({'Bucket': source_bucket_name, 'Key': obj_key}, obj_key)
        logger.info('copy operation was completed successfully')
    except s3_resourceClient.meta.client.exceptions.ClientError as err:
        logger.warning(f'ClientError: {err}')
    except s3_resourceClient.meta.client.exceptions.ValidationError as err:
        logger.warning(f'ValidationError: {err}')


source_bucket_name = '<BUCKET-NAME-1>'
target_bucket_name = '<BUCKET-NAME-2>'
obj_key = '<OBJECT-KEY>'
copy_obj_between_buckets_usingResourceClient(source_bucket_name, target_bucket_name, obj_key)

# --------------------- Using Low-Level Client ---------------------
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.copy_object

# boto3 config
'''
# uncomment if this code will run on your local with existing AWS config is set up by AWS cli
session = boto3.Session(profile_name='<PROFILE-NAME>')
s3_resourceClient = session.resource('s3')
'''
# uncomment if this code will run on Lambda with IAM role
s3_resourceClient = boto3.resource('s3')


def copy_obj_between_buckets_usingClient(source_bucket_name, target_bucket_name, obj_key):
    try:
        s3_resourceClient.meta.client.copy({'Bucket': source_bucket_name, 'Key': obj_key}, target_bucket_name, obj_key)
        logger.info('copy operation was completed successfully')
    except s3_resourceClient.meta.client.exceptions.ClientError as err:
        logger.warning(f'ClientError: {err}')
    except s3_resourceClient.meta.client.exceptions.ValidationError as err:
        logger.warning(f'ValidationError: {err}')


source_bucket_name = '<BUCKET-NAME-1>'
target_bucket_name = '<BUCKET-NAME-2>'
obj_key = '<OBJECT-KEY>'
copy_obj_between_buckets_usingClient(source_bucket_name, target_bucket_name, obj_key)
