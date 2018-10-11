def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    start, end = 0, len(height) - 1
    size = min(height[start], height[end]) * (end - start)

    while start < end:
      if height[start] < height[end]:
        start += 1
      else:
        end -= 1

      size = max(size, min(height[start], height[end]) * (end - start)) 

    return (size)
