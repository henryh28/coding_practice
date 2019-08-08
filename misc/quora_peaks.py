# Find maximum height of an array
# Array is strictly ascending, then descending with 1 peak value 
# strictly ascending or descending values are valid input as well

def findPeaks(peaks):
  midpoint = len(peaks)//2
  # found peak
  if len(peaks) <= 3:
    return max(peaks)
  elif peaks[midpoint] < peaks[midpoint+1]:
    # go right
    answer = findPeaks(peaks[midpoint:])
  else:
    # go left
    answer = findPeaks(peaks[:midpoint])

  return (answer)

input1 = [1, 2, 5, 17, 20, 38, 49, 84, 72, 62, 31, 18, 3]
input2 = [4]
input3 = [1,3,5, 7, 9]
input4 = [53, 32, 21,19,3]
input5 = []

print (" ===== reg: ", findPeaks(input1))
print (" ====== 1: ", findPeaks(input2))
print (" ====== asc: ", findPeaks(input3))
print (" ======= des: ", findPeaks(input4))
