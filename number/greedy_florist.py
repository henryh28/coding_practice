def getMinimumCost(k, c):
  cost = 0
  multiplier = 1
  c.sort()
  
  for i in range(1, len(c) + 1):
    cost += c.pop() * multiplier
    
    # multiplier increment check
    if i % k == 0:
      multiplier += 1

  return (cost)
