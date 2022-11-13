# print("hi")
# print("jjetech")
# print("python")

# def add(num1, num2):
#  print(num1+num2)


# add(200, 30450)
# add(200, 322200)
# add(206360, 36600)
# add(20040, 34500)

# def check_balance(account_number):
#  print("connecting to the DB")
#  print("checking the balance for the account: ", account_number)
#  print("current balance for the account: ", account_number, "is ", 1000)
# check_balance(123456789)
# check_balance(123455556789)
# check_balance(12378456789)


# def send_money(senders_account, receivers_account, transfer_amount):
#  print("In method send_money, details are senders account": ", senders_account, "receivers account, "amount to send: ", transfer_amount)
#  check_balance(senders_account)
# send_money(65656546,5545464,100)

import util
def check_balance(account_number):
 db_secrets = util.get_db_credentials_param("rds-credentials")
 print(db_secrets)
 # print("connecting to the DB")
 # print("checking the balance for the account: ", account_number)
 # print("current balance for the account: ", account_number, "is ", 1000)
 # print("")
 # return 1000



