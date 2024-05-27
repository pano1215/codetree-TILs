n = int(input())
line_arr = [list(map(int, input().split())) for _ in range(n)]
visited = [False for _ in range(1001)] # 일단 10으로 해두고 1000으로 바꿔서 제출하기  
cnt = 0 # 안 겹치는 선분 수 cnt 

# 겹치는지 확인하는 함수
def overlab(x1, x2) :
    # if x1 == 500 and x2 == 967 :
    #     for i in range(x1, x2 + 1) :
    #         print(visited[i], end = ' ')
    return any(visited[i] for i in range(x1, x2 + 1))

# 방문한 곳 True 처리
def visited_true(x1, x2) :
    global cnt 
    for i in range(x1, x2 + 1) :
        visited[i] = True
    cnt += 1
    return visited

# 이미 방문한 곳은 리셋하기
def delete_line(x1, x2) :
    global cnt 
    for i in range(x1, x2 + 1) :
        visited[i] = False
    return visited

def select_line(idx) :
    global cnt 

    if idx == n :
        return 
        
    #print(visited)
    x1, x2 = line_arr[idx]
    if overlab(x1, x2) :
        #print('겹침')
        delete_line(x1, x2) 
        select_line(idx + 1)
    else : 
        #print('안 겹침')
        visited_true(x1, x2)
        select_line(idx + 1)
        delete_line(x1, x2) 

select_line(0)
print(cnt)