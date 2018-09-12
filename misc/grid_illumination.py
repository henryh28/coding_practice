def answer(N, lamps, queries):
  lamp_list = [[] for x in range(N)]
  answer = []

  # Populate 2d array representation of lamps
  for lamp in lamps:
    lamp_list[N - lamp[1]].append(lamp[0] - 1)

  # Check each query against existing lamps for illumination
  for query in queries:
    # Convert query into standard 2d array notation
    query = [N - query[1], query[0] - 1]
    lit = False

    # Iterate over each row that might contain lamps
    for index, row in enumerate(lamp_list):
      distance = abs(query[0] - index)

      for lamp_node in row:
        # Check to not process any lamps that are adjacent to query
        if distance > 1 or (abs(query[1] - lamp_node) > 1):
          if index == query[0]:
            lit = True
            break

          if lamp_node == query[1]:
            lit = True
            break

          if abs(query[1] - lamp_node) == abs(query[0] - index):
            lit = True
            break

    answer.append("LIGHT" if lit else "DARK")
    
  return (answer)
  
lamps = [[3,4], [4,4], [1,6], [5,2], [7,8]]
queries = [[4,3], [1,5], [6,6], [6,1], [3,5]]

print(answer(8, lamps, queries))
