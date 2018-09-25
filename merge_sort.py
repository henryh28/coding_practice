def mergesort(array):
  result = []

  if len(array) <= 1:
    return array

  middle = len(array) // 2
  left = mergesort(array[:middle])
  right = mergesort(array[middle:])

  while len(left) > 0 and len(right) > 0:
    if left[0] < right[0]:
      result.append(left.pop(0))
    else:
      result.append(right.pop(0))

  if len(left) > 0:
    result.extend(left)
  else:
    result.extend(mergesort(right))

  return (result)


temp = [1, 3, 2, 6, 4, 3, 9, 2, 5]
temp2 = ["b", "d", "k", "c", "z", "a"]


new = mergesort(temp)
print(new)

new2 = mergesort(temp2)
print(new2)
