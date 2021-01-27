# config-kms-iam-rule-cdk

## Detect customer manged keys which allow IAM User access

Howto Install:  
If needed, export your AWS profile:  
`export AWS_PROFILE=profile_name`

Create a virtual environment and launch the stacks:  
```
python3 -m venv .venv  
source .venv/bin/activate   
python3 -m pip install -r requirements.txt  
cdk bootstrap aws://<account-id>/<region>  
cdk synth   
cdk deploy --all
```

## Notes

- Enable config in the account and region before use  
- The config role will need to have permission on the key in order to confirm its "compliant"
(non-compliant keys will be detected either way)  
- To debug the lambda function set this variable to 1 on/around line 81:  
DEBUG=1

(c) Copyright 2021 - NickTheSecurityDude

Disclaimer:  
For informational/educational purposes only.  Bugs are likely and can be reported on github.  
Using this will incur AWS charges.

