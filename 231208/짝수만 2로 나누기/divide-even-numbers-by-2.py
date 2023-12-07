# 변수 선언 및 입력:
n = int(input())
arr = list(map(int, input().split()))


def modify(arr):
    for i in range(n):
        if arr[i] % 2 == 0:
            arr[i] //= 2


modify(arr)
for elem in arr:
    print(elem, end=" ")