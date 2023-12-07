a, b, c = map(int, input().split())

li = [0 for _ in range(3)]
li[0] = a
li[1] = b
li[2] = c

li.sort()

print(li[1])