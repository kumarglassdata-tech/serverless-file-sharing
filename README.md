# Serverless File Sharing Platform

Upload and download files via a simple HTTP API using AWS Lambda, API Gateway and S3.

## Architecture

```
Client (Postman / curl)
        │
  API Gateway  (my-file-sharing-api-amc)
        │
  /files
  POST → UploadFunction → S3
  GET  → DownloadFunction ← S3
```

## Deploy

```bash
sam build
sam deploy --guided
```

## Usage

Upload:
```bash
curl -X POST "https://<api>.execute-api.<region>.amazonaws.com/dev/files?fileName=hello.txt"   -H "Content-Type: text/plain" -d "Hello World!"
```

Download:
```bash
curl "https://<api>.execute-api.<region>.amazonaws.com/dev/files?fileName=hello.txt"
```

## Troubleshooting

| Error | Cause | Fix |
|---|---|---|
| `403 Forbidden` | IAM role missing S3 permission | Check `FileSharingLambdaRole` policy |
| `400 Missing fileName` | Query param absent | Add `?fileName=yourfile.txt` to the URL |
| `400 Invalid fileName` | Path traversal attempt | Remove `..` or leading `/` from fileName |
| `500 Error uploading` | S3 bucket not found | Verify `BUCKET_NAME` env var matches deployed bucket |
