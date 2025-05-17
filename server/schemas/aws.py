from pydantic import BaseModel, HttpUrl, Field
from typing import Optional, Union


class AWSResponse(BaseModel):
    """
    Base response schema for AWS-related services.
    Provides a standard HTTP-style response code field.
    """
    code: int = Field(..., description="Status code representing the outcome of the AWS operation.")


class S3Response(AWSResponse):
    """
    Response schema for S3 file upload or access.
    Includes pre-signed URL, optional message, and ETag identifier.
    """
    presigned_url: Optional[HttpUrl] = Field(
        None,
        description="Pre-signed URL for temporary S3 file access."
    )
    msg: Optional[str] = Field(
        None,
        description="Optional human-readable message about the upload status or result."
    )
    etag_number: Optional[Union[int, str]] = Field(
        None,
        description="Entity tag (ETag) returned by S3 for identifying the uploaded object version."
    )


class LambdaResponse(AWSResponse):
    """
    Response schema for AWS Lambda executions.
    Includes the result of the function and optionally any captured logs.
    """
    result: Optional[str] = Field(
        None,
        description="Output result returned from the Lambda function execution."
    )
    logs: Optional[str] = Field(
        None,
        description="Optional log output captured during Lambda execution."
    )


class SNSResponse(AWSResponse):
    """
    Response schema for AWS SNS notifications.
    Indicates whether a notification was successfully dispatched.
    """
    notified: Optional[str] = Field(
        None,
        description="Indicates the result of the notification dispatch (e.g., 'Success', 'Failed')."
    )
