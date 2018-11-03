    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count_dict = {}
        max_value = 0
        answer = None
        
        for value in nums:
          count_dict[value] = 1 if value not in count_dict else count_dict[value] + 1
        
        for key, value in count_dict.items():
          if value > max_value:
            max_value = value
            answer = key
            
        return (answer)
