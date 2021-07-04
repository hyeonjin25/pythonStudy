# # 숫자
# # print(5)
# # print(-10)
# # print(3.14)
# # print(3+4)

# # 문자
# print('풍선')
# print("나비")
# print("ㅋㅋㅋㅋㅋㅋ")
# print("ㅋ"*8)

# # 참/거짓
# print(5>10)
# print(10>5)
# print(True)
# print(False)
# print(not False)
# print(not(5>10))
# print(3==5)
# print(3==3)
# print(3!=3)
# print((3>0) and (3<5));  print((3>0) & (3<5))
# print((3>0) or (3>5));  print((3>0) | (3>5))
# print(5>4>3)

# # 변수
# animal="강아지"
# name="나쵸"
# age=9
# is_audult = age >= 3
# print("우리집 "+animal+"의 이름은 "+name+"에요.")
# print("나이는 "+ str(age) +"살 이에요.")
# print(str(name)+"는 어른일까요? "+str(is_audult))
# print(name,"는 어른일까요? ",is_audult) # ,사용할 경우는 str로 바꿀필요없고 띄어쓰기가 들어감

# '''이렇게 하면
# 여러줄이
# 주석처리가 됨'''

# # 연산
# print(2**3) #2^3=8
# print(5/3)
# print(5%3) #5/3의 나머지
# print(5//3) #5/3의 몫

# #숫자처리 함수
# print(abs(-5)) #절댓값
# print(pow(4,2)) #4의 2제곱
# print(max(5,12)) #최댓값 찾기
# print(min(5,12)) #최솟값 찾기
# print(round(3.14)) #반올림

# from math import *
# print(floor(4.99)) #내림
# print(ceil(3.14)) #올림
# print(sqrt(16)) #제곱근

# #랜덤 함수
# from random import *
# print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
# print(random()*10) # 0.0 ~ 10.0 미만의 임의의 값 생성
# print(int(random()*10)) # 0 ~ 10 미만의 임의의 값 생성
# print(int(random()*10 + 1)) # 0 ~ 10 이하의 임의의 값 생성
# print(randrange(1,45)) # 1 ~ 45 미만의 임의의 값 생성
# print(randint(1,45)) # 1 ~ 45 이하의 임의의 값 생성
 
# #문자열
# sen = '나는 소녀입니다.'
# print(sen)
# sen2="파이썬은 쉬워요"
# print(sen2)
# sen3 =  """
# 나는 소녀이고, 
# 파이썬은 쉬워요
# """
# print(sen3)

# #문자열 슬라이싱
# jumin = "990120-1234567"
# print("성별 : "+jumin[7])
# print("연 : "+jumin[0:2]) # 0 ~ 2 직전까지
# print("생년월일 : "+jumin[:6]) # 처음부터 6 직전까지
# print("뒤 7자리 : "+jumin[7:]) # 7부터 끝까지
# print("뒤 7자리(뒤에부터) : "+jumin[-7:]) # 뒤에서 7부터 끝까지

# #문자열 처리
# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python","Java")) #문자열 바꾸기
# index = python.index("n") # n이 문자열에서 몇번째에 위치
# print(index)
# index = python.index("n", index + 1) # 2번째 n이 문자열에서 몇번째에 위치
# print(index)
# print(python.find("n")) # index랑 비슷
# print(python.find("Java")) # 없으면 -1반환
# #print(python.index("Java")) # 없으면 오류
# print(python.count('n')) # n이 몇번 나왔는지

# #문자열 포맷
# #방법1
# print("나는 %d살입니다." % 20) # 정수 값 넣기
# print("나는 %s살입니다." % 20) # 정수 값 넣기
# print("나는 %s을 좋아해요." % "파이썬") # 문자열 넣기
# print("나는 %s색과 %s색을 좋아해요." % ("파란","빨간")) # 문자열 넣기
# print("apple은 %c로 시작해요." % "a") # 문자 넣기

# #방법2
# print("나는 {}살입니다." .format(20))
# print("나는 {}색과 {}색을 좋아해요." .format("파란","빨간"))
# print("나는 {1}색과 {0}색을 좋아해요." .format("파란","빨간"))

# #방법3
# print("나는 {age}살이며 {color}색을 좋아해요." .format(age=20, color="하늘"))

# #방법4
# age=20
# color="노란"
# print(f"나는 {age}살이고, {color}색을 좋아해요.")