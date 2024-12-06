n, m = map(int, input().split())
arr = list(map(int, input().split()))

temp = []
max_num = -1

# 연산값의 최대값 구하기 
def find_max(result) :
    global max_num

    max_num = max(max_num, result)

# 조합별 xor 연산하기
def find_xor(temp) :
    result = 0
    for t in temp :
        result = result ^ t
    find_max(result)
    #print('result : ', result)

# 조합만들기
def start(num) :
    if len(temp) == m :
        #print('temp : ', temp)
        find_xor(temp)
        return 

    for i in range(num, n) : 
        temp.append(arr[i])
        start(i + 1) 
        temp.pop()

start(0)

print(max_num)