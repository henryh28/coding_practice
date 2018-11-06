def arrayManipulation(n, queries):
  numbers = [0] * (n + 1)
  subtotal, answer = 0, 0
  
  for start, end, value in queries:
    numbers[start - 1] += value
    numbers[end] -= value
    
  for number in numbers:
    subtotal += number
    answer = max(subtotal, answer)
  
  return (answer)
  
