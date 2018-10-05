n, x = map(int, input().split()) 

gradebook = []

# Append each list of grades into gradebook
for _ in range(x):
  gradebook.append(map(float, input().split())) 
    
# Zip up each column of all lists in gradebook for calculating average
for grades in zip(*gradebook): 
  print(sum(grades) / len(grades))
  
