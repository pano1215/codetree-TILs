n, m = map(int, input().split())
exp = list(map(int, input().split()))

temp = []
max_num = -1

def find_max(result) :
    global max_num
    max_num = max(max_num, result)

def xor() :
    result = 0
    for t in temp :
        result = result ^ t
    find_max(result)
    return 

def start(num) :
    if len(temp) == m :
        #print(temp)
        xor()
        return 
    
    for i in range(num, n) :
        temp.append(exp[i])
        start(i + 1)
        temp.pop()

start(0)

print(max_num)