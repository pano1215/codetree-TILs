from itertools import combinations 

n = int(input())
arr = list(map(int, input().split()))

total_sum = sum(arr)
min_num = float('inf')
for num in combinations(arr, n) :
    grp1_sum = sum(num)
    grp2_sum = total_sum - grp1_sum

    diff = abs(grp1_sum - grp2_sum)
    min_num = min(min_num, diff)
    
print(min_num)