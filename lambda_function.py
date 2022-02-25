import os
import json
from generate_image import cyberpunk_img_to_s3


def lambda_handler(event, context):

    cyberpunk_img_to_s3()

if __name__ == '__main__':
    lambda_handler(event=None, context=None)