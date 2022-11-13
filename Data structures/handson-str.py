name = "iron man"
print(len(name))
print(name[2])

print("iron" in name)
print(name.upper())  # converts every character to Upper case
print(name.replace("iron", "copper")) # replace iron with copper

#Strip function
user_name = " shey "
print(len(user_name))
print(user_name.strip())

company = "jj tech"
print(company.upper())  # Prints upper case
print(company) # Prints lower case 

# for Permanent change
job = "Senior Cloud Engineer"
job = job.upper()
print(job)

## Split
# email = "shey.njila@sheytechno"
# data = email.split("@")  # Split at @ and store the resulat in the variable "data"
# print(data)  #Output------>['shey.njila', 'sheytechno']--> this is a list 
# print(data[1].split('.')[0])  # isolate sheytecno  -->Output is sheytechno

# #another example
email = "vamsi.krishana@jjtech.com"
data = email.split("@")
print(data)

company_domain = data[1]
print(company_domain)

new_data = company_domain.split('.')
print(new_data)

final_data = new_data[0]

print(final_data)

print(email.split("@")[1].split(".")[0])


