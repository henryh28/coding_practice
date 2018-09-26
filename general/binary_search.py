def binarySearch(array, value, index = 0):
  if len(array) <= 0 or len(array) == 1 and array[0] != value:
    return (-1)

  middle = len(array) // 2

  if array[middle] == value:
    return (middle + index)

  if value < array[middle]:
    return (binarySearch(array[:middle], value, index))
  else:
    return (binarySearch(array[middle:], value, index + len(array[middle:])))

''' Tests
data = [1, 3, 4, 5, 7, 12, 18, 21, 23, 25, 30, 32, 34, 42, 47, 50]

target = 100
answer=binarySearch(data, target)
print(" ** index is: ", answer)
print(target == data[answer])

for i in range(len(data)):
  target = data[i]
  print("===========================")
  print("target is: ", target)
  answer = binarySearch(data, target)
  print(" ** index is: ", answer)
  print(target == data[answer])
'''
