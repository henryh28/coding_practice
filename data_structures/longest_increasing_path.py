class Solution:
  
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        self.answer = 0
        board = [[0 for x in range(len(matrix[0]))] for y in range(len(matrix))]

        def dfs(x, y):
          value = matrix[y][x]
          length = 0
          
          # Use DFS to fill in empty nodes on graph of distance
          if board[y][x] == 0:
            # Check right of current node
            if x < len(matrix[0]) - 1:
              right = matrix[y][x + 1]
              if value < right:
                length = max(length, board[y][x + 1]) if board[y][x + 1] != 0 else max(length, dfs(x+1, y))
                
            # Check below current node
            if y < len(matrix) - 1:
              down = matrix[y + 1][x]
              if value < down:
                length = max(length, board[y + 1][x]) if board[y + 1][x] != 0 else max(length, dfs(x, y+1))

            # Check above current node
            if y > 0:
              up = matrix[y - 1][x]
              if value < up:
                length = max(length, board[y - 1][x]) if board[y - 1][x] != 0 else max(length, dfs(x, y-1))

            # Check left of current node
            if x > 0:
              left = matrix[y][x - 1]
              if value < left:
                length = max(length, board[y][x - 1]) if board[y][x - 1] != 0 else max(length, dfs(x - 1, y))

            # Set value of current node equal to 1(self) + largest adjacent path
            board[y][x] = 1 + length

            # Update answer with largest path currently found
            if 1 + length > self.answer:
              self.answer = 1 + length
              
            return(board[y][x])
        
        for vertical in range(len(matrix)):
          for horizontal in range(len(matrix[vertical])):
            dfs(horizontal, vertical)

        return (self.answer)
