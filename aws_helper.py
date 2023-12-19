import logging
import boto3
from botocore.exceptions import ClientError

import argparse


def push_model_to_s3(model_path, bucket_name='yolov8-sku-detector'):
    s3 = boto3.client('s3')
    archive_path = compress_model(model_path)
    model_uri = s3.upload_file(
        Filename=archive_path,
        Bucket=bucket_name,
        Key=os.path.basename(archive_path)
    )
    return model_uri



if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    args = parser.parse_args()

    push_model_to_s3(args.path)
    
    


