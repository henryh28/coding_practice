    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if nums:
          answer = [[nums[0]]]
        else:
          return []
        
        if len(nums) == 1:
          return ([str(nums[0])])
        
        for index in range(1, len(nums)):
          if nums[index] != answer[-1][-1] + 1:
            answer.append([nums[index]])
          else:
            answer[-1].append(nums[index])
        
        ranges = []
        for rng in answer:
          ranges.append(str(rng[0]) if len(rng) == 1 else str(rng[0]) + "->" + str(rng[-1]))

        return (ranges)       

