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
