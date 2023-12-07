# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
arr = [0] + list(map(int, input().split()))


# 문제에서 구하고자 하는 값을 반환합니다.
def get_answer(a1, a2):
    return_value = 0
    for i in range(a1, a2 + 1):
        return_value += arr[i]

    return return_value


for _ in range(m):
    a1, a2 = tuple(map(int, input().split()))
    print(get_answer(a1, a2))