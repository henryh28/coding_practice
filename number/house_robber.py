    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        previous_highest, current_highest = 0, 0
        
        for value in nums:
          previous_highest, current_highest = current_highest, max(previous_highest + value, current_highest)
                
        return (current_highest)
        
