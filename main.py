import os
import random
from io import BytesIO

import boto3
import praw
import requests  # type: ignore
from dotenv import load_dotenv

load_dotenv()

S3_BUCKET = os.environ['S3_BUCKET']
CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
USERNAME = os.environ['USERNAME']
PASSWORD = os.environ['PASSWORD']


def cyberpunk_img_to_s3(image_type: str, limit: int) -> bool:
    """
    Scrape reddit's cyberpunk subreddit and upload image to S3 BUCKET

    Parameters
    ----------
    limit: int
        number of posts to scrape

    image_type: str
        scheduled or generated

    Returns True if image is uploaded to bucket
    """

    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        username=USERNAME,
        password=PASSWORD,
        user_agent="Scraping CYBERPUNK"
    )

    cyberpunk = reddit.subreddit('cyberpunk')

    valid_extensions = ['.jpeg', '.jpg', '.png', '.gif']
    urls = []
    extensions = []

    for post in cyberpunk.hot(limit=limit):

        _, extension = os.path.splitext(post.url)

        if extension.lower() in valid_extensions:
            urls.append(post.url.lower())
            extensions.append(extension)

    random_idx: int = random.randint(0, len(urls))  # this returns array
    image_url: str = urls[random_idx]
    image_ext: str = extensions[random_idx]

    try:
        response = requests.get(image_url)
    except Exception:
        raise ValueError('Connection refused')

    img = BytesIO(response.content)
    s3client = boto3.client('s3')
    try:
        s3client.upload_fileobj(
            Fileobj=img,
            Bucket=S3_BUCKET,
            Key=f'POST/cyberpunk_{image_type}',
            ExtraArgs={"ContentType": f"image/{image_ext.split('.')[1]}"}
        )
    except Exception:
        return False
    return True
