def spiralOrder(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    answer = []
    
    while len(matrix) > 0:
      # Pop first row of matrix into answer
      answer.append(matrix.pop(0))

      # Rotate remaining matrix
      matrix = zip(*matrix)
      matrix = [list(x) for x in matrix][::-1]

    # Flatten answer into 1d array
    answer = [element for sublist in answer for element in sublist]
    return (answer)
    