import sys
for line in sys.stdin:
    reverse = line[::-1]
    current_number = str(int(line) + int(reverse))
    answer = [1]
    
    while current_number[0] != current_number[-1]:
        new_reverse = current_number[::-1]
        current_number = str(int(current_number) + int(new_reverse))
        answer[0] = answer[0] + 1

    print(str(answer[0]) + " " + current_number)
