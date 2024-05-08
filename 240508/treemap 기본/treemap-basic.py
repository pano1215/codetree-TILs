from sortedcontainers import SortedDict

#add k v : (k, v) 쌍을 treemap에 추가합니다. key가 k, value가 v라는 뜻입니다. 
    #      이때 만약 동일한 k가 이미 존재한다면, v로 덮어씁니다.
#remove k : key가 k인 쌍을 찾아 treemap에서 제거합니다. 잘못된 입력은 주어지지 않습니다.
#find k : key가 k인 쌍이 treemap에 있는지를 판단합니다. 있다면 해당하는 value를 출력하고, 없다면 None을 출력합니다.
#print_list : treemap에 있는 쌍들을 key 기준으로 오름차순 정렬하여 각 value 값들만 공백을 사이에 두고 순서대로 출력합니다. 
              # 만약 treemap이 비어있다면 None을 출력합니다.

n = int(input())
sd = SortedDict() # treemap

for _ in range(n) :
    command = list(map(str, input().split()))
    
    if command[0] == 'add' :
        com = command[0]
        k = int(command[1])
        v = int(command[2])

        sd[k] = v
    elif command[0] == 'print_list' :
        if len(sd) > 0 :
            for key in sd :
                print(sd[key], end = ' ')
            print()
        else :
            print('None')
    else :
        com = command[0]
        k = int(command[1])

        if com == 'remove' :
            sd.pop(k)
        elif com == 'find' :
            if k in sd :
                print(sd[k])
            else :
                print('None')
    #print(sd)