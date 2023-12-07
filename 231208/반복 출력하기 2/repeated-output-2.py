# 변수 선언 및 입력:
n = int(input())


def print_string(n): # 1부터 n번째 줄까지 문자열을 출력하는 함수
    if n == 0:       # n이 0이라면, 더 이상 진행하지 않고
        return       # 퇴각합니다.

    print_string(n - 1)   # 1부터 n - 1번째 줄까지 출력하는 함수
    print("HelloWorld")
    

print_string(n)