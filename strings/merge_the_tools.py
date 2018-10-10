def merge_the_tools(string, k):
  
  # Breaks up string into 'k' sized chunks in an iterable
  for sections in zip(*[iter(string)] * k):
    output = []
    for letter in sections:
      if letter not in output:
        output.append(letter)
      
    print("".join(output))
    
