b, a = map(int, input().split())

for i in reversed(range(a, b + 1)):
    if i % 2 == 1:
        print(i, end = ' ')