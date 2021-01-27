##############################################################
#
# lambda_stack.py
#
# Resources:
#  1 lambda function (code in /lambda folder (from_asset))
#
##############################################################

from aws_cdk import (
  aws_iam as iam,
  aws_lambda as lambda_,
  core
)

class LambdaStack(core.Stack):

  def __init__(self, scope: core.Construct, construct_id: str, config_kms_iam_lambda_role: iam.IRole, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)

    # get acct id for policies
    #acct_id=env['account']

    # create the config KMS IAM checker Lambda function
    self._config_kms_iam_checker=lambda_.Function(self,"Config KMS IAM Lambda Func",
      code=lambda_.Code.from_asset("lambda/config_kms_iam_checker.zip"),
      handler="config_kms_iam_checker.lambda_handler",
      runtime=lambda_.Runtime.PYTHON_3_8,
      role=config_kms_iam_lambda_role,
      timeout=core.Duration.seconds(60)
    )

  # Exports
  @property
  def config_kms_iam_checker_function(self) -> lambda_.IFunction:
    return self._config_kms_iam_checker




