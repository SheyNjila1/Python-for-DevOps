# scores = [87,98,67,22,87,23, 90, 90, 60,87, 89, 92, 94,98]
# for marks in scores:
#    print(marks)

#    if marks >= 85 and marks <= 100:
#        print("A")
#    elif marks >= 70 and marks < 85:
#        print("B")
#    elif marks >= 60 and marks <= 70:
#        print("C")
#    elif marks < 60: 
#        print("Failed")
#    else:
#        print("Contact the Staff")

scores = [87,98,67,22,45,87,98,67,22,45,87,98,67,22,45,87,98,67,22,45,87,98,67,22,45]

for marks in scores:
    print(marks)
    if marks >= 85 and marks <= 100:
        print('A')
    elif marks >= 70 and marks < 85:
        print("B")
    elif marks >=60 and marks < 70:
        print("C")    
    elif marks < 60:
        print("Failed")
    else:
        print("Contact the staff")

