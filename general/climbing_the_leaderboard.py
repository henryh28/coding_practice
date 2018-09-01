def climbingLeaderboard(scores, alice):
  lookup = [(scores[0], 1)]
  answer = []
  
  for _, value in enumerate(scores):
    if value < lookup[-1][0]:
      lookup.append((value, lookup[-1][1] + 1))
  
  for score in alice:
    lop = 0
    for i in range(len(lookup) - 1, -1, -1):
      if score < lookup[i][0]:
        answer.append(lookup[i][1] + 1)
        break
      if score == lookup[i][0]:
        answer.append(lookup[i][1])
        break
      if i == 0:
        answer.append(1)
        break
      lop += 1
      
    for i in range(lop):
      lookup.pop()
    
  return(answer)
