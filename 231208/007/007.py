# 클래스 선언
class Spy:
    def __init__(self, secret_code, meeting_point, time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time


# 변수 선언 및 입력
s_code, m_point, time = tuple(input().split())

# 객체 생성
s = Spy(s_code, m_point, int(time))

# 출력
print(f"secret code : {s.secret_code}")
print(f"meeting point : {s.meeting_point}")
print(f"time : {s.time}")