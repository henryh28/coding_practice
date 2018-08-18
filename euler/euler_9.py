'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
found = False

for a in range(100, 500):
  for b in range(a + 1, 501):
    c = (a**2 + b**2) ** 0.5
    
    if a + b + c == 1000:
      print ("a: {}, b: {}, c: {}. = {}".format(a, b, c, a * b * c))
      found = True
      break

  if found == True:
    break
