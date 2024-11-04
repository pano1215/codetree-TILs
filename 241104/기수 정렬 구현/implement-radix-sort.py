def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # 기수는 10진수이므로 크기가 10인 배열 생성

    # 자릿수 기준으로 count 배열 채우기
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # count 배열을 누적합으로 변환하여 각 숫자의 위치 계산
    for i in range(1, 10):
        count[i] += count[i - 1]

    # output 배열을 채우며 안정 정렬 수행
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # 원래 배열에 정렬된 내용을 복사
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    # 최대값을 찾아 최대 자릿수만큼 반복
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# 입력
n = int(input())
arr = list(map(int, input().split()))

# 기수 정렬 수행
radix_sort(arr)

# 결과 출력
print(" ".join(map(str, arr)))