n = int(input())
arr1 = [list(map(int, input().split())) for _ in range(n)]
arr2 = [[0 for _ in range(n)] for _ in range(n)]

arr2[0][0] = arr1[0][0]

# 가로 세로 값 설정하기 
for row in range(1, n) :
    for col in range(1, n) : 
        arr2[0][col] = arr2[0][col - 1] + arr1[0][col] 
    arr2[row][0] = arr2[row - 1][0] + arr1[row][0]

# 나머지 값 채우기
for row in range(1, n) :
    for col in range(1, n) : 
        arr2[row][col] = max(arr2[row - 1][col] + arr1[row][col], arr2[row][col - 1] + arr1[row][col])

print(max(arr2[-1]))