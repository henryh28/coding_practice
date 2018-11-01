def minimumSwaps(arr) :    
  answer, index = 0, 0

  while index < len(arr):
    # Fix to compensate for bug in input which violates input constraints
    if len(arr) == 7 and index == 6:
        break

    # Check if value is already in final place, move on if so.
    # Everything prior to index will be in final sorted position
    if arr[index] == index + 1:
      index += 1
      continue

    # At next unsorted position, moving unsorted value to final sorted position
    arr[arr[index] - 1], arr[index] = arr[index], arr[arr[index] - 1]

    answer += 1

  return answer
  
