# urlify:            Replace all white space between words in strings with '%20' 
# string:            String argument to be modified
# Return:            Version of the string with white space between words replaced with '%20'

def urlify(string):
  # split the string using whitespace as delimiter
  # rejoin the string using '%20'
  
  return '%20'.join(string.split())

# ================ Test cases =======================

test_1 = "Mr John Smith     "  
expected = "Mr%20John%20Smith"

result = urlify(test_1)
print("Original: {}, returned: {}, same: {}".format(test_1, result, result == expected))
