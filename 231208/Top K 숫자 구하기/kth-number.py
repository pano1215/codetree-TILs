# 변수 선언 및 입력:
n, k = tuple(map(int, input().split()))
nums = list(map(int, input().split()))

# nums를 정렬합니다.
nums.sort()

# k번째 원소를 출력합니다.
print(nums[k - 1])