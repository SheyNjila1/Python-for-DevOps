pin_count = 0

while pin_count <= 5:
    pin_entered = False
    if pin_entered == False:
        pin_count = pin_count + 1
        if pin_count <=5:
            print("Please enter your pin again")
        else:
            print("Pin got blocked, try after 5 minutes")