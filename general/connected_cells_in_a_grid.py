def connectedCell(matrix):
  answer = 0
  vertical = len(matrix)
  horizontal = len(matrix[0])

  # Helper Depth First Search function
  def dfs(y, x):
    total = 0
  
    # Check if this cell is valid
    if matrix[y][x] != 1:
      return 0
    
    # Mark this cell as visited
    matrix[y][x] = -1
    
    # DFS up
    if y > 0:
      total += dfs(y - 1, x)
    
    # DFS up & right
    if y > 0 and x < horizontal - 1:
      total += dfs(y - 1, x + 1)

    # DFS right
    if x < horizontal - 1:
      total += dfs(y, x + 1)

    # DFS right & down
    if x < horizontal - 1 and y < vertical - 1:
      total += dfs(y + 1, x + 1)
      
    # DFS down
    if y < vertical - 1:
      total += dfs(y + 1, x)

    # DFS down & left
    if y < vertical - 1 and x > 0:
      total += dfs(y + 1, x - 1)
      
    # DFS left
    if x > 0:
      total += dfs(y, x - 1)

    # DFS left & up
    if y < vertical - 1 and y > 0:
      total += dfs(y - 1, x - 1)
      
    return (total + 1)
    
  for y in range(vertical):
    for x in range(horizontal):
      if matrix[y][x] == 1:
        size = dfs(y, x)
        answer = max(answer, size)
    
  return (answer)
