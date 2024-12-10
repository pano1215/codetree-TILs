from itertools import combinations

n, m = map(int, input().split())
arr = [i + 1 for i in range(n)]

for com in combinations(arr, m) :
    for num in com : 
        print(num, end = ' ')
    print()

