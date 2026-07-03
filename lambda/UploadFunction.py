import json
import boto3
import os

s3_client = boto3.client("s3")
BUCKET_NAME = os.environ.get("BUCKET_NAME", "my-file-sharing-bucket-amc")


def lambda_handler(event, context):
    try:
        file_name = event.get("queryStringParameters", {}).get("fileName")
        if not file_name:
            return _response(400, "Missing required query parameter: fileName")

        file_content = event.get("body", "")
        if file_content is None:
            file_content = ""

        print(f"[UPLOAD] key={file_name} bucket={BUCKET_NAME}")
        s3_client.put_object(
            Bucket=BUCKET_NAME,
            Key=file_name,
            Body=file_content.encode("utf-8"),
            ContentType="text/plain",
        )
        return _response(200, f"File '{file_name}' uploaded successfully to S3.")
    except Exception as e:
        return _response(500, f"Error uploading file: {str(e)}")


def _response(status_code, message):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
        },
        "body": json.dumps({"message": message}),
    }
