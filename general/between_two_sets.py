#!/bin/python3

import os
import sys

#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    
    a.sort()
    b.sort()
    step = 1
    complete = False
    start = -1
    largest = a[-1]
    possibles, answer = [], []

    while complete == False:
        complete = True

        if (largest * step) > b[0]:
            return (0)
        
        for i in a:
            if (largest * step) % i != 0:
                complete = False

        if complete == False:
            step += 1
        else:
            start = largest * step

    temp = start

    while temp <= b[0]:
        possibles.append(temp)
        temp += start

    for test_value in possibles:
        valid = True

        for element in b:
            if element % test_value != 0:
                valid = False

        if valid == True:
            answer.append(test_value)
            print("answer: ", answer)

    return(len(answer))
    
    
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()