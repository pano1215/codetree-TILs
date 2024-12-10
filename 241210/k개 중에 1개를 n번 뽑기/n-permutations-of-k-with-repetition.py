from itertools import combinations

k, n = map(int, input().split())

temp = []

def start(num) :
    if len(temp) == n :
        for i in temp :
            print(i, end = ' ')
        print()
        return
    
    for i in range(1, k + 1) :
        temp.append(i)
        start(num + 1)
        temp.pop()
        
start(1)