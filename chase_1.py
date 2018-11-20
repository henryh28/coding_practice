import sys

coins = [9, 3, 1]

for line in sys.stdin:
    answer, index = 0, 0
    target = int(line)

    while index < len(coins):
        if target >= coins[index]:
            answer += target // coins[index]
            target = target % coins[index]
        else:
            index += 1
            
    print (answer)
