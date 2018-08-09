class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        answer = []
        
        if len(nums) == 0:
          return answer
        
        for index in range(len(nums) - k + 1):
          window = nums[index:index + k]
          answer.append(max(window))
        
        return (answer)
        
