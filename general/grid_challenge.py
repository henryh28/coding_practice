# Complete the gridChallenge function below.
def gridChallenge(grid):
  for i in range(len(grid)):
    grid[i] = sorted(list(grid[i]), reverse=True)
  
  rotated = zip(*grid)
  
  for row in rotated:
    for j in range(1, len(row)):
      if row[j] < row[j-1]:
        return ("NO")
        
  return ("YES")
  