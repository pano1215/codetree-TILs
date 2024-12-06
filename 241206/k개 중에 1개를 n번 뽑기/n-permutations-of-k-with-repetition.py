k, n = map(int, input().split())

temp = []

def Print(temp) :
    for t in temp :
        print(t, end = ' ')
    print()
    return 
    
def start(num) :
    if len(temp) == n :
        Print(temp)
        return 

    for i in range(1, k + 1) :
        temp.append(i)
        start(i + 1)
        temp.pop()

start(1)