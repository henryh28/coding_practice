def print_rangoli(size):
  letters = list(map(chr, range(97 + size - 1, 96, -1)))
  answer = []

  for index in range(size):
      line = "-".join(letters[0:index +1 ]) # create front half of line
      line += line[-2::-1]                  # append last half of line to line
      line = line.center(size * 4 - 3, "-") # pad rest of line with "-"
      answer.append(line)

  print("\n".join(answer + answer[-2::-1]))
  
