# unique_characters: method for determining if a string has only unique characters 
# string:            String argument to be checked
# Return:            (True) 'string' has only unique characters 
#                    (False) if 'string' contains any non-unique characters

def unique_characters(string):
  string = ''.join(sorted(string))

  for i in range(0, len(string)-1):
    if string[i + 1]:
      if string[i] == string[i + 1]:
        return (False)

  return True

# ================ Test cases =======================

test_1 = "maria"      # False
test_2 = "henry"      # True
test_3 = "true 1"     # True
test_4 = "false test" # False
test_5 = "  "         # False

print("{}: \t\t{}".format(test_1, unique_characters(test_1)))
print("{}: \t\t{}".format(test_2, unique_characters(test_2)))
print("{}: \t{}".format(test_3, unique_characters(test_3)))
print("{}: \t{}".format(test_4, unique_characters(test_4)))
print("{}: \t\t{}".format(test_5, unique_characters(test_5)))
