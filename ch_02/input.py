# num1 = int(input("숫자1: "))
# num2 = int(input("숫자2: "))

#! 10, 20 / 10 20 형태로 입력 받아서 숫자형 리스트로 변환
num1AndNum2Input = input("숫자1, 숫자2: ").replace(",", "").split(" ")
num1AndNum2 = list(map(int, num1AndNum2Input))
print(num1AndNum2)

# 구조분해할당 (비구조할당)
num1, num2 = num1AndNum2
print(num1)
print(num2)

# int 함수를 호출해서 형 변환
# int('1')

# 문자열 리스트를 map으로 순회하면서 새로운 배열을 객체형태로 만든 것을 list 자료형으로 변환 시켜서 숫자형 리스트로 반환
# map(사용할함수, 배열)
nums = ['1', '2', '3', '4']
nums2 = list(map(int, nums))
print(nums2) # [1, 2, 3, 4]

# parseInt함수를 정의해서 사용
def parseInt(strNum):
  return int(strNum)

nums3 = list(map(parseInt, nums))
print(nums3) # [1, 2, 3, 4]

# lambda 사용 map(lambda 매개변수: 리턴값, 순회할리스트)
nums4 = list(map(lambda strNum: int(strNum), nums))
print(nums4) # [1, 2, 3, 4]