from typing import List, Dict, Any
import requests
import json
import io
import sys
import os

import bs4  # type: ignore
from bs4 import BeautifulSoup
import boto3
from tqdm import tqdm
from botocore.exceptions import ClientError
from boto3_type_annotations.s3 import Client
from dotenv import load_dotenv
import argparse


load_dotenv()

S3_BUCKET = os.environ['S3_BUCKET']


def get_params():
    """CLI arguments for running scripts"""

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'movies_url',
         type=str,
          help='URL with movie titles')
    parser.add_argument(
        's3_object_key',
        type=str,
        help='Object key for movie titles file',
    )
    arguments = parser.parse_args()

    return arguments


def get_titles(url: str) -> List[str]:
    """
    Get movie titles.

    Parameters
    ----------

    url: str
    link of website

    Return
        titles: List[str]
            movie titles

    """
    response = requests.get(str(url))
    soup = BeautifulSoup(response.content, 'html5lib')
    titles: List[Any] = soup.find_all(
        'span', attrs={"itemprop": "name"}
    )
    titles.pop(0)  # First item is title of webpage
    titles = [title.text for title in titles]

    return titles


def json_to_s3(object_body: Any, object_key: str) -> bool:
    """
    Uploadt json object to S3 Bucket,
    first dumps obj to json format.

    Parameters:
    ----------
    obj_body: Any
        object to be converted to json object

    object_key: str
        object key for s3 bucket

    Returns True if uploaded to Bucket.
    """
    json_obj = json.dumps(object_body) # json object
    filesize: int = sys.getsizeof(json_obj)

    s3client: Client = boto3.client('s3')

    try:
        with tqdm(total=filesize, unit='B', unit_scale=True, desc='Uploading file to S3 Bucket') as pbar:

            s3client.upload_fileobj(
                Fileobj=io.BytesIO(json_obj.encode()),
                Bucket=S3_BUCKET,
                Key=object_key,
                Callback= lambda bytes_uploaded: pbar.update(bytes_uploaded)
            )
    except ClientError:
        return False
    return True

if __name__ == '__main__':

    args = get_params()
    print(args.movies_url)
    print(args.s3_object_key)
    titles = get_titles(url=args.movies_url)
    json_to_s3(object_body=titles, object_key=args.s3_object_key)

