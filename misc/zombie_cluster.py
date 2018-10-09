
#
# Complete the 'zombieCluster' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY zombies as parameter.
#

def zombieCluster(zombies):
  answer = 0
  size = len(zombies)
  searched = []
  
  def explore(line, index):
    if [line, index] not in searched:
      if zombies[line][index] == "1":
        searched.append([line, index])
      else:
        return
    else:
      return

    if line != 0:                       # search up
      explore(line - 1, index)
    if line < len(zombies) - 1:         # search down
      explore(line + 1, index)
    if index != 0:                      # search left
      explore(line, index - 1)
    if index < len(zombies[line]) - 1:  # search right
      explore(line, index + 1)
      
    
  # This is a depth first search grid problem
  for line in range(size):
    for index, value in enumerate(zombies[line]):
      if [line, index] not in searched:
        if value == "1":
          explore(line, index)
          print("current searched: ", searched)
          answer += 1
  
  return (answer)
