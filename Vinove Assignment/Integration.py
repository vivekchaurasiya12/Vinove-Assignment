import os
import gzip
import boto3
from PIL import ImageGrab
from datetime import datetime

# Configure your AWS credentials and bucket name
AWS_ACCESS_KEY = 'your_access_key'
AWS_SECRET_KEY = 'your_secret_key'
S3_BUCKET_NAME = 'your_bucket_name'

# Initialize the S3 client
s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)

# Function to compress the screenshot before upload
def compress_image(image_path):
    compressed_path = image_path.replace('.png', '.gz')
    with open(image_path, 'rb') as f_in:
        with gzip.open(compressed_path, 'wb') as f_out:
            f_out.writelines(f_in)
    return compressed_path

# Function to upload the file to S3
def upload_to_s3(file_path, bucket_name, object_name):
    try:
        s3_client.upload_file(file_path, bucket_name, object_name)
        print(f"Uploaded {file_path} to S3 bucket {bucket_name} as {object_name}")
    except Exception as e:
        print(f"Failed to upload {file_path}: {e}")

# Function to capture screenshot with timestamp and upload it
def take_screenshot_and_upload(timezone):
    timestamp = datetime.now(timezone).strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_path = f"screenshot_{timestamp}.png"
    screenshot = ImageGrab.grab()
    screenshot.save(screenshot_path)
    print(f"Screenshot taken at {timestamp}")

    # Compress and upload to S3
    compressed_screenshot_path = compress_image(screenshot_path)
    upload_to_s3(compressed_screenshot_path, S3_BUCKET_NAME, f"screenshots/{os.path.basename(compressed_screenshot_path)}")

    # Clean up the local files
    os.remove(screenshot_path)
    os.remove(compressed_screenshot_path)
