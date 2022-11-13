# Another example regarding 'args'
def total(*args):
 total = 0
 for i in args:
  total += i
 return total
print('The total of the numbers is', total(0.577, 2.718, 3.14, 1.618, 1729, 6, 37))