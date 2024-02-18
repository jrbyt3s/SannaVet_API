from django.conf import settings
from boto3 import client


class Bucket:
    def __init__(self, name, folder):
        self.name = name
        self.folder = folder
        self.region = settings.AWS_REGION
        self.access_id = settings.AWS_ACCESS_KEY_ID
        self.access_secret = settings.AWS_ACCESS_KEY_SECRET

        self.client = client(
            's3',
            region_name=self.region,
            aws_access_key_id=self.access_id,
            aws_secret_access_key=self.access_secret
        )

        self.__url = f'https://{self.name}.s3.{self.region}.amazonaws.com'

    def upload_object(self, filename, stream):
        try:
            object_folder = f'{self.folder}/{filename}'
            self.client.upload_fileobj(
                stream, self.name, object_folder,
                ExtraArgs={'ACL': 'public-read'}
            )
            return f'{self.__url}/{object_folder}'
        except Exception as e:
            raise Exception(f'Bucket error -> {str(e)}')
