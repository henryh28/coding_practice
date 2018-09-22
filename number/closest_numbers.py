# Complete the closestNumbers function below.
def closestNumbers(arr):
  answers = []
  lowest = max(arr)
  arr.sort()
  
  for i in range(1, len(arr)):
    difference = arr[i] - arr[i - 1]
    
    if difference < lowest:
      lowest = difference
      answers = []
      
    if difference <= lowest:
      answers.append(arr[i - 1])
      answers.append(arr[i])

  return (answers)
  