class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
            
        stack = []
        length = len(s)

        lookup = {')': '(', ']': '[', '}': '{'}

        # Quick check for odd lengthed string, if odd length cannot close all open chars
        if length % 2 != 0:
            return (False)

        for i in range(len(s)):
            # check if current character is a (closing) key in lookup dict
            if s[i] in lookup:
                # check last element of stack to see if it matches value of current key
                if len(stack) > 0:
                    test = stack[-1]
                    # pop matching opening character off the stack if a match
                    if test == lookup[s[i]]:
                        del stack[-1]
                else:
                    # no element in stack, cannot have matching opener to current closer
                    return (False)
            else:
                # Will only fire for 'opening' characters
                stack.append(s[i])

        return (len(stack) == 0)
