##############################################################
#
# iam_stack.py
#
# Resources:
#   Lambda Execution Role
#
# Exports:
#  config_kms_iam_lambda_role
#
##############################################################

from aws_cdk import (
  aws_iam as iam,
  core
)

class IAMStack(core.Stack):

  def __init__(self, scope: core.Construct, construct_id: str, env, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)

    # get acct id for policies
    # acct_id=env['account']
    region=env['region']

    # create lambda execution role, use same role for both lambdas
    self._config_kms_iam_lambda_role=iam.Role(self,"KMS With IAM Lambda Role",
      role_name="Config_KMS_IAM_Lambda_Execution_Role-"+region,
      assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
      inline_policies=[iam.PolicyDocument(
        statements=[iam.PolicyStatement(
          actions=[
            "kms:ListKeys",
            "kms:GetKeyPolicy",
            "kms:DescribeKey"
          ],
          effect=iam.Effect.ALLOW,
          resources=["*"]
        )]
      )],
      managed_policies=[
        iam.ManagedPolicy.from_aws_managed_policy_name('job-function/ViewOnlyAccess'),
        iam.ManagedPolicy.from_aws_managed_policy_name('service-role/AWSLambdaBasicExecutionRole'),
        iam.ManagedPolicy.from_aws_managed_policy_name('service-role/AWSConfigRulesExecutionRole')
      ]
    ).without_policy_updates()

  # Exports
  @property
  def config_kms_iam_lambda_role(self) -> iam.IRole:
    return self._config_kms_iam_lambda_role