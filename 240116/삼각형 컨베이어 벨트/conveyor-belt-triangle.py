# 123 
# 593
# 651

# 123 593 651
# 112 359 365

n, t = map(int, input().split())

first_arr = list(map(int, input().split()))
second_arr = list(map(int, input().split()))
third_arr = list(map(int, input().split()))
arr = []
arr = first_arr + second_arr + third_arr

def Print() :
    for i in range(1, len(arr) + 1) :
        print(arr[i - 1], end = ' ')
        if (i % n == 0) :
            print()
    
def Turn() :
    for time in range(t) : 
        temp = arr[-1]
        for i in range((n * 3) - 1, 0, -1) :
            arr[i] = arr[i - 1]
        arr[0] = temp
    Print()
    
Turn()