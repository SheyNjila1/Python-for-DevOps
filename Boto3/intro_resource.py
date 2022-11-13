import boto3
iam = boto3.resource('iam')
policy_iterator = iam.policies.all()
print(policy_iterator)
for i in policy_iterator:
 if i.policy_name == 'AWSPanoramaFullAccess':
   print(i.policy_name, i.create_date, i.policy_id)
   i.attach_user(
    UserName = 'iamadmin',
   )