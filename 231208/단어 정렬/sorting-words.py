# 변수 선언 및 입력
n = int(input())
word_list = [
    input()
    for _ in range(n)
]

# 문자열 정렬
word_list.sort()

for word in word_list:
    print(word)