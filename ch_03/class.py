
#? 클래스 > 변수, 메소드로 이루어짐

class User:
  username="aaaa"
  password="1234"
  name="선하영"
  email="aaaa@example.com"

# self 키워드 중요!! (자바에서 this 같은 개념)
  def getUserinfo(self, address):
  # 문자열 한번에 적기 ''' > tab 들어가면 안 됨 전체로 인식해서 tab도 인식
    return f'''
username: {self.username}
password: {self.password}
name: {self.name}
email: {self.email}
address: {address}
'''

# 객체 생성
user1 = User()
# 참조하는 것을 무조건 첫번째 매개변수로 가지도록 설계 (user1, "부산") 과 똑같은 것?
print(user1.getUserinfo("부산"))