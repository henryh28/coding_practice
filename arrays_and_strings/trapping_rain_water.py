class Solution:
  def trap(self, height):
    answer = 0

    # can't hold anything
    if len(height) < 3:
      return answer

    # remove leading and ending Zeros 
    while height[0] == 0 or height[-1] == 0:
      height.pop(0) if height[0] == 0 else height.pop()


    # helper method to calculate amount of trapped water
    def amount(left, right, index):
      temp = 0

      if left == -1:
        # move left index up to highest index and process only right
        left = index
      if right == -1:
        # move right index down to highest index and process only left
        right = index

      # update total amount of trapped water in current segment
      for i in range(left, right):
        temp += height[index] - height[i]

      return (temp)

    # loop while the possibility of a gap exists
    while len(height) > 2:
      # Get the highest point in the height
      copy = sorted(height, reverse=True)
      high = min(copy[0], copy[1])
      highest = max(height)
      highest_index = height.index(highest)
      height[highest_index] = high


      # look for highs on left and right of highest Index 
      test = [index for index, value in enumerate(height) if value == high]
      left_index = min(test) if len(test) > 0 else -1
      right_index = max(test) if len(test) > 0 else -1

      answer += amount(left_index, right_index, highest_index)

      # remove processed segment from height
      height = height[:left_index] + height[right_index:]

    return (answer)
    