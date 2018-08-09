def solve(s):
  max_length = 0
  uniques = list(set(s))
  
  # helper to verify string is alternating characters
  def validate(s):
    for index, value in enumerate(s, 1):
      if index % 2 != 0:  # odd characters
        if value != s[0]:
          return False
      else:               # even characters
        if value == s[0]:
          return False
        
    return True

  for x in uniques:
    for y in [y for y in uniques if y != x]:
      string = ""
      
      for char in s:
        if char == x or char == y:
          string += char

      valid = validate(string)
      
      if valid:
        max_length = max(max_length, len(string))
      
  return max_length
  
