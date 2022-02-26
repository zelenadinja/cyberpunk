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
    return render_template(template_name_or_list='scheduled_image.html')


@app.route('/GENERATED', methods=['GET', 'POST'])
def generated_image():
    LAMBDA_GENERATE.invoke(
        FunctionName=LAMBDA_ARN,
        InvocationType='RequestResponse',
    )
    return render_template(template_name_or_list='generated_image.html')


if __name__ == '__main__':
    app.run(debug=True)
