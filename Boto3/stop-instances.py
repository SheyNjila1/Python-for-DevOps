# code to stop instances [First get the instances and that are running and then stop them]
import boto3

session = boto3.session.Session(region_name = 'us-east-1')

ec2 = boto3.resource('ec2')


# Get only running instances
instances = ec2.instances.filter(
	Filters=[{'Name': 'instance-state-name',
				'Values': ['running']}])

# Stop the instances
for instance in instances:
	instance.stop()
	print('Stopped instance: ', instance.id)






