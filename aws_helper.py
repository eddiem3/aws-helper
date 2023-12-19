# -*- coding: utf-8 -*-
"""A module-level docstring

Notice the comment above the docstring specifying the encoding.
Docstrings do appear in the bytecode, so you can access this through
the ``__doc__`` attribute. This is also what you'll see if you call
help() on a module or any other Python object.
"""


import logging
import boto3
from botocore.exceptions import ClientError

import argparse






def push_model_to_s3(model_path, bucket_name='yolov8-sku-detector'):
     """
     Compress a model in aws .tar.gz format and upload to S3 bucket.

     :param str: The path to the model
     #TODO HANDLE ERRORS
    """
    
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
    
    


