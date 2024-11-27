# 선언 및 초기화 방법
list1 = [1, 5, 4, 3, 4]
# list2 = list()

# 인덱싱, 슬라이싱 적용 가능
print(list1[0])
print(list1[0:2])

print(list1.index(3))


# print(list1.sort()) > 원본의 값이 변해버림  > 깊은 복사 해서 정렬
# 인덱스의 처음부터 끝까지를 슬라이싱해서 정렬 > 슬라이싱을 하면 새로운 배열에 담겨서 새로운 주소값이 생김
list2 = list1[:]
list2.sort()
print(list2) # [1, 3, 4, 4, 5]
print(list1) # [1, 5, 4, 3, 4]

list2.reverse() 
print(list2) # [5, 4, 4, 3, 1]

print(list2.pop(0)) # pop은 return 존재 > 5 (pop은 인덱스 번호를 사용해서 삭제)
print(list2) # [4, 4, 3, 1]

list2.remove(4) # remove는 반환 타입 X (remove는 값 자체를 사용해서 삭제)
print(list2) # [4, 3, 1] (같은 값이 여러 개 있으면 제일 앞에 있는 하나만 지움)

list1.insert(1, 10)
print(list1) # [1, 10, 5, 4, 3, 4]

list3 = list1.copy()
print(list3) # [1, 10, 5, 4, 3, 4]

list1.extend(list3)
print(list1) # [1, 10, 5, 4, 3, 4, 1, 10, 5, 4, 3, 4]

print(list3 + [1, 2, 3, 4]) # [1, 10, 5, 4, 3, 4, 1, 2, 3, 4]
print(list3 * 3) # [1, 10, 5, 4, 3, 4, 1, 10, 5, 4, 3, 4, 1, 10, 5, 4, 3, 4]

list4 = [1, "선하영", [10, 20], 3.14, [30, 40]]
print(list4) 

# [시작인덱스:끝인덱스:스텝]
# print(list4[2:5:2])
print(list4[2::2])