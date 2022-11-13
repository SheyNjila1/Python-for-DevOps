def validate_account_number(account_number):
    print(account_number, "is valid")

validate_account_number(235879628576778)
validate_account_number(56456464564645)
validate_account_number(3456656456456)
validate_account_number(5454645645645646)

def check_number(number):
    if number <0:
        print('negative')
    elif number > 0:
        print('positive')
    else:
        print('zero')

check_number(10)
check_number(-6)
check_number(0)


def calculate_bmi(height, weight):
    bmi = ((weight/height)/height) * 1000
    print(bmi)

calculate_bmi(176, 72)
calculate_bmi(136, 56)
calculate_bmi(126, 34)
calculate_bmi(164, 34)
calculate_bmi(134, 54)


def greet(name):
    print("Hi ", name)

greet("vamsi")