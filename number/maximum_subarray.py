def maxSubArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    current_value, max_value = nums[0], nums[0]

    if not nums:
      return (0)

    for number in nums[1:]:
      # Start from current value if sum of previous sequence is less than current value
      current_value = max(number, current_value + number)
      max_value = max(current_value, max_value)

    return (max_value)
