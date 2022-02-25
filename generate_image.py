import os

import praw
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
USERNAME = os.environ['USERNAME']
PASSWORD = os.environ['PASSWORD']

REDDIT = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    username=USERNAME,
    password=PASSWORD,
    user_agent="Scraping CYBERPUNK"
)

CYBERPUNK_SUB = REDDIT.subreddit('cyberpunk')
