#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = input()
    letters = {}
    
    for letter in s:
      letters[letter] = 1 if letter not in letters else letters[letter] + 1
      
    # Sort dict by descending values and ascending keys
    letters = sorted(letters.items(), key=lambda x: (-x[1],x[0]))
 
    for i in range(3):
      print(letters[i][0], letters[i][1])
      
