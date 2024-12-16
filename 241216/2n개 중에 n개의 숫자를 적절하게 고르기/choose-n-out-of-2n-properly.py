import sys

n = int(input())
arr = list(map(int, input().split()))

temp = []
total_sum = sum(arr)
min_val = sys.maxsize

def find_min(temp) :
    global total_sum, min_val

    temp_sum_1 = sum(temp)
    temp_sum_2 = total_sum - temp_sum_1
    min_val = min(min_val, abs(temp_sum_1 - temp_sum_2))
    temp_sum = sum(arr)

def start(num) : 
    if len(temp) == n :
        #print(temp)
        find_min(temp)
        return

    for i in range(num, len(arr)) :
        temp.append(arr[i])
        start(i + 1)
        temp.pop()

start(0)

print(min_val)