n = int(input())
arr1 = [list(map(int, input().split())) for _ in range(n)]
arr2 = [[0 for _ in range(n)] for _ in range(n)]

arr2[0][0] = arr1[0][0]

# 가로 세로 값 설정하기 
for row in range(n) :
    for col in range(n) : 
        if row == 0 :
            arr2[0][col] += arr1[0][col] 
        
    arr2[row][0] += arr1[row][0]

    print(arr2)