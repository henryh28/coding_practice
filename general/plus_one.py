class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # convert 'digits' (a list of ints) into one integer value and add 1 to it
        temp = int(''.join(map(str, digits))) + 1

        # Convert the computed value back into a list and return it
        return (list(map(int, str(temp))))
    
