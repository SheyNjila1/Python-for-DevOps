import requests  # Install the requests module if not available-----> pip install requests

# print(dir(requests))


# response = requests.get("https://reqres.in/api/users/")
# #print(response)
# print("ResonseCode: ", response)
# print("Response: ", response.json())

# response = requests.get("https://reqres.in/api/users/3")
# #print(response)
# print("ResonseCode: ", response)
# print("Response: ", response.json())

# response = requests.post("https://reqres.in/api/users/", json={
#  "name": "ironman",
#  "job": "leader"
# })
# #print(response)
# print("ResonseCode: ", response)
# print("Response: ", response.json())

# def get_all_users():
#  print("Getting all users .....")
#  response = requests.get("https://reqres.in/api/users/")
#  print(response)
#  print("ResonseCode: ", response)
#  print("Response: ", response.json())
#  return response.json()

# get_all_users()
## Avoiding hardcoding
# def get_all_users(user_id):
#     print("Getting all users .....")
#     response = requests.get("https://reqres.in/api/users/" + user_id)
#     print(response)
#     print("ResonseCode: ", response)
#     print("Response: ", response.json())
#     return response.json()
# get_user("2")
# get_user("4")
# get_user("10")

# def create_user(user_data):
#     print("Creating a new user with details... .....", user_data)
#     response = requests.get("https://reqres.in/api/users/", json= user_data)
#     print("ResonseCode: ", response)
#     print("Response: ",response.json())
#     return response.json()
# create_user({
#  "name": "morpheus",
#  "job": "leader"
# })

# def create_user(user_data):
#     print("Creating a new user with details... .....", user_data)
#     response = requests.get("https://reqres.in/api/users/", json= user_data)
#     print("ResonseCode: ", response)
#     print("Response: ",response.json())
#     return response.json()
# # create_user({
# #  "name": "morpheus",
# #  "job": "leader"
# # })


response = requests.get("https://developers.google.com/apis-explorer/3")
#print(response)
print("ResonseCode: ", response)
print("Response: ", response.json())