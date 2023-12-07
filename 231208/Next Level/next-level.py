# 클래스 선언
class User:
    def __init__(self, user_id="", level=0):
        self.user_id = user_id
        self.level = level

        
# 초기값을 이용하여 첫 번째 User 객체를 만들어 줍니다.
user1 = User()

# 값을 변경합니다.
user1.user_id = "codetree"
user1.level = 10

# 변수 선언 및 입력
user2_id, level2 = tuple(input().split())

# 초기값을 이용하여 두 번째 User 객체를 만들어 줍니다.
user2 = User()

# 값을 변경합니다.
user2.user_id = user2_id
user2.level = int(level2)

# 출력
print(f"user {user1.user_id} lv {user1.level}")
print(f"user {user2.user_id} lv {user2.level}")