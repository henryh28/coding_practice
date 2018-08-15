# Complete the hackerrankInString function below.
def hackerrankInString(s):
  target = "hackerrank"

  for letter in s:
    if letter == target[0]:
      target = target[1:]
      
      if len(target) == 0:
        return "YES"

  return "NO"
  