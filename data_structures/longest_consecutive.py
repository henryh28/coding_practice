class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest_streak = 0
        num_set = set(nums)
        
        # iterate over all numbers in set, to measure streak for all possible starting chains
        for value in num_set:
            # Find the start of a chain of numbers
            if value - 1 not in num_set:
                current = value
                streak = 1
        
                # measure the streak for each chain once start is found
                while current + 1 in num_set:
                    current += 1
                    streak += 1
                
                longest_streak = max(longest_streak, streak)
        
        return longest_streak
        