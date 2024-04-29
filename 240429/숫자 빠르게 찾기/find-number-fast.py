n, m = map(int, input().split())
n_arr = list(map(int, input().split()))
idx = -1 # n_arr에 값이 없으면 -1을 출력해야 하기 때문에 -1로 설정 

# 해당 target_num의 위치찾기 함수 
def search_target_num(target_num) :
    # 전역함수로 사용 
    global idx 
    # target_num이 새로 입력될 때마다 -1로 설정해줘야 하기 때문에 재설정 
    idx = -1 

    ## right, left 설정
    right = n - 1
    left = 0

    while left <= right:
        ## right, left의 중간값으로 mid 설정
        mid = (right + left) // 2

        ## mid와 target_num 비교
        ## mid == t_n인 경우 : mid = idx
        if n_arr[mid] == target_num:
            idx = mid + 1
            break

        ## mid > target_num인 경우 : mid - 1 = right
        if n_arr[mid] > target_num : 
            right = mid - 1
        ## mid < t_n인 경우 : mid + 1 = left 
        elif n_arr[mid] < target_num : 
            left = mid + 1
        
    return idx 


# m번 target_num 입력받기
for time in range(m) :
    target_num = int(input())

    retrun_idx = search_target_num(target_num)
    print(retrun_idx)