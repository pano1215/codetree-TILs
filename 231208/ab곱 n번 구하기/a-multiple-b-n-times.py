n = int(input())

for _ in range(n) :
    arr = input().split()
    a, b = int(arr[0]), int(arr[1])

    sum = 1
    for i in range(a, b + 1):
        sum *= i
    print(sum)