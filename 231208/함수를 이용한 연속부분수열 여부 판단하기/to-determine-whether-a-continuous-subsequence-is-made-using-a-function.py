# 변수 선언 및 입력:
n1, n2 = tuple(map(int, input().split()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))


# n번째 인덱스부터 시작하는 n2길이의 a수열과
# b수열이 완전히 일치하는지 확인합니다..
def is_same(n):
    for i in range(n2):
        if a[i + n] != b[i]:
            return False

    return True


# b가 a의 연속부분수열인지 확인합니다.
def is_subsequence():
    for i in range(n1 - n2 + 1):
        if is_same(i):
            return True
    
    return False


if is_subsequence():
    print("Yes")
else:
    print("No")