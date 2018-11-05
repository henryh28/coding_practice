def sockMerchant(n, ar):
  sock_dict = {}
  answer = 0
  
  for value in ar:
    sock_dict[value] = 1 if value not in sock_dict else sock_dict[value] + 1
    
  for _, value in sock_dict.items():
    answer += value // 2
      
  return (answer)
  
