from itertools import combinations 

n, m = map(int, input().split())
arr = list(map(int, input().split()))

max_num = -1
result = 0
for com in combinations(arr, m) :
    #print('com : ', com)
    for num in com :
        result = result ^ num
    max_num = max(max_num, result)
    result = 0
print(max_num)
