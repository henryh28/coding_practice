def minimumLoss(price):
  lowest = max(price)
  value_and_index = []
  
  for index, value in enumerate(price):
    value_and_index.append((value, index))
  
  value_and_index.sort(reverse = True)
  
  for index in range(len(value_and_index) - 1):
    # Only process if next value comes after current value
    if value_and_index[index][1] < value_and_index[index + 1][1]:
      loss = value_and_index[index][0] - value_and_index[index + 1][0]
      if loss >= 0:
        lowest = min(lowest, loss)
        # Short circuit return.  zero loss is minimum possible loss
        if lowest == 0:
          return (lowest)
  
  return (lowest)
  