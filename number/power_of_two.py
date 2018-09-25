def isPowerOfTwo(self, n):
  """
  :type n: int
  :rtype: bool
  """
  test = 0
  power = 1
  
  # Special handling for odd numbers
  if n % 2 != 0:
    return (True if n == 1 else False)
    
  # Handling for even numbers        
  while test < n:
    test = 2 ** power 
    power += 1
    
    if test == n:
      return (True)
  
  return (False)
  