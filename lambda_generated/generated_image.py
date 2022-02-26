import os

from dotenv import load_dotenv

from main import cyberpunk_img_to_s3

load_dotenv()

def lambda_handler(event, context):

    cyberpunk_img_to_s3(image_type="GENERATED", limit=int(os.environ['GENERATED_LIMIT']))
