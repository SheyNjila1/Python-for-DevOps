import boto3
## To use boto for s3 interaction 
s3 = boto3.client('s3')
response = s3.list_buckets()
# print(response)
## List objects in the bucket
put_boject_response = s3.put_object(Body="G:\\My Drive\\AWS-2022-PROJECTS\\JJTEC-PYTHON\\python-introduction\\avenger.txt", Bucket='gitlab-statefile-shey-hub', Key='avenger.txt')  ## -----> https://stackoverflow.com/questions/40336918/how-to-write-a-file-or-data-to-an-s3-object-using-boto3
print(put_boject_response)

# Upload a file
with open('G:\\My Drive\\AWS-2022-PROJECTS\\JJTEC-PYTHON\\python-introduction\\avenger.txt', 'rb') as data:
    s3.upload_fileobj(data, 'gitlab-statefile-shey-hub', 'avenger-v1.txt')

#Create Bucket
s3.create_bucket(
    Bucket='3ignatius0818',
    
)

print(create_bucket_response)

