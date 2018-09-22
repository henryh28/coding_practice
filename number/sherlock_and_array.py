def balancedSums(arr):
  left = 0
  right = sum(arr)
  
  for i in range(len(arr)):
    right -= arr[i]
    
    if left == right:
      return ("YES")
    
    left += arr[i]
    
  return ("NO")
  