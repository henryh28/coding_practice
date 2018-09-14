# Complete the pairs function below.
def pairs(k, arr):
  answers = []

  for value in arr:
      answers.append(value + k)
  
  return(len(set(answers) & set(arr)))
  