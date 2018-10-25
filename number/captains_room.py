_, groups = input(), input().split()
answer = {}

for value in groups:
    answer[value] = 1 if value not in answer else answer[value] + 1
    
for key, value in answer.items():
    if value == 1:
        print (key)
