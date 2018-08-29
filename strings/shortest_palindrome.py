def shortestPalindrome(self, s):
    """
    :type s: str
    :rtype: str
    """
    rev_s = ''.join(reversed(s))
    answer = ""
    
    for i in range(len(s)):
      if s[0:len(s) - i] == rev_s[i:]:
        temp = ""
        if i > 0:
          temp = "".join(reversed(s[-i:]))
        answer = temp + s
        return (answer)
    
    return (answer)
