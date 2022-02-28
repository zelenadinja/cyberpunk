import os

import boto3
from dotenv import load_dotenv
from flask import Flask, render_template
from mypy_boto3_lambda import LambdaClient

load_dotenv()

LAMBDA_GENERATE: LambdaClient = boto3.client('lambda')
LAMBDA_ARN: str = os.environ['LAMBDA_GENERATE_ARN']

app = Flask(__name__)


@app.route("/",  methods=['GET', 'POST'])
def scheduled_image():

    image = "https://cyberpunk-web-app.s3.eu-west-3.amazonaws.com/POST/cyberpunk_SCHEDULED"
    return render_template(template_name_or_list='scheduled_image.html', scheduled_image=image)


@app.route('/GENERATED', methods=['GET', 'POST'])
def generated_image():

    LAMBDA_GENERATE.invoke(
        FunctionName=LAMBDA_ARN,
        InvocationType='RequestResponse',
    )
    image = "https://cyberpunk-web-app.s3.eu-west-3.amazonaws.com/POST/cyberpunk_GENERATED"
    return render_template(template_name_or_list='generated_image.html', generated_image=image)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
