import pathlib
import boto3

from lib.currency import get_currency

AWS_REGION = "eu-west-3"
S3_BUCKET_NAME = "stas346"

resource = boto3.resource("s3", region_name=AWS_REGION)
iterator = resource.buckets.all()
print("Listing Amazon S3 Buckets:")
for bucket in iterator:
    print(f"-- {bucket.name}")

URL = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
get_currency(URL)



# BASE_DIR = pathlib.Path(__file__).parent.resolve()
# x = r'C:\Users\Admin\Desktop\Stas\CI-CD\start.py'


# s3_client = boto3.client("s3", region_name=AWS_REGION)

# def upload_files(file_name, bucket, object_name=None, args=None):
#     if object_name is None:
#         object_name = file_name

#     s3_client.upload_file(file_name, bucket, object_name, ExtraArgs=args)
#     print(f"'{file_name}' has been uploaded to '{S3_BUCKET_NAME}'")

# # upload_files(f"{BASE_DIR}\\demo.txt", S3_BUCKET_NAME)

# upload_files(x,S3_BUCKET_NAME ,'start.py')


""""Upload file on bucket """

BASE_DIR = pathlib.Path(__file__).parent.resolve()
x = r'.\\currency.txt'


s3_client = boto3.client("s3", region_name=AWS_REGION)

def upload_files(file_name, bucket, object_name=None, args=None):
    if object_name is None:
        object_name = file_name

    s3_client.upload_file(file_name, bucket, object_name, ExtraArgs=args)
    print(f"'{file_name}' has been uploaded to '{S3_BUCKET_NAME}'")
  
upload_files(x,S3_BUCKET_NAME ,'currency.txt')
