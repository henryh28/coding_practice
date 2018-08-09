def isValid(s):
  letters = {}
  
  for char in s:
    letters[char] = letters[char] + 1 if char in letters else 1

  # Convert dictionary to a set
  array = list(letters.values())
  letter_set = set(letters.values())
  array.sort()

  maximum = array[-1]
  minimum = array[0]

  # 3 or more different values, auto fail
  if len(letter_set) >= 3:
    return "NO"

  # if there are exactly 2 different frequencies
  if len(letter_set) == 2:
    min_count = max_count = 0

    for value in array:
      if value == array[0]:
        min_count += 1
      else:
        max_count += 1

    # 2+ of each different frequency, can only drop 1 and not enough
    if min_count > 1 and max_count > 1:
      return "NO"

    if maximum - minimum > 1 and min_count > 1:
      return "NO"

  # default case, for remaining possibility of only 1 frequency
  return "YES"
