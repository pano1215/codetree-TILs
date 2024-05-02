n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 처음 등장하는 위치를 찾는 이진탐색 함수
def binary_search(target_num) : 
    # left right mid 설정
    left = 0
    right = n - 1
    idx = n # n으로 설정해야 다른 값들이 min_idx보다 작음 

    # left <= right일 때까지 반복함 
    while left <= right : 
        mid = (left + right) // 2

        if arr[mid] >= target_num :
            idx = min(idx, mid) + 1 # mid는 1부터 시작하는 순서와 1차이가 나기 때문에 여기서 +1해줌. 27번 라인에서 +1하면 -1 + 1이 되어서 0으로 return되기 때문에 여기서 +1해줘야함 
            right = mid - 1
        else : 
            left = mid + 1

    return idx # target_num의 위치 반환 

# target_num를 m번 입력받기 
target_arr = list(map(int, input().split()))
for i in range(m) :
    target_num = target_arr[i]

    if target_num not in arr : # 시간초과에 안 걸리기 위해서, 처음부터 arr에 target_num이 없으면 -1을 출력하고 다음으로 넘어감 
        print(-1)
        continue

    result = binary_search(target_num) # 처음 등장하는 위치를 찾는 이진탐색 함수 호출
    print(result)