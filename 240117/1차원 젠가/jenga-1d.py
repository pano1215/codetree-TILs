n = int(input())
block = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

def Gether(b_arr) :
    arr = [0] * len(b_arr)
    for i in range(len(b_arr)) :
        arr[i] = b_arr[i]
    return arr

def Move(a_arr) :
    temp = []
    for e in a_arr :
        if e != 0 :
            temp.append(e)
    return Gether(temp)
    
def Blank1() :
    for i in range(s1 - 1, e1) :
        block[i] = 0
    return Move(block)

def Blank2(sec_arr) :
    for i in range(s2 - 1, e2) :
        sec_arr[i] = 0
    return Move(sec_arr)

sec_arr = Blank1()
thi_arr = Blank2(sec_arr)

print(len(thi_arr))
for e in thi_arr :
    print(e)