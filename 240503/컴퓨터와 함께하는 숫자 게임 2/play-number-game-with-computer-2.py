import sys
sys.setrecursionlimit(10**5)

m = int(input())
a, b = list(map(int, input().split()))

# m과 a~b까지의 범위 배열 만들기 
#m_arr = [num for num in range(1, m + 1)] # 메모리 초과 때문에 배열을 따로 만들지 않음 
#a_b_arr = [num for num in range(a, b + 1)]
min_cnt = sys.maxsize # 가장 적게 지속될 때를 구하기 위한 임시 변수
max_cnt = -sys.maxsize # 가장 오래 지속될 때를 구하기 위한 임시 변수 

# 이진탐색 함수 
def binary_search(target_num) : 
    # left right cnt 설정
    left = 1
    right = m
    cnt = 0 

    # left <= right일 때까지 반복함 
    while left <= right : 
        cnt += 1

        # mid 설정 
        mid = (left + right) // 2

        # 같다면 cnt return 
        if mid == target_num :
            return cnt

        if mid > target_num :
            right = mid - 1
        else : 
            left = mid + 1

    return cnt # cnt return 

#for i in a_b_arr :
while a <= b :
    # target_num 설정하기 
    target_num = a

    cnt = binary_search(target_num)

    max_cnt = max(max_cnt, cnt)
    min_cnt = min(min_cnt, cnt)

    a += 1

print(min_cnt, max_cnt)