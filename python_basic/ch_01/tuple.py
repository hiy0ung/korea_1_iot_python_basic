print()
#? 리스트랑 동일한 구조(값의 추가, 수정, 삭제 불가능)
# 리스트의 순서나 값이 변하지 않아야 할 때 사용
tuple1 = ()
tuple1 = tuple()

tuple1 = (1, 2, 3)
print(tuple1[1:])

tuple1 = tuple1 * 3
print(tuple1)

# tuple1.append(10) > append 사용 불가 (추가 불가)
# print(tuple1)

#! 값을 1개만 넣고 싶을 때는 ,를 뒤에 꼭 붙여줘야함
tuple2 = (10,)
# 괄호 생략 가능
tuple3 = 1, 2, 3

#? 함수 표기법 (def 함수명(매개변수1, 매개변수2...): 구현부)
# python 은 중괄호 대신 : 사용
# 들여쓰기가 되면 함수 안에서 정의
def add(n1, n2, n3): 
  # 리턴이 여러 개가 가능("tuple" 형태가 가능하기 때문에 > 괄호가 생략된 형태)
  return n1 + n2, n2 + n3, n1 + n3 
  # 리스트로 받고 싶으면 
  # return [n1 + n2, n2 + n3, n1 + n3] 

print(add(10, 20, 30))


numbers = [1, 2, 3]
a, b, c = numbers