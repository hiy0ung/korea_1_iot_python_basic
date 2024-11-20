
#? Map 자료형()
# key, value
# key 중복 X, 순서 X

dict1 = dict()
dict1 = {
  # key 값은 항상 문자열로 감싸야함
  "name": "선하영",
  "age": 27,
  "state": "지쳤음"
}

print(dict1)

# list와 tuple은 key 값이 인덱스 번호!
list1 = ['a', 'b', 'c']
tuple1 = ('a', 'b', 'c')
dict1 = { '10':'a', '20':'b', '30':'c' }

print(list1[0])
print(tuple1[0])
print(dict1['10'])

#? dict 쌍 추가
dict1['40'] = 'd'
print(dict1) # {'10': 'a', '20': 'b', '30': 'c', '40': 'd'}
dict1.update({ '40':'e', '50':'f' })
print(dict1)
dict1['40'] = 'g'
print(dict1)

# value 조회
print(dict1.get('20'))
print(dict1['20'])

# 쌍 삭제
print(dict1.pop('30')) # c
print(dict1) # {'10': 'a', '20': 'b', '40': 'g', '50': 'f'}

# list안에 tuple 형태로 들어가있음
print(dict1.items())

#? python에서 반복문
for item in dict1.items():
  print(item) 
  # key와 value값 뽑아서 사용 가능
  # print(item[0]) > key 값

# key 값 바로 들고 오기
for key in dict1.keys():
  print(key)

# value 값 바로 들고 오기
for value in dict1.values():
  print(value)

# 인덱싱, 슬라이싱 다 가능 > 리스트 형태이기는 한데 리스트로 사용은 할 수 없음(내장함수 사용 불가)
keys1 = dict1.keys()
print(keys1)

# 리스트로 사용하고 싶으면 형 변환을 해 주면 됨!
keys1 = list(dict1.keys())
print(keys1)