def countTriplets(arr, r):
  from collections import defaultdict

  # Sets default value to 0 so that incomplete triplets will be multiplied by zero
  second = defaultdict(int)
  third = defaultdict(int)
  answer = 0

  for value in arr:
    answer += third[value]
    third[value * r] += second[value] # completes triplets based on existing valid values from second
    second[value * r] += 1            # adds 1 to count of how many triplets (value * r) would satisfy

  return answer  
