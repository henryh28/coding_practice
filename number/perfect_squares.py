def numSquares(self, n):
    """
    :type n: int
    :rtype: int
    """
    answer, squares = [], [1]

    # Populating list of squares
    while squares[-1] < n:
      squares.append(int(math.sqrt(squares[-1]) + 1) ** 2)

    # Checking for single valued answer
    if n in squares:
      return (1)

    # Helper for finding if double valued answer exists
    def doubles(number):
      for value in squares:
        target = number - value
        if target in squares:
          return ([value, target])
      return ([])

    # Checking for 2 valued answers
    answer = doubles(n)
    if answer != []:
      return(len(answer))

    # Checking for triple valued answers
    for first in squares:
      target = n - first
      rest = doubles(target)

      if rest != []:
        answer = [first] + rest
        return (len(answer))

    # No combinations less than 4 exists. Lagrange 4 square theorem leads to answer of 4
    return (4)
