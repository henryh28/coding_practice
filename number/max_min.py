def maxMin(k, arr):
  arr.sort()
  lowest_distance = arr[-1]

  for index in range(len(arr) - k + 1):
    temp_distance = arr[index + k - 1] - arr[index]
    
    if temp_distance < lowest_distance:
      lowest_distance = temp_distance
      if lowest_distance == 0:
        return (0)
  
  return (lowest_distance)
  