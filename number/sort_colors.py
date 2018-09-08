def sortColors(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    front = 0
    back = len(nums) - 1
    check = 0
    
    while front < back:
      if nums[front] == 2:
        nums[front], nums[back] = nums[back], nums[front]
        back -= 1
      elif nums[front] == 1:
        check = front + 1
        while check <= back:
          if nums[check] == 0:
            nums[front], nums[check] = nums[check], nums[front]
            break
          else:
            check += 1
        front += 1
      elif nums[front] == 0:
        front += 1
       
        
