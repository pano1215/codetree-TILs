# itertools - product 가져오기
from itertools import product

# 값 입력받기 
command = list(input())

# calculate_expression 함수 
def calculate_expression(command, combination) :
    # 연산자와 피연산자를 순서대로 저장
    temp = []

    i = 0
    # i가 expression의 길이와 같아질 <= 때까지 반복함
    while i < len(command) : 
        # 알파벳일 경우
        if command[i].isalpha() :
            # 알파벳일 경우 주어진 값으로 대체
            temp.append(combination[command[i]])
        # 알파벳이 아닌 경우
        else :
            # 연산자일 경우 그대로 추가
            temp.append(command[i])
        i += 1

    # 모든 연산의 우선순위가 같으므로 왼쪽에서 오른쪽 순서대로 계산
    start_num = temp[0]
    i = 1
    while i < len(temp) :
        operator = temp[i]
        num = temp[i + 1]

        if operator == '+' :
            start_num += num
        elif operator == '-' :
            start_num -= num
        elif operator == '*' :
            start_num *= num
        i += 2

    return start_num

# maximize_expression(command) 함수 
def maximize_expression(command) : 
    # 사용된 알파벳만 추출하여 중복 제거
    values = set(filter(str.isalpha, command))

    # 최대값을 위한 비교값 설정 
    max_num = float('-inf')

    # 각 변수에 대해 1부터 4까지의 값을 부여하는 모든 경우의 수
    for idx in product(range(1, 5), repeat = len(values)) :
        
        # 여기서 알파벳과 숫자의 조합을 만들어 줌 
        combination = dict(zip(values, idx))

        # calculate_expression 호출 
        result = calculate_expression(command, combination) 

        # 최대값 찾기 
        max_num = max(result, max_num)
        
    # return
    return max_num
    
# 함수 호출 
print(maximize_expression(command))