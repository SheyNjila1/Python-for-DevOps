# # Nested List of Students
# students = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12],
#     [13,14,15,16],
# ]

# for i in students:  ## Iteration through lists and not individual students
#  print(i)

# Now using nested index approache, we do thw following:

# Nested List of Students
students = [ [1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16], ["Oliver", "Shey", "Njila"]]

for i in students:  # Iteration through lists and not individual students
 for j in i:        # i is list and j is individual student(value)
  print(j) # Will print all values from the different lists
# With nested loops, two loops are used



