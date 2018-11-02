_, inputs = input(), set(input().split())

for _ in range(int(input())):
    command = input().split()[0]
    getattr(inputs, command)(set(input().split()))
    
print (sum(map(int, inputs)))
