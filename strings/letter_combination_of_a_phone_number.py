class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
          return [] 
        
        cypher = {
          '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
          '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz',
        }
        
        groups = [cypher[digit] for digit in digits if digit in cypher]
        answer = list("".join(x) for x in itertools.product(*groups))
        
        return (answer)
        