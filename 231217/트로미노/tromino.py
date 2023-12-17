import sys

row, column = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(row)]

#     ㄴ        ㄱ       ㅢ       ㅣㅡ     ㅣ        ㅡ
dx = [0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 2, 0, 0, 0]
dy = [0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 2]

def in_range(x, y) : # 격자에서 벗어나는지 여부 확인
    return x >= 0 and x < row and y >= 0 and y < column

max_num = -sys.maxsize # 최솟값 설정 - max 비교하기 위해 선언

for r in range(row) : # row 순회
    for c in range(column) : # column 순회
        sum_temp = 0 # 값들을 설정하기 위한 변수 선언
        for xy in range(len(dx)) : # 도형의 모형 배열 순회
            if xy % 3 == 0 : # 각 도형의 배열을 3번째 idx마다 설정했기 때문에 3의 배수로 
                sum_temp = 0 # 초기화해줘야함

            if in_range(r + dx[xy], c + dy[xy]): # 격자 안에 들어간다면 true
                sum_temp += arr[r + dx[xy]][c + dy[xy]] # arr의 요소 더하기
            max_num = max(max_num, sum_temp) # 최댓값 비교
            
print(max_num)