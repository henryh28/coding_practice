def minPatches(self, nums, n):
    """
    :type nums: List[int]
    :type n: int
    :rtype: int
    """
    covered, index, answer = 1, 0, 0
    
    while covered <= n:
      if index < len(nums) and nums[index] <= covered:
        covered += nums[index]
        index += 1
      else:
        covered += covered
        answer += 1
    
    return answer
