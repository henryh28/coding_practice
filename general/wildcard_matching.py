def isMatch(self, s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    # shortcut
    if s == p or p == "*":
      return True
    
    if min(len(s), len(p)) == 0 and max(len(s), len(p)) > 0:
      return False        

    s_len = len(s)
    dp = [True] + [False] * s_len
    
    for p_letter in p:
      if p_letter == "*":          # Multi match
        for index in range(1, s_len + 1):
          dp[index] = dp[index - 1] or dp[index]
      else:                        # Single match
        for index in reversed(range(s_len)):
          dp[index + 1] = dp[index] and (p_letter == s[index] or p_letter == "?")
      
      dp[0] = dp[0] and p_letter == "*"
      
    return dp[-1]
    