def kaprekarNumbers(p, q):
  answer = []
  
  for num in range(p, q + 1):
    squared = num * num
    squared_length = len(str(squared))
    right_length = squared_length - len(str(num))
    string_num = str(squared)
    
    if squared_length > 1:
      left = string_num[:right_length]
      right = string_num[right_length:]
    else:
      left = 0
      right = string_num[-1]
    
    if int(left) + int(right) == num:
      answer.append(num)

  if answer:
    for x in answer:
      print(x, end=" ")
  else:
    print("INVALID RANGE")
    