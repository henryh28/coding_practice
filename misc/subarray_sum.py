#
# Complete the 'subarraySum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def subarraySum(arr):
  answer_value = 0
  size = len(arr)
  
  for i in range(1, size):
    for j in range(size):
        if j + i <= size:
          # Line 28 is causing the time out failure, because I'm making a slice of 
          # a potentially very, very large array, which is computationally expensive
          # Fix is to pre-compute the value so that I don't need to make slices of a 
          # very large array per iteration.
          answer_value += sum(arr[j:j + i])
  
  answer_value += sum(arr)
  return (answer_value)
