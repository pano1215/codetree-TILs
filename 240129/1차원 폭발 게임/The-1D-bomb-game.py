n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# 터진 결과 담기 
def Copy(bomb) :
    copy_arr.append(bomb)
    if 0 in copy_arr :
        copy_arr.remove(0)
    return copy_arr

# m이상으로 연속하는 폭탄이 있는지 체크
def Same_check(bomb) :
    cnt = 1
    for i in range(arr.index(bomb), len(arr) - 1) :
        if bomb == arr[i + 1] and arr[i] == arr[i + 1] :
            cnt += 1
        else :
            cnt = 1
        
        if cnt >= m :
            return Copy(0)
    return Copy(bomb)

# m이상으로 연속하는 폭탄이 있는지 체크 - 없다면 반복 종료 
def Final_same_check(arr) :
    cnt = 1
    for i in range(len(arr) - 1) :
        if arr[i] == arr[i + 1] :
            cnt += 1
        else :
            cnt = 1
        
        if cnt >= m :
            return True
    return False

copy_arr = []
for bomb in arr :
    copy_arr.append(bomb)

while Final_same_check(arr) :
    copy_arr = []
    for bomb in arr :
        #print(bomb)
        copy_arr = Same_check(bomb) 
    #print(copy_arr)
    
    if not Final_same_check(copy_arr) :
        break

    arr = []
    for ca in copy_arr :
        arr.append(ca)

# 정답 출력
print(len(copy_arr))

if len(copy_arr) != 0 :
    for ca in copy_arr :
        print(ca)