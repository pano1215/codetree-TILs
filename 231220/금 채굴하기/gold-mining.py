import sys

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

max_num = -sys.maxsize
        
for k in range(50) :
    if k > n :
        break 
    for row in range(n) :
        for column in range(n) :
            gold = 0
            gold_num = 0
            mining = 0
            for rr in range(n) :
                for cc in range(n) :
                    if arr[rr][cc] == 1 and abs(row - rr) + abs(column - cc) <= k :
                        #print(row, column, rr, cc, abs(row - rr) + abs(column - cc), k)
                        gold += m 
                        gold_num += 1
                        #print(gold)
            #print('==================')
            mining = (k * k) + ((k + 1) * (k + 1))
            profit = gold - mining
            #print('gold : ', gold, 'mining : ', mining, 'profit : ', profit)
            if profit > 0 :
                max_num = max(max_num, gold_num)

print(max_num)