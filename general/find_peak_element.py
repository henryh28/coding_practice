def findPeakElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    for index in range(len(nums)):
      if index < len(nums) - 1:
        if nums[index] > nums[index + 1]:
          return (index)
      else:
        return (index)
