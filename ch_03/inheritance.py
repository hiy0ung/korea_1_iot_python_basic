from dataclasses import dataclass
from overrides import overrides

@dataclass
class Person:
  name: str
  age: int

  def move(self):
    print(f"""{self.name}({self.age})님이 움직입니다.""")

# 클래스 상속 (extends 키워드 X)
@dataclass
class Student(Person):
  score: int

  def study(self):
    print("공부를 합니다.")

# 자식 요소에서 부모 요소를 재정의해서 사용 가능 (덮어쓴다는 개념이 더 정확...?)
  @overrides
  def move(self):
    super().move() # 부모 클래스를 호출
    print("학생이 움직입니다.")

@dataclass
class Teacher(Person):
  subject: str

  def lesson(self):
    print("수업을 합니다.")

  def move(self):
    print("선생님이 움직입니다.")

# 생성되면서 메모리에 할당됨
# 상속 받는다는 것은 메모리 공간을 새로운 클래스 + 상속 받을 클래스를 합쳐서 메모리 공간을 확장 시킴
# teacher 클래스가 만들어지면 person 클래스가 같이 만들어지면서 그 person클래스를 teacher 클래스가 참조하는 개념
person = Person(name="사람", age=10)
student = Student(name="김학생", age=15, score=90)
teacher = Teacher(name="선생님", age=30, subject="python")

print(person)
print(student)
print(teacher)

# 자동으로 형 변환이 됨
person2:Person = student
print(person2)


person3:Teacher = person2
print(person3)

print(isinstance(person3, Student))
print(isinstance(person3, Teacher))

persons = [ person, student, teacher ]

for p in persons:
  p.move()
  if isinstance(p, Student):
    p.study()
  elif isinstance(p, Teacher):
    p.lesson()

