
# input은 자료형이 무조건 문자열
# 밑 형태로 형 변환을 잘 하지는 않음 > input.py에 형 변환 방식 적어둠!
inputNumber = int(input("입력: "))

if inputNumber % 2 == 0:
  print("짝수")
else:
  print("홀수")

# 3개를 입력 받아서 숫자 리스트로 변경 (무조건 띄워쓰기로 구분해서 입력 받음)
num1, num2, num3 = list(map(int, input("숫자 3개 입력: ").split(" ")))

if num1 % 4 == 0:
  print("num1은 4의 배수")
elif num2 % 4 == 0:
  print("num2는 4의 배수")
elif num3 % 4 == 0:
  print("num3는 4의 배수")
else:
  print("4의 배수 없음")
