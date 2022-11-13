# #list of mobile phones
mobiles = ["apple", "samsung", "lg", "blackberry", "oneplace"]
print(type([]))
print(type(mobiles))
print(mobiles)
print(len(mobiles))
for item in mobiles:
      print(item)

print(mobiles[3])

# #replacing and item
mobiles[2] = "nokia"
print (mobiles)  
#lg replaced by nokia --->['apply', 'samsung', 'nokia', 'blackberry', 'oneplace']
# The dir functions
#print(dir(mobiles))

##Using functions from dir
# #Append item to existing list
# ['apply', 'samsung', 'nokia', 'blackberry', 'oneplace'].append("google pixel")
mobiles.append("google pixel")
# print(mobiles)

## Copy function
new_mobile_phones = mobiles.copy()
print(new_mobile_phones)

##pop --->remove the value in index 2
mobiles.pop(2)
print(mobiles)

### Resource ---> https://www.programiz.com/python-programming/methods/list/pop#:~:text=Python%20List%20pop%20%28%29%201%20pop%20%28%29%20parameters.,without%20an%20index%2C%20and%20for%20negative%20indices.%20

####CREATE A NEW LIST
a = []  # decalring a variable of empty list
a = list() #using the list function to describe list
print(type(a))

#####TUPLES:
#### USE TUPLES WHEN YOU DO NOT WANT THE DATA TO BE CHANGE
traffic_symbols = ("red", "green", "yellow")

print(traffic_symbols)
#traffic_symbols[1] = "white"

covid_rules = ("wear mask", "maintain 1.5 meter distance")
# Using the count variable:
print(traffic_symbols.count("red"))
print(len(traffic_symbols))

### Additioanal colors can be added to the list of colors and not tuples
colors = ["red", "green", "yellow"]
colors.append("white")
print(colors)


