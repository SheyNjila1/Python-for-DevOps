phone = {"name": "phone", "price": 1000, "color": "grey", "camera": 128, "storage": 128 }

print(phone)
print(type(phone))
print(phone["price"])
print(phone["name"])

phone["price"] = 1500 # CHange phone price to 1500

print(phone) # The output will show 1500 instead of 1000
phone["storage"] = 256
print(phone)
phone["year"] = 2022 # Add a new key and key-value
print(phone)
print(phone.keys())
print(phone.values())
print(phone.clear())

###############OUTPUT#####

# phone
# {'name': 'phone', 'price': 1500, 'color': 'grey', 'camera': 128, 'storage': 128}
# {'name': 'phone', 'price': 1500, 'color': 'grey', 'camera': 128, 'storage': 256}
# {'name': 'phone', 'price': 1500, 'color': 'grey', 'camera': 128, 'storage': 256, 'year': 2022}

# What is there are many phones-----> List of DIctionaries

all_phones = [
            {"name": "iphone", "price": 1000, "color": "56", "camera": 128},
            {"name": "samsung", "price": 56, "color": "546", "camera": 655},
            {"name": "sdsf", "price": 1006540, "color": "56", "camera": 546},
            {"name": "fsdf", "price": 45, "color": "546", "camera": 128},
            {"name": "sdf", "price": 56, "color": "grey", "camera": 12546568},
            {"name": "sdfsd", "price": 56, "color": "546", "camera": 56}
]
print(all_phones)

MLB_team = dict([
    ('Colorado', 'Rockies'),
    ('Boston', 'Red Sox'),
    ('Minnesota', 'Twins'),
    ('Milwaukee', 'Brewers'),
    ('Seattle', 'Mariners')
])

print(MLB_team)