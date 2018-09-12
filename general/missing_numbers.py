def missingNumbers(arr, brr):
  # Make a copy of arr since shouldn't remove elements from it while iterating
  copy_a = list(arr)
  
  for value in copy_a:
    arr.remove(value)
    brr.remove(value)
    
  return (sorted(set(brr)))
