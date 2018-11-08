def maxProduct(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    backwards = nums[::-1]
    answer = max(nums)

    for i in range(1, len(nums)):
      if nums[i - 1] != 0:
        nums[i] *= nums[i - 1]

      if backwards[i - 1] != 0:
        backwards[i] *= backwards[i - 1]

      answer = max(answer, nums[i], backwards[i])

    return (answer)
