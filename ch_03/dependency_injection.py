# 의존성 주입
from dataclasses import dataclass

# service가 repository에 의존
# 외부에서 만든 것을 의존성 주입해서 사용
@dataclass
class Repository:

  def insert(self, entity:dict):
    print(f"{entity} -> 데이터를 추가합니다.")

@dataclass
class Service:
  repository: Repository

  def __init__(self, repository:Repository):
    self.repository = repository

  def addData(self, dto:dict):
    entity = dto
    self.repository.insert(entity)

# 객체를 매번 생성해야하서 안 좋은 코드
# class Service:
#   repository = Repository()

#   def addData(self, dto:dict):
#     entity = dto
#     self.repository.insert(entity)

#   def addData(self, dto:dict):
#     entity = dto
#     self.repository.insert(entity)

#   def addData(self, dto:dict):
#     entity = dto
#     self.repository.insert(entity)

# 하나의 객체를 공유!
repository = Repository()
service = Service(repository)

service.addData({"name":"선하영", "age": 27})