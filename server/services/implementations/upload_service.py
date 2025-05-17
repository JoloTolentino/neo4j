from pathlib import Path
from fastapi import UploadFile
from botocore.exceptions import ClientError
from server.services.interfaces.media_service import MediaService, AWSRegion
from server.schemas.aws import S3Response
import boto3
import uuid
import os 
import botocore
import asyncio



class UploadService(MediaService):
    def __init__(self, region: AWSRegion = AWSRegion.US_EAST_1) -> None:
        self.client = boto3.client("s3", region_name=region)
        self.BUCKET = "jolo-test-bucket"
        self.PREM_PATH = Path("uploads")
        self.PREM_PATH.mkdir(parents=True, exist_ok=True)
        #1024* 1024 = 1 million bytes therefore 1MB
        self.MAX_CHUNK = 5*1024*1024 
        if not self.bucket_exists():
            self._create_bucket()


    def bucket_exists(self) -> bool:
        try:
            self.client.head_bucket(Bucket=self.BUCKET)
            return True  # Bucket exists and is accessible
        except botocore.exceptions.ClientError as e:
            error_code = int(e.response['Error']['Code'])
            if error_code == 404:
                return False  
            else:
                raise e  


    def _generate_id(self) -> uuid:
        return uuid.uuid4()

    def _create_bucket(self) -> None:
        self.client.create_bucket(
            Bucket = self.BUCKET
        )
    def _upload_s3(self, file:UploadFile, path:str) -> bool: 
        try:
            self.client.upload_fileobj(file.file,self.BUCKET,path)
            return True
        except Exception as e:
            print(e) # need to log
            return False
        
    async def _upload_large_file_s3(self, file:UploadFile, path:str) -> S3Response:
        '''
        triggers a webhook sns response
        
        '''
        response = self.client.create_multipart_upload(Bucket=self.BUCKET, 
                                                       Key=path)
        upload_id = response['UploadId']
        parts = [] # aws requires that
        part_id = 1 
        try: 
            while True: 
                # reads 5mb worth of data incremently 
                chunk = await file.read(self.MAX_CHUNK)
                if not chunk:
                    break 
                response = await asyncio.to_thread(
                    self.client.upload_part,
                    Bucket = self.BUCKET,
                    Key = path,
                    PartNumber = part_id,
                    Body = chunk
                )
                parts.append({
                    'ETag':response['ETag'],
                    'PartNumber': part_id
                })

                response = await asyncio.to_thread(
                    self.client.complete_multipart_upload,
                    Bucket = self.BUCKET,
                    UploadId = upload_id,
                    Key = file.name,
                    MultipartUpload = {
                        'Parts':parts
                    }
                )
                return {
                    'url': response['url']
                }

        except ClientError as err: 
            raise ClientError(f'')




    async def upload_file_on_prem(self, file: UploadFile) -> str:
        file_id = self._generate_id()
        fname = "".join(f"{file_id}_prem_{file.filename}".split())
        

        pass

    async def upload_file(self, file: UploadFile) -> str:
        '''
        Generates a unique id for uploads
        '''
        file_id = self._generate_id()
        fname = "".join(f"{file_id}_s3_{file.filename}".strip().split())    
        save_path = 'fastapi/uploads/'
        path = os.path.join(save_path,fname)
        success = await asyncio.to_thread(self._upload_s3,file,path)
        if not success:
            raise Exception(f'failed to upload to s3: {file.filename}')
        url = f"https://{self.BUCKET}.s3.{self.client.meta.region_name}.amazonaws.com/{path}"
        return url
        

    async def download_files(self, group):
        return super().download_files(group)

    async def download_file(self, filename):
        return super().download_file(filename)

    async def remove_file(self, file: str) -> None:
        pass
