# 변수 선언 및 입력:
a, b = tuple(map(int, input().split()))


# 온전수인지 아닌지 여부를 판단하는 함수를 작성합니다.
def judge_number(n):
    if n % 2 == 0:
        return False
    elif n % 10 == 5:
        return False
    elif n % 3 == 0 and n % 9 != 0:
        return False
    else:
        return True


cnt = 0

for i in range(a, b + 1):
    if judge_number(i):
        cnt += 1

print(cnt)