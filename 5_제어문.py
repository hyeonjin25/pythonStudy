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

'''
while문
'''
customer = "토르"
index = 5
while index >= 1:
    print("{0}손님, 커피가 준비 됐습니다. {1}번 남았어요." .format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기 처분 되었습니다.")

person = "Unknown"
while person != customer:
    print("{0}손님, 커피가 준비 됐습니다." .format(customer))
    person = input("이름이 어떻게 되세요?")