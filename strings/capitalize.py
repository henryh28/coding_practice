def solve(s):
  words = s.split(' ')
  return (" ".join(word.capitalize() for word in words))
