#
# Complete the 'missingWords' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#

def missingWords(s, t):
  words_s = s.split()
  words_t = t.split()
  answer = []
  word_dict = {}
  
  for word in words_t:
    word_dict[word] = 1 if word not in word_dict else word_dict[word] + 1
  
  for word in words_s:
    if word not in word_dict.keys():
      answer.append(word)
      
  return (answer)
  
