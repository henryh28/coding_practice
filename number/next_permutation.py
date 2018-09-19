def nextPermutation(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    if nums == sorted(nums, reverse = True):
      nums.sort()        
    else:
      # Find descending element
      for index in range(len(nums) - 1, -1, -1):
        if nums[index] > nums[index - 1]:
          descending = index - 1
          break
          
      # Swap decending element with next largest element
      for index, value in enumerate(nums[descending + 1:]):
        next_largest = min(x for x in nums[descending + 1:] if x > nums[descending])
        
        if value == next_largest:
          swap_index = descending + index + 1
          nums[descending], nums[swap_index] = nums[swap_index], nums[descending]
          break
      
      # Sort the remaining areas, rebuilding since checker won't accept + .sort as answer
      prefix = nums[:descending + 1]
      suffix = sorted(nums[descending + 1:])
      
      for i in range(len(nums)):
        nums[i] = prefix[i] if i < len(prefix) else suffix[i - len(prefix)]
          