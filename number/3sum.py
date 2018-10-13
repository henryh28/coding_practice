    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = []
        nums.sort()        
        
        for first in range(len(nums) - 2):
          # Skip subsequent triplets that start with a previously checked value
          if first > 0 and nums[first] == nums[first - 1]:
            continue

          second, third = first + 1, len(nums) - 1

          while second < third:
            target = nums[first] + nums[second] + nums[third]

            if target == 0:
              answer.append([nums[first], nums[second], nums[third]])
              while second < third and nums[second] == nums[second + 1]:
                second += 1
              while second < third and nums[third] == nums[third - 1]:
                third -= 1
              second += 1
              third -= 1
            else:
              if target > 0:
                third -= 1
              else:
                second += 1
        
        return (answer)
