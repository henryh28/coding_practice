def quicksort(array):
  if len(array) <= 1:
    return (array)

  # Set pivot to last element of list
  pivot = array[-1]
  lesser, greater = [], []

  for value in array[:-1]:
    lesser.append(value) if value < pivot else greater.append(value)

  result = quicksort(lesser)
  result.append(pivot)
  result.extend(quicksort(greater))

  return (result)
  