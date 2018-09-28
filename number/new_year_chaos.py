def minimumBribes(q):
  answer = 0
  index = len(q) - 1
  
#  for index in reversed(range(len(q))):
  while index >= 0:
    value = q[index]

    if value > index + 1:
      # Current value is more than 2 steps away from correct position. Invalid sequence
      if value > index + 3:
        answer = "Too chaotic"
        break
      else:
        # Number of steps current value is away from correct position
        steps = value - (index + 1)

        # Sort the out of position segment        
        for i in range(steps):
          q[index + i] = q[index + i + 1]
        q[index + steps] = value

        # Update answer and reset iterator by 1 to continue from current place
        answer += steps
        index += 1
    index -= 1

  print(answer)
  