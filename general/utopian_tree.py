def utopianTree(n):
  height = 1
  
  for i in range(1, n + 1):
    height = height * 2 if i % 2 != 0 else height + 1
      
  return (height)
