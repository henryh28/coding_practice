def migratoryBirds(arr):
  highest = 0
  answer = None
  birds = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
  
  for bird in arr:
    birds[bird] += 1
  
  for key, value in birds.items():
    if value > highest:
      highest = value
      answer = key
  
  return (answer)
  