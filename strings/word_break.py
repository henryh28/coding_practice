class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        matches = [True] + ([False] * len(s))
        length = len(s)
            
        # Set graph corresponding to end of word to true when a word in dict is found, check to see 
        # if rest of word exists in dict; if not, repeat process from end of currently found word
        for start in range(length):
          for end in range(start, length):
            if matches[start] and s[start:end + 1] in wordDict:
              matches[end + 1] = True
                    
        return matches[-1]
    
