#https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html
import boto3
session = boto3.session.Session(region_name="us-east-1")
dynamodb = session.resource('dynamodb')
table = dynamodb.Table('JJTechStudents')
def lambda_handler(event, context):
 response = table.put_item(
     Item = {
         "StudentId":"1234",
         "StudentName":"Thor",
         "Age": 22,
         "Country":"US"
     }
 )

 print("Response of item insertion: ", response)
