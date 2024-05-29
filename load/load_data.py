import boto3
from io import StringIO
from config.config import AWS_REGION, S3_BUCKET_NAME, S3_OUTPUT_FILE

def load_data(data):
    csv_buffer = StringIO()
    data.to_csv(csv_buffer, index=False)
    s3_resource = boto3.resource('s3', region_name=AWS_REGION)
    s3_resource.Object(S3_BUCKET_NAME, S3_OUTPUT_FILE).put(Body=csv_buffer.getvalue())
