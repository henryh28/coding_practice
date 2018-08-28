def decentNumber(n):
  answer = ""
  quotient = n // 3
  remainder = n % 3

  if n < 3:
    print (-1)
    return
  
  while quotient >= 0:
    if remainder % 5 == 0:
      remainder = remainder // 5

      for i in range(quotient):
        answer += "555"
      for i in range(remainder):
        answer += "33333"

      print (answer)
      return
    else:
      quotient -= 1
      remainder += 3

  print (-1)
  