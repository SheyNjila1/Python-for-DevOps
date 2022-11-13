import boto3

session = boto3.session.Session(profile_name="default", region_name= "us-east-1")

ec2 = session.client('ec2')

volumes = ec2.describe_volumes(
    Filters=[
        {
            'Name': 'status',
            'Values': [
                'available',
            ]
        },
    ],
)

print("Available volumes: ", volumes)

for i in volumes["Volumes"]:
    print("Current EBS volume: ", i["VolumeId"])
    delete_response = ec2.delete_volume(
        VolumeId = i["VolumeId"]
    )
    print("Volume delete operation response: ", delete_response)
