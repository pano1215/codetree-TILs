n = int(input())

visited = [False] * (n + 1)
pick = [] 

def make_per(num) :
    if len(pick) == n :
        for elem in pick : 
            print(elem, end = ' ')
        print()
        return 
    
    for i in range(1, n + 1) :
        if visited[i] :
            continue

        visited[i] = True
        pick.append(i) 

        make_per(num + 1)

        visited[i] = False
        pick.pop()

make_per(1)