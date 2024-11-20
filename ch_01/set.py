
#? set은 집합!
set1 = set()
set1 = {'a', 'b', 'c'}

# 하나만 집어서 가져나올 수 없음 (순서 X)
# print(set1['a'])
print(set1)

# 리스트로 변환해서 꺼내서 쓸 수 있음
# print(list(set1)) 

# 반복문은 허용 
for data in set1:
  if data == 'b':
    print(data)

# 합집합 (union 대신에 + 써도 됨)
set2 = {1, 2, 3, 4, 'a'}
set3 = set1.union(set2)
print(set3)

# 교집합 출력
print(set1 & set2)

# 중복이 제거되어 출력
set4 = {1, 1, 1, 2, 3, 4, 5, 5, 5}
print(set4)
set4 = set([1, 1, 1, 2, 3, 4, 5, 5, 5])
print(set4)

# 차집합 (왼쪽에 두는 수가 중요함)
print(set1 - set2)