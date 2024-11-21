def moduleTest():
  print("메소드 모듈")

def moduleTest2():
  print("메소드 모듈2")

from dataclasses import dataclass

@dataclass
class StudentModule:
  name: str
  age: int

# import 하는 다른 파일에도 실행이 되지 않게 하기! > module.py에서 실행 안 됨
# test 할 때만 거의 사용
if __name__ == "__main__":
  moduleTest()
  moduleTest2()