n = int(input())
cnt = 0
num_arr = [] # 붙일 숫자를 만드는 배열

# 아름다운 수인지 체크하기 
def is_beautiful() :
    i = 0
    while i < n :
        
        # 인덱스를 초과하는 경우
        if i + num_arr[i] - 1 >= n :
            return False
        
        # 연속하는 수를 찾기
        for j in range(i, i + num_arr[i]) :
            if num_arr[j] != num_arr[i] :
                return False

        i += num_arr[i]
    return True

# 숫자만들기
def make_num(num) :
    global cnt 
    if len(num_arr) >= n :
        if is_beautiful(): 
            cnt += 1
        return
    
    for i in range(1, 5) :
        num_arr.append(i)
        make_num(i + 1)
        num_arr.pop()

make_num(0)

print(cnt)