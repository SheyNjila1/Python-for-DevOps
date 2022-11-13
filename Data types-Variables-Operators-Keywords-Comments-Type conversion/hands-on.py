from re import X


math = 78
science = 34
passing_score = 35

# they have to pass both math and science, otherwise they fail

if math >= passing_score and science >= passing_score:
 print('test passed')
else:
 print('test failed')


# Iteration
fruits = ["watermelon", "grapes", "orange"]
print("grapes" in fruits)

name = "jjtech"
print("tech" in name)

name = "jjtech"
print("x" in name)

print(1+2.5)
age = 43.5
new_age = int(age)
print(age)
print(new_age)

# ___#############################___
# price = 10
# quantity = 2
# total = price*quantity
# print("Total amount to be paid: ", total) #This will describe what the value stands for

# use the in put concept
# price = 2
# quantity = int(input("How many items? "))
# customer_name = "Shey"
# print(type(quantity))
# total = price * int(quantity)
# # This will describe what the value stands for
# print("Total amount to be paid: ", total)

# quantity = quantity + 2
# total = price * quantity
# print("Total amount to be paid: ", total)
# print("Total to be paid: ",) total, "name: ", customer_name, "price: ", price, "quantity: ", quantity)
# # OR


#####################################################################---FINAL CODE:
price = 2
quantity = int(input("How many items? "))
customer_name = "vamsi"

print(type(quantity))

total = price * quantity

print("Total amount to be paid: ", total)

quantity = quantity + 2

total = price * quantity

print("Total amount to be paid: $", total, "name: ",
      customer_name, "price: ", price, "quantity: ", quantity)

print("Total amount to be paid: ${}, customer name: {}, price: {}, quantity: {}".format(
    total, customer_name, price, quantity))

