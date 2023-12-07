n = int(input())
arr = list(map(int, input().split()))

def max_num(n) :
    #re = 0
    #for i in arr :
    #    if i > re :
    #        re = i
        # print(re)
    #return re
    if n == 0 :
        return arr[0]
    return max(max_num(n - 1), arr[n])

print(max_num(n-1))