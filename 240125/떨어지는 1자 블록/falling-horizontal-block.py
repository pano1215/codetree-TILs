# 입력
n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 선언
k = k - 1

def is_in_range(x) :
    return 0 <= x < n 

# 1이 있는 지점의 위에 블록을 채움
# return된 row와 block_leng 바로 위부터 k만큼 1로 변경
def Load_block(check, row, block_leng) :
    for cnt in range(m) : # 블록길이만큼 반복
        arr[row][block_leng + cnt] = 1
        #print(block_leng, cnt, block_leng + cnt - 1)
    return arr

# 밑에 블록이 있는지 체크하는 함수
# 하나라도 1이면 있는거고 모두 0이면 없는 
def Check_block() :
    check = True
    for row in range(n) :
        for block_leng in range(k, k + m) :
            if is_in_range(row + 1) and arr[row + 1][block_leng] == 0 :
                check = True
            else :
                check = False
                return Load_block(check, row, block_leng)

arr = Check_block()

for e in arr :
    for ee in e :
        print(ee, end = ' ')
    print()