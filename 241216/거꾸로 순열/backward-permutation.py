from itertools import permutations

n = int(input())
temp = [i for i in range(n, 0, -1)]

for num in permutations(temp, n) :
    for e in num :
        print(e, end = ' ')
    print()

# def start(n) : 
#     if len(temp) == n :
#         print(temp)
#         return

#     for i in range(n, 0, -1) :
#         temp.append(i)
#         start(n - 1)
#         temp.pop()

# start(n)