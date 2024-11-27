name = '선하영'

print(name)

#? 문자열 사이에 문자열 추가 (join)
print(",".join(name))

#? f포맷, 표현식
print(f"{name}입니다.")

#? 문자열 안에서 찾고자 하는 문자열의 위치 반환
# find는 예외(오류) X (실행 O) > "-1"을 가져옴
# index는 예외(오류) O > 실행 X
print(name.find('이'))
# print(name.index('이'))

# 뒤에서부터 찾음
print(name.rfind('영'))
print(name.rindex('영'))

#? 문자열 안에 찾고자 하는 문자열의 개수
print(name.count('선'))

#? 문자열의 길이 
print(name.__len__())
print(len(name))

#? 문자열 양끝 공백 제거
print("  이름  ".strip())
# 왼쪽 공백 제거
print("  이름  ".lstrip())
# 오른쪽 공백 제거
print("  이름  ".rstrip())

#? 문자열 특정 부분 변경
print("010-1234/5678".replace("-", "").replace("/", ""))

#? 토큰으로 문자열을 리스트화 하기
print("선하영, 선하영1, 선하영2".split(", "))

address = "부산광역시 동래구 사직동 롯데캐슬 101동 101호"
addressList = address.split(' ')
address1 = addressList[0]
address2 = addressList[1]
address3 = " ".join(addressList[2:])

print(f"주소1: {address1}, 주소2: {address2}, 주소3: {address3}")
# \n: 줄바꿈
print(f"주소1: {address1}\n주소2: {address2}\n주소3: {address3}")
# ", ' 3개 사용해서 줄바꿈, tab까지 허용함 (모든 입력값을 허용함)
print(f"""주소1: {address1}
주소2: {address2}
주소3: {address3}""")

# 인덱싱, 슬라이싱
print(address[0])
# 0 인덱스부터 3 인덱스 전까지
print(address[0:3])
print(address[2:3])
# 시작 인덱스 지정하지 않으면 무조건 처음부터
print(address[:3]) 
# 끝 인덱스 지정하지 않으면 무조건 끝까지
print(address[4:]) 
print(address[-1:]) 
print(address[-3:]) 
print(address[-3:-1]) 
# 마이너스 인덱스부터 찾으면 플러스 인덱스로 찾을 수 없음
print(address[-3:4]) 
# 플러스 인덱스부터 찾으면 마이너스 인덱스로 찾을 수 있음
print(address[4:-3]) 

print(address[:address.find('시 ') + 1])
print(address[address.find('시 ') + 2:address.find('구' ) + 1])

print("*" * 20)
print("1. 회원가입")
print("2. 로그인")
print("*" * 20)

