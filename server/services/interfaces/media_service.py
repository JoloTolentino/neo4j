from abc import ABC, abstractmethod
import enum


class AWSRegion(str, enum.Enum):
    US_EAST_1 = "us-east-1"
    US_WEST_2 = "us-west-2"
    EU_CENTRAL_1 = "eu-central-1"



class MediaService(ABC):
    @abstractmethod
    def upload_file(self, file):
        'given a file, the services uploads it localy or to the cloud'

    @abstractmethod
    def download_file(self, filename):
        'given a filename provides the file associated with the filename'

    @abstractmethod
    def download_files(self, group):
        'given a file group, returns all the '

    @abstractmethod
    def update_status(self, job_id): 
        'update'