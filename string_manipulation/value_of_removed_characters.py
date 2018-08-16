def ascii_distance(str1, str2):
  str_1_dict = {}
  removed_ascii_value = 0

  # Read letter and their frequency into a dictionary
  for char in str1:
    str_1_dict[char] = 1 if char not in str_1_dict else str_1_dict[char] + 1

  '''
    Compare letters in second string and to first string letters 
    in the dictionary. Reduce the value of each letter/key for each 
    occurence in second string.  Remove key from dictionary if 
    Value ever becomes zero. If letter is not in dictionary, 
    add the ascii value for the nonmatching character right away
  '''
  for char in str2:
    if char in str_1_dict:
      str_1_dict[char] -= 1

      if str_1_dict[char] <= 0:
        str_1_dict.pop(char, None)
    else:
      removed_ascii_value += ord(char)

  # Add ascii value of remaining key in dictionary value number of
  # times to answer
  for key, value in str_1_dict.items():
    for i in range(value):
      removed_ascii_value += ord(key)

  return (removed_ascii_value)

st_1 = "through" #ough, remove t, h, r
st_2 = "sloughs" #ough, remove s, l, s

st_3 = "cat" #at, remove c
st_4 = "bat" #at, remove b

print (ascii_distance(st_1, st_2))
print (ascii_distance(st_3, st_4))
