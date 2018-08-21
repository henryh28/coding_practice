def toys(w):
  w.sort()
  window = 4
  containers = 1
  limit = w[0] + 4
  
  for i in range(len(w)):
    if w[i] > limit:
      containers += 1
      limit = w[i] + window
      
  return (containers)
  