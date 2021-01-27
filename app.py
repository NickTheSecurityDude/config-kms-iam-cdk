#!/usr/bin/env python3

###################################################################
#
# 1. IAM Stack
#
# 2. Lambda Stack
#   - config_kms_iam_policy_checker.py
# 
# 3. Config Stack
# 
###################################################################

from aws_cdk import core

import boto3
import sys

client = boto3.client('sts')
region=client.meta.region_name

"""
if region != 'us-east-1':
  print("This app may only be run from us-east-1")
  sys.exit()
"""

account_id = client.get_caller_identity()["Account"]

my_env = {'region': region, 'account': account_id}

from stacks.iam_stack import IAMStack
from stacks.lambda_stack import LambdaStack
from stacks.config_stack import ConfigStack

proj_name="config-kms-iam"

app = core.App()

iam_stack=IAMStack(app, proj_name+"-iam",env=my_env)
lambda_stack=LambdaStack(app, proj_name+"-lambda",
  config_kms_iam_lambda_role=iam_stack.config_kms_iam_lambda_role
)
config_stack=ConfigStack(app,proj_name+"-config",
  config_kms_iam_checker_function=lambda_stack.config_kms_iam_checker_function
  )

app.synth()
