# Sets
###Sets used when order is not important and no duplications guaranteed
###Order is guranteed in a list

playlist1 = {"album1", "album2", "album3", "album4", "album1"}

playlist2 = {"album3", "album6", "album7", "album103" }

# Using union ----> Combine two sets without duplication 
print(playlist1.union(playlist2))
print(playlist1.intersection(playlist2))
print(playlist1.difference(playlist2))