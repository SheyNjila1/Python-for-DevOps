fruits = ["kiwi", "watermelon", "grapes", "oranges", "apples"]


for i in fruits:
    print(i)
    if i == "grapes":        
        break


numbers = [1,2,3,4,5]
for i in numbers:
    if i == 4:
        break
    print(i)




results = [False, False, False, True, False, True]

for i in results:
    if i == True:
        continue
    print(i, "all good for boarding")


testing_results = False

if testing_results == False:
    pass

for i in range(18):
    pass

def store_user_details_in_db():
    pass
