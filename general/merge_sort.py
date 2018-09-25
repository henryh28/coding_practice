def mergesort(array):
  if len(array) <= 1:
    return (array)

  result = []

  middle = len(array) // 2
  left = mergesort(array[:middle])
  right = mergesort(array[middle:])

  while left and right:
    result.append(left.pop(0) if left [0] < right[0] else right.pop(0))

  result.extend(left if left else mergesort(right))

  return (result)
