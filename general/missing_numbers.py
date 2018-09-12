def missingNumbers(arr, brr):
  copy_a = list(arr)
  
  for value in copy_a:
    arr.remove(value)
    brr.remove(value)
    
  return (sorted(set(brr)))
