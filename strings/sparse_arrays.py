def matchingStrings(strings, queries):
  answer = []
  string_dict = {}
  
  for string in strings:
    string_dict[string] = 1 if string not in string_dict else string_dict[string] + 1
    
  for query in queries:
    answer.append(string_dict[query] if query in string_dict else 0)
  
  return (answer)
  
