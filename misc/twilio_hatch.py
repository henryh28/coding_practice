#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'split' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING message as parameter.
#

# Idea for extra credit:
# Split incoming 'message' into list of words interspersed with a blank space.  Create new blank
# line and append the word if current line length + word length will not exceed 155. Add on 
# segment info.  check for output constraints

def split(message):
  # Chunk = 155 because max segment length is 160, then minus 5 for segment info. (1/9)
  # Count = Beginning of the count for number of segments to return
  # length = length of 'message' argument. Calculated once here to prevent further len() calls
  # segments = number of segments, of max length 160, to return.  Maximum allowed segment is 9
  # answer = Array containing the segments of texts to return to calling function
  chunk, count = 155, 1
  length = len(message)
  segments = min(9, (length // 155) + 1)
  answer = []

  # If message is less than 160 characters, return unmodified message as element in answer,
  # Otherwise, break 'message' into chunks of max length 155 (to accommodate the extra 5 characters
  # segment info to be appended at end of line), and append the segmented string as next element in answer
  if length <= 160:
    return ([message])
  else:
    for i in range(0, length, chunk):
      answer.append(message[i:i+chunk] + "({}/{})".format(count, segments))
      count += 1

    return (answer)


if __name__ == '__main__':
