# # File to copy objects from the source to the destination bucket ---->https://stackoverflow.com/questions/59949299/how-to-copy-files-and-folders-from-one-s3-bucket-to-another-s3-using-python-boto
# import boto3
# session = boto3.session.Session(profile_name='default', region_name='us-east-1')
# client = session.client('s3')
# ## client.copy_object(Bucket="BucketName", CopySource="BucketName/OriginalName", Key="NewName")
# # response = client.copy_object(Bucket="destination-bucket-shey", CopySource="lambdashey/main.tf", Key="main.tf")
# # print(response)

# # List objects in a bucket
# bucket_objects = client.list_objects_v2(

#     Bucket='shey-gitlab-cicd-bucket-final',
# )
# for i in bucket_objects['Contents']:
#  print(i)
# # # copy all the objects/multiple objects 
# # response = client.copy_object(Bucket="destination-bucket-shey", CopySource="lambdashey/main.tf", Key="main.tf")
# # print(response)


###################################
import boto3

session = boto3.session.Session(profile_name="default", region_name="us-east-1")

client = session.client('s3')

SOURCE_BUCKET = ''
DESTINATION_BUCKET = ''

bucket_objects = client.list_objects_v2(
    Bucket='shey-gitlab-cicd-bucket-final'
)

for i in bucket_objects['Contents']:
    print(i['Key'])
    response = client.copy_object(Bucket="destination-bucket-shey", CopySource="shey-gitlab-cicd-bucket-final/"+ i["Key"], Key=i["Key"])
    print(response)

