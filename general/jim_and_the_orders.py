# Complete the jimOrders function below.
def jimOrders(orders):
  temp = []

  for index, value in enumerate(orders, 1):
    temp.append((value[0] + value[1], index))
    
  temp.sort()
  answer = [number for time, number, in temp]

  return(answer)
  