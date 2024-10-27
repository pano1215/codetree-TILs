n = int(input())
meetings = [list(map(int, input().split())) for _ in range(n)]
meetings = sorted(meetings, key = lambda x : x[1])

conformed_meeting = []
conformed_meeting.append([-1, -1])
for meeting in meetings :
    start_time = meeting[0]
    end_time = meeting[1]

    #print(conformed_meeting[-1][1])
    if start_time >= conformed_meeting[-1][1] : 
        conformed_meeting.append(meeting)

print(n - len(conformed_meeting) + 1)