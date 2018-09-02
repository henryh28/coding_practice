def isMonotonic(self, A):
  """
  :type A: List[int]
  :rtype: bool
  """
  pattern = None
  previous = A[0]
  
  for i in range(len(A)):
    if pattern == None:
      if A[i] > previous:
        pattern = "rising"
      if A[i] < previous:
        pattern = "falling"
    else:
      if pattern == "rising":
        if A[i] < previous:
          return False
      if pattern == "falling":
        if A[i] > previous:
          return False
    previous = A[i]
        
  return True
