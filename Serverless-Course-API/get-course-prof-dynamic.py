import boto3


session = boto3.session.Session(region_name="us-east-1",profile_name="default")

dynamodb = session.resource('dynamodb')

table = dynamodb.Table('gloriousdb-course-table')

# print(table.table_name)

# print(table.table_arn)

# print(table.item_count)

# print(table.key_schema)


# items = table.scan()
# print(items)
def lambda_handler(event, context):  # defines function for the get_item; multiple functions can be defined for other attributes 
 print(" event ":, event)
 course = table.get_item(
     Key= {
         "Courseid": "IT100"  # Must appear as on the dynamomoDB table
     }
 )

 print(course['Item'])
