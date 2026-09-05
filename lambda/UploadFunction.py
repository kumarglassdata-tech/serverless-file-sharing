import json
import boto3
import os

s3_client = boto3.client("s3")
BUCKET_NAME = os.environ.get("BUCKET_NAME", "my-file-sharing-bucket-amc")
MAX_FILENAME_LENGTH = 255


def lambda_handler(event, context):
    try:
        file_name = event.get("queryStringParameters", {}).get("fileName")
        if not file_name:
            return _response(400, "Missing required query parameter: fileName")

        if ".." in file_name or file_name.startswith("/"):
            return _response(400, "Invalid fileName")

        if len(file_name) > MAX_FILENAME_LENGTH:
            return _response(400, f"fileName exceeds {MAX_FILENAME_LENGTH} characters")

        file_content = event.get("body", "")
        if file_content is None:
            file_content = ""

        print(f"[UPLOAD] key={file_name} bucket={BUCKET_NAME} size={len(file_content)}")

        s3_client.put_object(
            Bucket=BUCKET_NAME,
            Key=file_name,
            Body=file_content.encode("utf-8"),
            ContentType="text/plain",
        )
        return _response(200, f"File '{file_name}' uploaded successfully to S3.")

    except Exception as e:
        print(f"[UPLOAD] ERROR: {e}")
        return _response(500, f"Error uploading file: {str(e)}")


def _response(status_code: int, message: str) -> dict:
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
        },
        "body": json.dumps({"message": message}),
    }
