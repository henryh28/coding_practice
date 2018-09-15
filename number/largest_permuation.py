def largestPermutation(k, arr):
  answer = sorted(arr, reverse=True)
  i, j = 0, 0
  largest = max(arr)
  
  if k >= len(arr) - 1:
    return (answer)
  
  while i < k:
    if len(arr[j:]) == 0:
      return (arr)
    
    if arr[j] != largest:
      swap_index = arr.index(largest)
      arr[j], arr[swap_index] = arr[swap_index], arr[j]
      if arr == answer:
        return (answer)
    else:
      i -= 1

    i += 1
    j += 1
    largest -= 1
  return (arr)
  