def budgetShopping(n, bundleQuantities, bundleCosts):
  answer, index, previous_largest = 0, 0, 0
  remaining = n

  # Need to run loop until out of money or until no match is found
  while n > 0:
    remaining = n

    for index in range(len(bundleCosts)):
      times = n // bundleCosts[index]
      
      if times > 0:
        if times * bundleQuantities[index] + previous_largest > answer:
          answer = (times * bundleQuantities[index]) + previous_largest
          remaining = n % bundleCosts[index]
          
    if remaining == n:
      break
    else:
      n = remaining
      previous_largest = answer

  return (answer)
  
