def icecreamParlor(m, arr):
  prices = {}
  
  for index, value in enumerate(arr):
    prices[value] = [index] if value not in prices else prices[value] + [index]

  for index, value in enumerate(arr):
    second_value = m - value
    
    if second_value in prices:
      indices = prices[second_value]
  
      for second_index in indices:
        if second_index != index:
          return ([index + 1, second_index + 1])
  
  return ([-1, -1])


'''
def icecreamParlor(m, arr):
  for index, value in enumerate(arr):
    target_value = m - value
    
    for second_index, second_value in enumerate(arr):
      if second_value == target_value and second_index != index:
        return ([index + 1, second_index + 1])
      
  return ([-1, -1])
'''
