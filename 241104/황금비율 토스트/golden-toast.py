from collections import deque
import sys
input = sys.stdin.read

def process_breads(n, m, breads, commands):
    # 초기 리스트를 커서를 기준으로 두 덱으로 나눔
    left = deque(breads)  # 커서 왼쪽의 빵들
    right = deque()       # 커서 오른쪽의 빵들, 초기에는 비어 있음

    for command in commands:
        if command == 'L':
            if left:
                right.appendleft(left.pop())
        elif command == 'R':
            if right:
                left.append(right.popleft())
        elif command == 'D':
            if right:
                right.popleft()
        elif command.startswith('P '):
            # command가 'P &'의 형태일 때 &를 추가해야 함
            _, char = command.split()
            left.append(char)
    
    # 최종 결과를 출력하기 위해 왼쪽과 오른쪽 덱을 병합
    result = ''.join(left) + ''.join(right)
    return result

# 입력 받기
data = input().strip().splitlines()
n, m = map(int, data[0].split())
breads = list(data[1])
commands = data[2:]

# 결과 계산 및 출력
output = process_breads(n, m, breads, commands)
print(output)