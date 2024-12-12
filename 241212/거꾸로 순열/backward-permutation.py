from itertools import permutations 

n = int(input())
arr = [i for i in range(n, 0, -1)]

for per in permutations(arr, n) :
    for num in per :
        print(num, end = ' ')
    print()