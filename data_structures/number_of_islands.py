class Solution:
  def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    islands = 0
    
    def explore(line, index):
      if grid[line][index] == "1":
        grid[line][index] = "x"
      else:
        return

      if line != 0:               # up
        explore(line - 1, index)
      if line < len(grid) - 1:    # down
        explore(line + 1, index)
      if index != 0:              # left
        explore(line, index - 1)
      if index < len(grid[line]) - 1: # right
        explore(line, index + 1)
        
    for line in range(len(grid)):
      for index, value in enumerate(grid[line]):
        if value == "1":
          explore(line, index)
          islands += 1
          
    return islands
    