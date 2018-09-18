def findShortestSubArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    frequency = {}
    valid_values = []
    minimum = len(nums) + 1
    reverse_nums = nums[::-1]
    
    for val in nums:
      frequency[val] = 1 if val not in frequency else frequency[val] + 1
      
    max_freq = max(frequency.values())
    
    for key, value in frequency.items():
      if value == max_freq:
        valid_values.append(key)

    for number in valid_values:
      start = nums.index(number)
      end = len(nums) - reverse_nums.index(number) - 1
      temp = end - start + 1
      
      minimum = min(minimum, temp)
        

    return (minimum)
