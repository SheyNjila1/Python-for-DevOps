# Use case: Get course(item) from DynamoDB table created
import boto3
dynamodb = boto3.session.Session(region_name="us-east-1",profile_name="default")
# go to Boto3 DynamoDB documentation > Service Resource: Modified as above to include profile and region in Session Object
dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('gloriousdb-course-table')  # from boto3 documentation: The following attributes
# print(table.table_name)
# print(table.table_arn)
# print(table.item_count)
# print(table.key_schema)
# items = table.scan()
# print(items)
course = table.get_item()
Key= {
      'Courseid': 'IT100'
  }
print(course)

