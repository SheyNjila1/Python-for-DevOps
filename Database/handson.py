# import mysql.connector  # Import mysql connector ---> use: pip install mysql-connector (https://pypi.org/project/mysql-connector/)

# # mydb = mysql.connector.connect(
# #   host="test-database.ckoxpc5adjwh.us-east-1.rds.amazonaws.com",
# #   user="admin",
# #   password="Admin12345"
# # )
# #print(mydb)
# #Create Database
# mycursor = mydb.cursor()  #Cursor gives control to the variable called mycursor 
# # mycursor.execute("CREATE DATABASE avengers") # Create Database called mydatabase
# # mycursor.execute("SHOW DATABASES") #executes database display
# # for x in mycursor:
# #  print(x)

# ### Create Table
# mydb = mysql.connector.connect(
#   host="test-database.ckoxpc5adjwh.us-east-1.rds.amazonaws.com",
#   user="admin",
#   password="Admin12345",
#   database="NETFLIX"
# )
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
##########################################################################
import mysql.connector

mydb = mysql.connector.connect(
  host="test-database.cgz2br1nzzx8.us-east-1.rds.amazonaws.com",
  user="admin",
  password="Admin12345",
  database="NETFLIX"
)

print(mydb)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE avengers")

# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#     print(x)


#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

## Insert data into table
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)" # Column called Name and another called address
# val = ("John", "Highway 21")  # Values for the name and address respectively
# mycursor.execute(sql, val)  # calling sql and val above 

# mydb.commit()  # commiting the changes into customers table and be persistent(permanent)

# print(mycursor.rowcount, "record inserted.") #rowcount shows how many rows have changed (1), record inserted (2)

## Select
mycursor.execute("SELECT * FROM customers")  # Slect all the rows

myresult = mycursor.fetchall() # Does the job in database already 

for x in myresult: # Only when you want to print in terminal
  print(x)         # Only when you want to display in terminal

