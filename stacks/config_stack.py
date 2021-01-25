##############################################################
#
# config_stack.py
#
# Resources:
#   KMS with IAM custom Config rule
#
##############################################################

from aws_cdk import (
  aws_config as config,
  aws_lambda as lambda_,
  core
)

class ConfigStack(core.Stack):

  def __init__(self, scope: core.Construct, construct_id: str, config_kms_iam_checker_function: lambda_.IFunction, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)

    config.CustomRule(self,"KMS With IAM Config Rule",
      config_rule_name="kms-key-with-iam-access",
      lambda_function=config_kms_iam_checker_function,
      configuration_changes=True,
      periodic=True,
      maximum_execution_frequency=config.MaximumExecutionFrequency.TWENTY_FOUR_HOURS,
      rule_scope=config.RuleScope.from_resources([
        config.ResourceType.KMS_KEY
      ])
    )