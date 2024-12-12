from itertools import permutations
from itertools import combinations
from itertools import product

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr_points = [[(j, i) for i in range(n)] for j in range(n)]
#print(arr_points)

def is_valid_combination(per) :
    row = set()
    col = set()

    for x, y in per :
        if x in row or y in col:  # 이미 같은 행 또는 열이 존재하면 False
            return False
        row.add(x)
        col.add(y)
    return True

sum_num = 0
sum_arr = -float('inf') # [] 
for per in product(*arr_points) :
    if is_valid_combination(per):
        #print(per)

        sum_num = 0
        for i in range(len(per)) :
            x, y = per[i]
            sum_num += arr[x][y]
            sum_arr = max(sum_arr, sum_num)
            #sum_arr.append(sum_num)

print(sum_arr)