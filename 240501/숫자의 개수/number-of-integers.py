n, m = map(int, input().split())
n_arr = list(map(int, input().split()))

# target_num이 끝나는 마지막 위치 찾기 함수 - max_idx 
def max_bound(target_num) :
    left = 0 
    right = n - 1
    max_idx = -1 # -1로 세팅해야 다른 값들이 max_idx보다 작을 수 없음

    while left <= right : 
        mid = (left + right) // 2 # 가운데 위치 선택

        if n_arr[mid] == target_num : # n_arr[mid]의 값이 target_num와 같다면, 
            max_idx = max(mid, max_idx) # max로 갱신을 해야 target_num의 최대 위치를 알 수 있음 

        if n_arr[mid] <= target_num : # mid위치보다 target의 위치가 더 뒤에 있어야 최대 idx를 구할 수 있음 
            left = mid + 1 
        else : 
            right = mid - 1 
    
    return max_idx

# target_num이 시작하는 첫 번째 위치 찾기 함수 - min_idx
def lower_bound(target_num) :
    left = 0 
    right =  n - 1
    min_idx = n # 배열의 길이만큼(n)으로 설정해야 다른 idx보다 작을 것이기 때문에 n으로 설정

    while left <= right : # 이렇게 조건을 걸어야, left right가 배열에 target_num가 없다는걸 알고 끝날 수 있음
        mid = (left + right) // 2 # 가운데 위치 선택

        if n_arr[mid] == target_num : # n_arr[mid]의 값이 target_num와 같다면, 
            min_idx = min(mid, min_idx) # min_idx값을 mid로 갱신 : 그래야 target_num이 처음 나오는 위치를 알 수 있음 

        if n_arr[mid] >= target_num : # n_arr[mid]이 target_num보다 더 크다면
            right = mid - 1 # right 갱신 : mid - 1이어야 범위를 좀 더 축소할 수 있음  
        else :
            left = mid + 1 # left 갱신 : mid + 1이어야 범위를 좀 더 축소할 수 있음  

    return min_idx

# 숫자 m번 받기 - for
for _ in range(m) :
    target_num = int(input())
    min_idx = lower_bound(target_num) # target_num이 시작하는 첫 번째 위치 찾기 함수 호출 - min_idx
    max_idx = max_bound(target_num) # target_num이 끝나는 마지막 위치 찾기 함수 호출 - max_idx 
    diff = max_idx - min_idx + 1
    
    if diff < 0 : # -1 - 길이 + 1이기 때문에 배열에 target_num이 없으면 음수가 나옴  
        diff = 0 # 때문에 0으로 변경해줘야함 
    print(diff)