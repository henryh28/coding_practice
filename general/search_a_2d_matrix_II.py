def searchMatrix(self, matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    if not matrix or not matrix[0]:
      return False

    row = 0
    column = len(matrix[0]) - 1

    while True:
      value = matrix[row][column]
      
      if value == target:
        return True
      
      if value > target:
        if column > 0:
          column -= 1
        else:
          return False
      else:
        row += 1
        if row > len(matrix) - 1:
          return False
          