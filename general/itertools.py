from itertools import product
# Generate cartesian products usin product()
a = map(int, input().split())
b = map(int, input().split())

print (*product(a, b))


from itertools import permutations
# Print permutations of a string up to length n
string, length = input().split()
string = sorted(string)
length = int(length)

print (*("".join(x) for x in permutations(string, length)), sep = "\n")


from itertools import combinations
# Print combinations of a string up to length n

string, length = input().split()
string = sorted(string)
length = int(length)

for i in range(1, length + 1):
  for j in combinations(string, i):
    print("".join(j))


from itertools import groupby
# Print groupby representation of a string
for k, v in groupby(input()):
  print((len(list(v)), int(k)), end=" ")
