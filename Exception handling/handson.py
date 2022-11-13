f=open("movies.txt", "r") # open the file and execute in x mode, movies.txt will be created

# print(dir(f)) # Give output of different funftion 

# f.write(" Hi there, we We aare from JJtech \n") 
# f.write("And its Monday . anothe python class")
print(f.readlines(2))
f.close()
