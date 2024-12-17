n = int(input())
visited = [False] * (n + 1)

temp = []
def make_per(num) :
    #print('num :', num)
    if len(temp) == n :
        for e in temp :
            print(e, end = ' ')
        print()
        return 

    for i in range(1, n + 1) :
        if visited[i] :
            continue

        visited[i] = True
        temp.append(i)

        #print('temp :', temp)
        make_per(num + 1)

        visited[i] = False
        temp.pop()

make_per(1)