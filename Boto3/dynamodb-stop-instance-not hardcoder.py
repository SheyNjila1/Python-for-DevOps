import boto3
session = boto3.session.Session(region_name = 'us-east-1')
ec2 = session.resource('ec2')
def lambda_handler(event, context):
    # Get only running instances
    instances = ec2.instances.filter(
        Filters=[{'Name': 'instance-state-name',
                    'Values': ['running']}])
    # Stop the instances
    for instance in instances:
        instance.stop()
        print('Stopped instance: ', instance.id)