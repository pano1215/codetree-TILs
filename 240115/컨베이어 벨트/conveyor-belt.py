n, t = map(int, input().split())
up_arr = list(map(int, input().split()))
down_arr = list(map(int, input().split()))
arr = up_arr + down_arr

def Print(arr) :
    for i in range(1, len(arr) + 1) :
        print(arr[i - 1], end = ' ')
        if (i > 0 and i % 3 == 0) :
            print()

def turn() :
    for time in range(t) : 
        last_num = arr[-1]
        for i in range((n * 2) - 1, 0, -1) :
            arr[i] = arr[i - 1]
        arr[0] = last_num
    Print(arr)


turn()

# for time in range(t) :
#     for row in range(len(arr)) :
#         temp1 = arr[0][n - 1]
#         temp2 = arr[1][n - 1]

#         for i in range(n - 1, 0, -1) :
#             arr[row][i] = arr[row][i - 1]
#         arr[1][0] = temp1
#         arr[0][0] = temp2