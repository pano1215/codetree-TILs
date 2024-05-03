import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

# 좌표(target_num)를 입력받음
target_arr = list(map(int, input().split()))

# target_num을 찾는 이진탐색 함수
def binary_search(target_num, spectrum_arr) : 
    # left right 설정 
    left = 0
    right = len(spectrum_arr) - 1

    idx = False # 만약 스펙트럼(spectrum_arr)에 없다면 False로 return 

    # left <= right일 때까지 반복함 
    while left <= right : 
        # mid 설정
        mid = (left + right) // 2

        if spectrum_arr[mid] == target_num:
            idx = True
            break

        if spectrum_arr[mid] >= target_num :
            right = mid - 1
        else : 
            left = mid + 1

    return idx # target_num의 위치 반환 

# 각 범위(spectrum_arr)에서 좌표(target_arr)의 유무 판별 
def overlap_check(target_arr) : 
    temp_cnt = 0 
    for i in range(n) :
        num_cnt = target_arr.count(target_arr[i])
        temp_cnt = max(temp_cnt, num_cnt)
    return temp_cnt

# 각 범위(spectrum_arr)에 좌표(target_arr)가 있는지 없는지 체크
def check_is_not(target_arr, spectrum_arr) :
    check = False
    for i in range(n) :
        if target_arr[i] in spectrum_arr :
            check = True
    return check

# 각 범위에 해당하는 배열 만들기 
def make_spectrum_arr(left, right) :
    spectrum_arr = [] 
    while left <= right :
        spectrum_arr.append(left)
        left += 1
    return spectrum_arr

for _ in range(m) : # m번 선분의 범위가 주어짐
    spectrum = list(map(int, input().split()))

    # 범위에서 left right 설정 
    left = spectrum[0]
    right = spectrum[1]

    # 각 범위에 해당하는 배열 만들기 
    spectrum_arr = make_spectrum_arr(left, right)

    # 각 범위(spectrum_arr)에 좌표(target_arr)가 있는지 없는지 체크
    check = check_is_not(target_arr, spectrum_arr)
    
    if check : # 좌표(target_arr)가 범위(spectrum_arr) 안에 있는 경우 
        # target_arr에서 중복되는 값이 있는지 없는지 체크 함 
        temp_cnt = overlap_check(target_arr)

        # target_num의 중복이 없는 경우 | 중복이 있다면 target_num이 2이상이기 때문
        if temp_cnt == 1 : 
            cnt = 0
            ## target_arr을 순회하면서 갯수 구하기 
            for i in range(n) :
                target_num = target_arr[i]
                if binary_search(target_num, spectrum_arr) : # 스펙트럼(spectrum_arr)에 target_num가 있는 경우
                    cnt += 1
        # target_num의 중복이 있는 경우
        ## target_arr을 순회하면서 처음 시작 위치 구하기 
        ## target_arr을 순회하면서 처음 끝 위치 구하기 
        ## 갯수 구하기 
        print(cnt)
        continue
    else : # 좌표(target_arr)가 범위(spectrum_arr) 안에 없는 경우 
        print(0)
        continue