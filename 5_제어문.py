# '''
# if문
# '''
# weather = input("오늘 날씨는 어때요?")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요.")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요.")
# else:
#     print("준비물 필요 없어요.")

# '''
# for문
# '''
# for wait in [0,1,2,3,4]:
#     print("대기번호 : {0}" .format(wait))

# for wait in range(1,6):
#     print("대기번호 : {0}" .format(wait))


# '''
# while문
# '''
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}손님, 커피가 준비 됐습니다. {1}번 남았어요." .format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기 처분 되었습니다.")

# person = "Unknown"
# while person != customer:
#     print("{0}손님, 커피가 준비 됐습니다." .format(customer))
#     person = input("이름이 어떻게 되세요?")


# '''
# continue와 break문
# '''
# absent=[2,5] #결석
# no_book=[7] #책 없음
# for student in range(1,11): #1부터 10까지
#     if student in absent: #결석한 학생의 번호일 경우
#         continue
#     if student in no_book:
#         print("오늘 수업은 여기까지, {0}은 교무실로 따라와" .format(student))
#         break
#     print("{0}, 책을 읽어봐" .format(student))


''' 
한줄 for문
'''
#출석 번호가 1,2,3,4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
students=[1,2,3,4,5]
print(students)
students=[i+100 for i in students]
print(students)

#학생들 이름을 길이로 변화
students=["jennie","rose","jisu"]
students=[len(i) for i in students]
print(students)

#학생 이름을 대문자로 변환
students=["jennie","rose","jisu"]
students=[i.upper() for i in students]
print(students)