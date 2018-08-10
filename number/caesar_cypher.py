def caesarCipher(s, k):
  while k > 26:
    k -= 26

  # helper function to rotate string 's' by amount 'amount'
  def rotate(index, amount, limit, s):
    if ord(s[index]) + amount <= limit:
      s = s[:index] + chr(ord(s[index]) + amount) + s[index + 1:]
    else:
      overshoot = ((ord(s[index]) + amount) - limit) + (limit - 26)
      s = s[:index] + chr(overshoot)+ s[index + 1:]
      
    return (s)
  
  for index in range(len(s)):
    
    #lower case
    if ord(s[index]) >= ord('a') and ord(s[index]) <= ord('z'):
      s = rotate(index, k, ord('z'), s)

    # upper case
    if ord(s[index]) >= ord('A') and ord(s[index]) <= ord('Z'):
      s = rotate(index, k, ord('Z'), s)
    
  return(s)
  