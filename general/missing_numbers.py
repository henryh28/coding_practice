def missingNumbers(arr, brr):
  dict_a, dict_b, answer = {}, {}, []
  
  for value in arr:
    dict_a[value] = 1 if value not in dict_a else dict_a[value] + 1

  for value in brr:
    dict_b[value] = 1 if value not in dict_b else dict_b[value] + 1
  
  for key, value in dict_b.items():
    if key not in dict_a:
      answer.append(key)
    elif dict_a[key] != value:
      answer.append(key)
  
  return (sorted(answer))
  