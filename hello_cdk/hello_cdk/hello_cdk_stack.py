from aws_cdk import (
  Stack,
  aws_lambda as _lambda, # Import the Lambda module
  CfnOutput, # Import CfnOutput
  aws_s3 as s3
)
from constructs import Construct

class HelloCdkStack(Stack):

  def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)

    self.bucket = s3.Bucket(
            self,
            "Bucket",
            versioned=True
        )
