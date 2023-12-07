n = int(input())
arr = list(map(int, input().split()))
arr.sort()
max_num = 0 

while arr :
    num1 = arr.pop(0)
    num2 = arr.pop(-1)

    num_sum = num1 + num2
    if num_sum > max_num :
            max_num = num_sum
print(max_num)