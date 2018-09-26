def beautifulTriplets(d, arr):
  value_dict = {}
  triplets = 0
  
  for index, value in enumerate(arr):
    value_dict[value] = True

  for i in range(len(arr)):
    if arr[i] + d in value_dict and arr[i] + (2 * d) in value_dict:
      triplets += 1
  
  return (triplets)
  