"""Unit tests for UploadFunction and DownloadFunction."""
import json, os, sys, unittest
from unittest.mock import MagicMock, patch

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lambda"))
os.environ["BUCKET_NAME"] = "my-file-sharing-bucket-amc"

def _event(file_name="test.txt", body="Hello World!"):
    return {"queryStringParameters": {"fileName": file_name}, "body": body}

class TestUploadFunction(unittest.TestCase):
    @patch("UploadFunction.s3_client")
    def test_success(self, mock_s3):
        mock_s3.put_object = MagicMock(return_value={})
        import UploadFunction; UploadFunction.s3_client = mock_s3
        r = UploadFunction.lambda_handler(_event(), None)
        self.assertEqual(r["statusCode"], 200)

    @patch("UploadFunction.s3_client")
    def test_missing_filename(self, mock_s3):
        import UploadFunction; UploadFunction.s3_client = mock_s3
        r = UploadFunction.lambda_handler({"queryStringParameters": {}, "body": "x"}, None)
        self.assertEqual(r["statusCode"], 400)

    @patch("UploadFunction.s3_client")
    def test_path_traversal(self, mock_s3):
        import UploadFunction; UploadFunction.s3_client = mock_s3
        r = UploadFunction.lambda_handler(_event(file_name="../etc/passwd"), None)
        self.assertEqual(r["statusCode"], 400)

    @patch("UploadFunction.s3_client")
    def test_s3_error(self, mock_s3):
        mock_s3.put_object = MagicMock(side_effect=Exception("fail"))
        import UploadFunction; UploadFunction.s3_client = mock_s3
        r = UploadFunction.lambda_handler(_event(), None)
        self.assertEqual(r["statusCode"], 500)

class TestDownloadFunction(unittest.TestCase):
    @patch("DownloadFunction.s3_client")
    def test_success(self, mock_s3):
        body = MagicMock(); body.read.return_value = b"content"
        mock_s3.get_object = MagicMock(return_value={"Body": body})
        import DownloadFunction; DownloadFunction.s3_client = mock_s3
        r = DownloadFunction.lambda_handler(_event(), None)
        self.assertEqual(r["statusCode"], 200)
        self.assertEqual(r["body"], "content")

    @patch("DownloadFunction.s3_client")
    def test_missing_filename(self, mock_s3):
        import DownloadFunction; DownloadFunction.s3_client = mock_s3
        r = DownloadFunction.lambda_handler({"queryStringParameters": {}}, None)
        self.assertEqual(r["statusCode"], 400)

    @patch("DownloadFunction.s3_client")
    def test_path_traversal(self, mock_s3):
        import DownloadFunction; DownloadFunction.s3_client = mock_s3
        r = DownloadFunction.lambda_handler(_event(file_name="../../secret"), None)
        self.assertEqual(r["statusCode"], 400)

if __name__ == "__main__":
    unittest.main()
