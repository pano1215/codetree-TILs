n, m = map(int, input().split())

temp = []

def print_ans() :
    for t in temp :
        print(t, end = ' ')
    print()
    return 

def start(num, cnt) :
    if len(temp) == m and cnt == m : 
        print_ans()
        return 

    for i in range(num, n + 1) :
        temp.append(i)
        start(i + 1, cnt + 1)
        temp.pop()

        #print('temp : ', temp)

start(1, 0)