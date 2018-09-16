def superpalindromesInRange(self, L, R):
    """
    :type L: str
    :type R: str
    :rtype: int
    """
    answer = []
    limit = int((10 ** 18) ** 0.25)
    
    def is_palindrome(number):
      return (str(number) == str(number)[::-1])
    
    def valid_square(squared):
      if squared >= int(L) and is_palindrome(squared):
        answer.append(pal_num)

    # Odd length palindromes
    for value in range(1, limit):
      pal_num = str(value) + str(value)[-2::-1]
      squared = int(pal_num) ** 2

      if squared > int(R):
        break
      valid_square(squared)
        
    # Even length palindromes
    for value in range(1, limit):
      pal_num = str(value) + str(value)[::-1]
      squared = int(pal_num) ** 2
      
      if squared > int(R):
        break
      valid_square(squared)
    
    return (len(answer))
    