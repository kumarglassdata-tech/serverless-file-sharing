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

        if ".." in file_name or file_name.startswith("/"):
            return _response(400, "Invalid fileName")

        print(f"[DOWNLOAD] key={file_name} bucket={BUCKET_NAME}")

        s3_response = s3_client.get_object(Bucket=BUCKET_NAME, Key=file_name)
        file_content = s3_response["Body"].read().decode("utf-8")

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "text/plain",
                "Access-Control-Allow-Origin": "*",
                "Content-Disposition": f'attachment; filename="{file_name}"',
                "X-File-Name": file_name,
            },
            "body": file_content,
        }

    except s3_client.exceptions.NoSuchKey:
        return _response(404, f"File '{file_name}' not found.")
    except Exception as e:
        print(f"[DOWNLOAD] ERROR: {e}")
        return _response(500, f"Error downloading file: {str(e)}")


def _response(status_code: int, message: str) -> dict:
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
        },
        "body": json.dumps({"message": message}),
    }
