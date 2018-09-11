n, m = map(int, input().split())
array = list(input().split())
a = set(input().split())
b = set(input().split())

scores_by_value = [(value in a) - (value in b) for value in array]
print(sum(scores_by_value))
