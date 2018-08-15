
def maxMin(k, arr):
  arr = sorted(arr)
  smallest = arr[-1]
  
  for i in range(len(arr) - (k - 1)):
    minimum = arr[i]
    maximum = arr[i + k - 1]
    difference = maximum - minimum
    smallest = min(difference, smallest)

    if smallest == 0:
      return (smallest)
  
  return (smallest)
  