def biggerIsGreater(w):
  for i in reversed(range(len(w))):
    temp_slice = list(w[i:])
    
    if temp_slice != sorted(temp_slice, reverse = True):
      head = min([x for x in temp_slice if x > temp_slice[0]])
      temp_slice.remove(head)
      next_largest = min(temp_slice)
      temp_slice.remove(next_largest)
      
      return (w[:i] + head + next_largest + "".join(sorted(temp_slice)))
      
  return ("no answer")
  
