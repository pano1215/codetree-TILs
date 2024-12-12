import math
import sys
from itertools import combinations

n, m = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(n)]

max_len = -sys.maxsize
def min_length(com) :
    global max_len

    max_len = -sys.maxsize
    #print('com : ', com)
    for i in range(len(com)) :
        x1, y1 = com[i]
        for j in range(i + 1, len(com)) :
            x2, y2 = com[j]
            leng = (x1 - x2) ** 2 + (y1 - y2) ** 2
            
            max_len = max(max_len, leng)
            #print('leng : ', leng, max_len)
    max_arr.append(max_len)
    
    return max_len

max_arr = []
for com in combinations(arr, m) :
    #print(com)
    max_len = min_length(com)
    max_arr.append(max_len)
#print('max_arr : ', max_arr)

print(min(max_arr))