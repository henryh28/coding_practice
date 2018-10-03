def bonAppetit(bill, k, b):
  # k is the index of the item that wasn't eaten by allergic member
  # b is the amount paid by the allergic member
  lesser_half = (sum(bill) - bill[k]) // 2
  
  print ("Bon Appetit" if lesser_half == b else b - lesser_half)
  