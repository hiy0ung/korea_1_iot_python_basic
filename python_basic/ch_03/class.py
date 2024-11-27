
#? 클래스 > 변수, 메소드로 이루어짐
# 파이썬에서는 변수를 미리 정의 잘 안 함
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


user2 = User()
print(user2.getUserinfo("서울"))

# 생성자를 사용
# __init__(매개변수1, 매개변수2, ...)
class User2:
  
  # email, address는 필수값 아님, 값 안 넣으면 ""
  def __init__(self, username:str, password:str, name:str, email:str|None="", address:str|None=""):
    self.username = username
    self.password = password
    self.name = name
    self.email = email
    self.address = address

  def getUserinfo(self):
    return f'''
username: {self.username}
password: {self.password}
name: {self.name}
email: {self.email}
address: {self.address}
'''

user3 = User2(username="aaa", password="1234", name="선하영")
print(user3.getUserinfo())

user4 = User2(username="bbbb", password="5678", name="강감자", email="bbbb@example.com", address="서울")
print(user4.getUserinfo())

'''

Student 클래스 만들기
name - str (필수)
age - int (필수)
address - str (선택)
!선택값은 무조건 뒤로 빼기!

incrementAge()  -> 호출되면 무조건 age 1씩 증가

getStudentInfo() -> 학생 정보 전체 출력

'''

# 클래스 정의
# 클래스 안의 함수 정의에는 self 키워드 꼭 필요함!
class Student:
  # 생성자 함수 정의
  def __init__(self, name:str, age:int, address:str|None=""):
    self.name = name
    self.age = age
    self.address = address
  
#   def __str__(self):
#     return  f'''
# name = {self.name}
# age = {self.age}
# address = {self.address}
# '''

  def incrementAge(self):
    self.age += 1

  def getStudentInfo(self):
    return f'''
name = {self.name}
age = {self.age}
address = {self.address}
'''
  
student = Student("선하영", 10, "부산")
print(student.getStudentInfo())
student.incrementAge()
print(student.getStudentInfo())
student.incrementAge()
print(student.getStudentInfo())
student.incrementAge()
print(student.getStudentInfo())

# 생성자 생성의 또 다른 방법
# @dataclass annotation사용 / from - import문 직접 작성해야함!
from dataclasses import dataclass
@dataclass
class Student2:
  name: str
  age: int
  address: str | None=""

student2 = Student2("선하영", 15)
print(student2)