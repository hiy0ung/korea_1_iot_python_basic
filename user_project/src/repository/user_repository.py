from dataclasses import dataclass
from pymysql import cursors, connect
from src.config.database_config import DatabaseConfig
from src.entity.user_entity import User

# @dataclass
# class UserRepositoryStudy:
#
#   def insert(self, user: User):
#     connection = DatabaseConfig.getConnection()
#     cursor = connection.cursor()
#     # %s 자리만 채워주는 거!
#     sql = '''
# insert into user_tb
# values(default, %s, %s, %s, %s, now(), now())
# '''
#     insertCount = cursor.execute(query=sql, args=(user.username, user.password, user.name, user.email))
#     print(f'User데이터 추가 성공 {insertCount}건')
#     # 오토 커밋을 지원하지 않아서 꼭 커밋 메소드 사용해 줘야함!
#     connection.commit()
#
# # cursor() > sql에 들어감?
# # execute() > 번개모양 (sql문 실행)
#
#   def findById(self, user_id: int):
#     connection = DatabaseConfig.getConnection()
#     # dict 형태(key: value)로 들고 옴
#     # 만약 cursor()안에 아무 것도 지정 안 하면 튜플 형태로 순서대로 가지고 옴 > 인덱싱을 통해서 데이터를 꺼내야 함
#     cursor = connection.cursor(cursor=cursors.DictCursor)
#     sql = '''
#     select * from user_tb where user_id = %s
#     '''
#     # 튜플이기 때문에 매개변수 1개이면 ,로 끝내기
#     cursor.execute(query=sql, args=(user_id,))
#     result = cursor.fetchone()
#     print(result)
#     print(result.get('username'))
#
#     def findAll(self, user_id: int):
#       connection = DatabaseConfig.getConnection()
#       cursor = connection.cursor(cursor=cursors.DictCursor)
#       sql = '''
#       select * from user_tb
#       '''
#       # 튜플이기 때문에 매개변수 1개이면 ,로 끝내기
#       cursor.execute(query=sql)
#       result = cursor.fetchall()
#       print(result)

# @dataclass
# class UserRepository:
#   def insert(self, user: User):
#     connection = DatabaseConfig.getConnection()
#     cursor = connection.cursor()
#     sql = '''
#     insert into user_tb
#     values(default, %s, %s, %s, %s, now(), now())
#   '''
#     insertCount = cursor.execute(query=sql, args=(user.username, user.password, user.name, user.email))
#     print(f'User데이터 추가 성공 {insertCount}건')
#     connection.commit()
#
#   def findByUsername(self, username: str):
#     connection = DatabaseConfig.getConnection()
#     cursor = connection.cursor()
#     sql = '''
#     select * from user_tb where username = %s
#     '''
#     cursor.execute(sql, args=(username,))
#     result = cursor.fetchone()
#     if result:
#       print("이미 사용중인 사용자 이름입니다.")
#     connection.close()
#     return result
#
#   def findById(self, user_id: int):
#     connection = DatabaseConfig.getConnection()
#     cursor = connection.cursor(cursor=cursors.DictCursor)
#     sql = '''
#     select * from user_tb where user_id = %s
#     '''
#     cursor.execute(query=sql, args=(user_id,))
#     result = cursor.fetchone()
#     print(result)
#
#   def deleteUser(self, user_id: int):
#     connection = DatabaseConfig.getConnection()
#     cursor = connection.cursor(cursor=cursors.DictCursor)
#     sql = '''
#     delete from user_tb where user_id = %s
#     '''
#     cursor.execute(query=sql, args=(user_id,))
#     print(f'데이터 삭제 성공: {user_id}')
#     connection.commit()

# signup
class UserRepository:

  @staticmethod
  def delete(userId: int):
    successCount = 0
    try:
      connection = DatabaseConfig.getConnection()

      try:
        cursor = connection.cursor()
        sql = 'delete from user_tb where user_id = %s'
        successCount = cursor.execute(query=sql, args=(userId,))
        connection.commit()
      except Exception as e:
        print(e)
      finally:
        connection.close()
    except Exception as e:
      print("데이터베이스 연결 실패")

    return successCount

  @staticmethod
  def findAll():
    foundUsers = []

    try:
      connection = DatabaseConfig.getConnection()
      try:
        cursor = connection.cursor(cursor=cursors.DictCursor)
        sql = "SELECT * FROM user_tb order by user_id"
        cursor.execute(sql)
        rs = cursor.fetchall()
        if len(rs) > 0:
          # rs를 반복 돌려서 user를 하나씩 꺼내와서 리스트로 만들기 (rs는 튜플 타입 > list로 변경)
          foundUsers = list(map(lambda user: User(
            userId = user['user_id'],
            username=user['username'],
            password=user['password'],
            email=user['email'],
            createDate=user['create_date'],
            updateDate=user['update_date']
          ), rs))
      except Exception as e:
        print(e)
      finally:
        connection.close()
    except Exception as e:
      print("데이터베이스 연결 실패")

    return foundUsers


  @staticmethod
  def findByUsername(username: str):
    foundUser = None

    try:
      connection = DatabaseConfig.getConnection()
      try:
        cursor = connection.cursor(cursor=cursors.DictCursor)
        sql = "SELECT * FROM user_tb WHERE username = %s"
        cursor.execute(query=sql, args=(username,))
        rs = cursor.fetchone()
        # rs가 bool 자료형으로 바꿔서 false가 아닐 때 객체 생성
        if bool(rs):
          # User 객체를 생성 (커서에서 찾은 값이 snake방식이라 표기함!)
          foundUser = User(
            userId=rs['user_id'],
            username=rs['username'],
            password=rs['password'],
            email=rs['email'],
            createDate=rs['create_date'],
            updateDate=rs['update_date']
          )
      except Exception as e:
        print(e)
      finally:
        connection.close()
    except Exception as e:
      print(e)
      print("데이터베이스 연결 실패")

    return foundUser

  @staticmethod
  def saveUser(user: User):
    # connection이 try, finally에서 지역 변수로 존재 하기 때문에 밖에 빼서 쓸 수 있게 해줘야 함
    connection = None

    # db에 아예 접근하지 못했을 때 예외 처리 하는 구문
    try:
      connection = DatabaseConfig.getConnection()
      try:
        cursor = connection.cursor()
        sql = '''
          insert into user_tb values(default, %s, %s, %s, %s, now(), now())
        '''
        cursor.execute(query=sql, args=(user.username, user.password, user.name, user.email))
        # 마지막 auto_increment된 값을 가져옴
        user.userId = cursor.lastrowid
        # commit - 물리적 데이터베이스에 저장하는 역할?
        connection.commit()
      except Exception as e:
        print(e)
        print("사용자 정보 추가 실패!!")
      finally:
        connection.close()
    except Exception as e:
      print(e)

