import boto3
session = boto3.session.Session(profile_name='default', region_name='us-east-1')
ec2 = session.client('ec2')
response = ec2.run_instances(

    BlockDeviceMappings=[
        {
            'DeviceName': '/dev/xvda',
            'Ebs': {

                'DeleteOnTermination': True,
                'VolumeSize': 8,
                'VolumeType': 'gp2'
            },
        },
    ],
    ImageId= 'ami-026b57f3c383c2eec',
    InstanceType='t2.micro',
    MaxCount=1,
    MinCount=1,
    Monitoring={
        'Enabled': False
    },
   
)
print(response)


# response = instance.stop(
#     Hibernate=True|False,
#     DryRun=True|False,
#     Force=True|False
# )
