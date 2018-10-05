from collections import OrderedDict
words = OrderedDict()

for i in range(int(input())):
  word = input()
  words[word] = 1 if word not in words else words[word] + 1

print(len(words))

for key, val in words.items():
  print(val, end=" ")
  
