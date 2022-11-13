
# try:
#     print("Hey SHey")
#     marks = 95
#     print(marks/0)
# except Exception as e:
#  print("unexpected issue", e)
    
# print("unexpected issue")
# print("JJTech")
# print("learning python")
# print("Completed!!!!")

## SCenario
# def add(number1, number2):
#  total = number1 + number2
#  return total 
# result = add(10,2000)
# print(result)

# print("Hiiiii, there")
# print("JJTech")

#SCe
# def add(number1, number2):
#  try:
#      total = number1 + number2
#      return total 
#  except Exception as e:
#     print(e)
# result = add(10,"shey")
# print(result)

# print("Hiiiii, there")
# print("JJTech")

##SCe
try:
   f = open("jjtech-students.txt", "r")
   print(f.read())
except Exception as e:
   print(e)
   f = open("jjtech-students.txt", "x")
   f.close()
print("hellllllllllllloooooo")  # File is created