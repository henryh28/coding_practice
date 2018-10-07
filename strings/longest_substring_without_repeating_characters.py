def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    substring, longest = [], []

    if len(s) <= 1:
      return (len(s))

    for index in range(len(s)):
      if s[index] in substring:
        chop = substring.index(s[index]) + 1
        substring = substring[chop:]

      substring.append(s[index])
      if len(substring) > len(longest):
        longest = substring[:]

    return (len(longest))
