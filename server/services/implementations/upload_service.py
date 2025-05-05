import boto3
import uuid
import pathlib
from fastapi import UploadFile
from server.services.interfaces.s3_service import S3Service,AWSRegion


class UploadService(S3Service):
    def __init__(self, region: AWSRegion = AWSRegion.US_EAST_1) -> None:
        self.client = boto3.client("s3", region_name=region) #
        self.BUCKET = 'test'
        self.PREM_PATH =  pathlib.Path('uploads')
        self.PREM_PATH.mkdir(parents=True, exist_ok=True)
    
    def _generate_id():
        return uuid.uuid4()
    
    def _create_bucket():
        pass


    
    async def upload_file_on_prem(self, file:UploadFile) -> str:
        file_id = self._generate_id()
        fname = f'{file_id}_prem_{file.filename}'
        
        
        
        pass
    async def upload_file(self, file:UploadFile) -> str:
        file_id = self._generate_id()
        fname = f'{file_id}_s3_{file.filename}'

        
        pass



    async def download_files(self, group):
        return super().download_files(group)

    async def download_file(self, filename):
        return super().download_file(filename)

    async def remove_file(self, file : str) -> None:
        pass
