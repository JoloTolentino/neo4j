from abc import ABC, abstractmethod
import enum


class AWSRegion(str, enum.Enum):
    US_EAST_1 = "us-east-1"
    US_WEST_2 = "us-west-2"
    EU_CENTRAL_1 = "eu-central-1"


class S3Service(ABC):
    @abstractmethod
    def upload_file(self, file):
        pass

    @abstractmethod
    def download_file(self, filename):
        pass

    @abstractmethod
    def download_files(self, group):
        pass
