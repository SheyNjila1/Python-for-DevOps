import boto3

def list_all_s3_buckets():
    print("listing all the buckets")
    s3_resouce = boto3.resource("s3")
    s3_resouce.buckets.all()
    for bucket in s3_resouce.buckets.all():
     print(bucket.name)


