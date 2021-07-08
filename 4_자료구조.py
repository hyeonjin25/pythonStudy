''' 
리스트[] - list 
'''
subway=[10,20,30]
print(subway)
subway.append(40) #맨 뒤에 40 넣기
print(subway)
print(subway.index(20)) # 20의 index알기
subway.insert(1,50) # 1번째에 50넣기
print(subway)
print(subway.pop()) # 맨뒤 꺼내기
print(subway)
subway.append(20)
print(subway.count(20)) # 20의 개수 알기
subway.sort()
print(subway)
subway.reverse() # 순서 뒤집기
print(subway)
subway.clear() # 모두 지우기
print(subway)

mix_list=[10,"안녕",True] # 다양한 자료형 가능
print(mix_list)
list=["하이",20]
mix_list.extend(list) # 합치기
print(mix_list)


''' 
dictionary(사전) 
-> unique한 key
''' 
cabinet={3:"제니", "B-3":"지수", 7:"가영"}
print(cabinet[3])
print(cabinet["B-3"])
print(cabinet.get(3))
#print(cabinet[5]) # 오류 발생 후 종료
print(cabinet.get(5)) # None 출력 종료X
print(cabinet.get(5,"없음")) # 값이 없을 경우 "없음" 출력 종료X
# 존재여부 판단
print(3 in cabinet) # True
print(5 in cabinet) # False
# 교체, 삭제
cabinet[3] = "태리"
print(cabinet)
del cabinet[3]
print(cabinet)
# 출력
print(cabinet.keys()) # key들만 출력
print(cabinet.values()) # value들만 출력
print(cabinet.items()) # 둘다 출력
# 모두 지우기
cabinet.clear()
print(cabinet)


''' 
튜플
-> 값이 변경되지 않음, list보다 빠름
''' 
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])
# menu.add("생선까스") # 에러
(name, age, hobby) = ("태리", 20, "코딩") # 괄호 없어도 됨
print(name, age, hobby)


''' 
집합(set)
-> 중복이 안되고 순서가 없음
''' 
my_set = {1,2,3,3,3}
print(my_set) # 3은 한번만 나옴
java = {"제니","지수"}
python = set(["제니","태리"])
# java와 python의 교집합 출력
print(java & python) 
print(java.intersection(python))
# java와 python의 합집합 출력 (순서X)
print(java | python)
print(java.union(python))
# java와 python의 차집합 출력
print(java - python)
print(java.difference(python))
# 추가, 삭제
python.add("가영")
print(python)
python.remove("태리")
print(python)


'''
자료구조의 변경
'''
drink = {"커피","우유","주스"}
print(drink, type(drink))

drink = list(drink)
print(drink, type(drink))

drink = tuple(drink)
print(drink, type(drink))

drink = set(drink)
print(drink, type(drink))

