def lights(n):
  # Create n-lengthed binary string of "1"s
  binary = "".join(["1" for x in range(n)])
  
  # Convert the binary string into numeric representation
  answer = int(binary, 2)

  # Return answer % 100000 per problem instructions
  return answer % 100000
