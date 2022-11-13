import uuid
import math
import calendar
import os
import json

#print(dir(uuid)) # Unique user identification
#print(uuid.uuid4())
print(math.floor(54.98989797897))
print(calendar.month(2022,10))
print(calendar.weekday(2022,9,13))
print(calendar.isleap(1899))
print(os.getcwd())

file_size = os.path.getsize('movies.txt')
print("File Size is :", file_size, "bytes")

print(json.dumps({'name': 'shey', 'age': 27, 'country': 'India'}))
# https://docs.python.org/3/py-modindex.html
