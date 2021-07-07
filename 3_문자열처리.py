 
'''
문자열
'''
sen = '나는 소녀입니다.'
print(sen)
sen2="파이썬은 쉬워요"
print(sen2)
sen3 =  """
나는 소녀이고, 
파이썬은 쉬워요
"""
print(sen3)


'''
문자열 슬라이싱
'''
jumin = "990120-1234567"
print("성별 : "+jumin[7])
print("연 : "+jumin[0:2]) # 0 ~ 2 직전까지
print("생년월일 : "+jumin[:6]) # 처음부터 6 직전까지
print("뒤 7자리 : "+jumin[7:]) # 7부터 끝까지
print("뒤 7자리(뒤에부터) : "+jumin[-7:]) # 뒤에서 7부터 끝까지


'''
문자열 처리
'''
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python","Java")) #문자열 바꾸기
index = python.index("n") # n이 문자열에서 몇번째에 위치
print(index)
index = python.index("n", index + 1) # 2번째 n이 문자열에서 몇번째에 위치
print(index)
print(python.find("n")) # index랑 비슷
print(python.find("Java")) # 없으면 -1반환
#print(python.index("Java")) # 없으면 오류
print(python.count('n')) # n이 몇번 나왔는지


'''
문자열 포맷
'''
#방법1
print("나는 %d살입니다." % 20) # 정수 값 넣기
print("나는 %s살입니다." % 20) # 정수 값 넣기
print("나는 %s을 좋아해요." % "파이썬") # 문자열 넣기
print("나는 %s색과 %s색을 좋아해요." % ("파란","빨간")) # 문자열 넣기
print("apple은 %c로 시작해요." % "a") # 문자 넣기

#방법2
print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요." .format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아해요." .format("파란","빨간"))

#방법3
print("나는 {age}살이며 {color}색을 좋아해요." .format(age=20, color="하늘"))

#방법4
age=20
color="노란"
print(f"나는 {age}살이고, {color}색을 좋아해요.")

#탈출 문자
print("백문이\n불여일견")
print("저는 \"학생\"입니다.") #문장 내에서 따옴표
print("안녕\\하이") #문장 내에서 \
print("Red Apple\rPine") #커서를 맨 앞으로 이동
print("Redd\bApple") #백스페이스(한글자 지움)
print("Red\tApple") #탭

#비밀번호 만들기 예제
site="http://naver.com"
st=site.replace("http://","") # http:// 제거
st=st[:st.index(".")] # .com 제거
pw=st[:3]+str(len(st))+str(st.count("e"))+"!"
print(pw)

