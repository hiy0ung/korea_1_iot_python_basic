from src.entity.user_entity import User
from src.repository.user_repository import UserRepository
from src.view.signup import SignUpView


def main():
  signupView = SignUpView()

  while True:
    print("""
1. 회원가입
2. 사용자 조회
3. 사용자 전체 조회
4. 사용자 삭제   
q. 프로그램 종료 
""")
    selectedMenu = input("선택 >>> ")

    if selectedMenu in ("q", "Q"):
      print("프로그램을 종료합니다.")
      return

    elif selectedMenu == "1":
      signupView.showSignup()

    elif selectedMenu == "2":
      username = input("username >>> ")
      foundUser = UserRepository.findByUsername(username)
      print(foundUser if bool(foundUser) else "해당 사용자 이름의 정보가 존재하지 않습니다.")

    elif selectedMenu == "3":
      foundUsers = UserRepository.findAll()
      for user in foundUsers:
        print(user)

    elif selectedMenu == "4":
      username = input("username >>> ")
      foundUser = UserRepository.findByUsername(username)
      if not bool(foundUser):
        print("해당 사용자이름은 존재하지 않습니다.")
        continue
      password = input("password >>> ")
      if foundUser.password != password:
        print("비밀번호가 일치하지 않습니다.")
        continue

      if input("사용자를 삭제하시겠습니까? (y/n)") in ("y", "Y"):
        if UserRepository.delete(foundUser.userId) > 0:
          print(f'삭제된 사용자 정보 >>> {foundUser}')

  # newUser = User(username='bbbb',password='1234', name='김감자', email='bbbb@example.com')
  # userRepository = UserRepositoryStudy()
  # # userRepository.insert(newUser)
  # userRepository.findById(1)
  # userRepository.findAll()

  # username = input('사용자 이름: ')
  # password = input('비밀번호: ')
  # name = input('성명: ')
  # email = input('이메일: ')



  # registerUser = User(username= username, password=password, name=name, email=email)
  # repository = UserRepository()
  # existUser = repository.findByUsername(username)
  # if existUser:
  #   return
  #
  # repository.insert(registerUser)
  #
  # repository.findById(9)
  # repository.deleteUser(4)


  # UserRepository 클래스 생성
  # 1. username을 select해서 중복 username 검사
  # 2. username이 중복이면 이미 사용중인 사용자 이름입니다. 출력 후 프로그램 종료
  # 3. 중복이 아니면 사용자 정보 insert
  # 4. insert된 사용자 select하여 조회(userId)
  # 5. 해당 userId로 삭제



if __name__ == "__main__":
  main()