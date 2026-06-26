import boto3
from botocore.exceptions import ClientError
from src.config import Config
import mimetypes

class S3Manager:
    def __init__(self):
        Config.validate()
        self.s3_client = boto3.client(
            "s3",
            aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
            region_name=Config.AWS_REGION
        )
        self.bucket_name = Config.AWS_BUCKET_NAME

    def upload_file(self, file_obj, filename: str) -> bool:
        """Uploads file with correct MIME type detection."""
        try:
            content_type, _ = mimetypes.guess_type(filename)
            if not content_type:
                content_type = 'application/octet-stream'
                
            self.s3_client.upload_fileobj(
                file_obj,
                self.bucket_name,
                filename,
                ExtraArgs={"ContentType": content_type}
            )
            return True
        except ClientError as e:
            print(f"Upload Error: {e}")
            return False

    def list_files(self, search_query: str = ""):
        """Lists files and gathers object metadata."""
        try:
            response = self.s3_client.list_objects_v2(Bucket=self.bucket_name)
            files = []
            if 'Contents' in response:
                for obj in response['Contents']:
                    filename = obj['Key']
                    if search_query.lower() in filename.lower():
                        files.append({
                            "key": filename,
                            "size": round(obj['Size'] / 1024, 2),  # KB
                            "last_modified": obj['LastModified'].strftime("%Y-%m-%d %H:%M:%S")
                        })
            return files
        except ClientError as e:
            print(f"List Error: {e}")
            return []

    def get_download_url(self, filename: str):
        """Generates a secure presigned URL for secure downloading."""
        try:
            url = self.s3_client.generate_presigned_url(
                'get_object',
                Params={'Bucket': self.bucket_name, 'Key': filename},
                ExpiresIn=3600 # Valid for 1 hour
            )
            return url
        except ClientError as e:
            print(f"Presigned URL Error: {e}")
            return None

    def delete_file(self, filename: str) -> bool:
        """Removes a file object from the S3 bucket."""
        try:
            self.s3_client.delete_object(Bucket=self.bucket_name, Key=filename)
            return True
        except ClientError as e:
            print(f"Delete Error: {e}")
            return False