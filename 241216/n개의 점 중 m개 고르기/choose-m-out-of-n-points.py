from itertools import combinations
import math
import sys

n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

max_arr = []
def fine_len(arr) :
    global max_val, max_arr

    x1, y1 = arr[0][0], arr[0][1]
    x2, y2 = arr[1][0], arr[1][1]

    dist = (x1 - x2) ** 2 + (y1 - y2) ** 2
    return dist

for num in combinations(points, m) :
    #print(num)
    max_val = -sys.maxsize
    for two_com in combinations(num, 2) :
        #print(two_com)
        dist = fine_len(two_com)
    
        max_val = max(max_val, dist)
    max_arr.append(max_val)

print(min(max_arr))