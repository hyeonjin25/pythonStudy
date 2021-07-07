'''이렇게 하면
여러줄이
주석처리가 됨'''

'''
숫자
'''
print(5)
print(-10)
print(3.14)
print(3+4)


'''
문자
'''
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*8)


'''
참/거짓
'''
print(5>10)
print(10>5)
print(True)
print(False)
print(not False)
print(not(5>10))
print(3==5)
print(3==3)
print(3!=3)
print((3>0) and (3<5));  print((3>0) & (3<5))
print((3>0) or (3>5));  print((3>0) | (3>5))
print(5>4>3)


'''
변수
'''
animal="강아지"
name="나쵸"
age=9
is_audult = age >= 3
print("우리집 "+animal+"의 이름은 "+name+"에요.")
print("나이는 "+ str(age) +"살 이에요.")
print(str(name)+"는 어른일까요? "+str(is_audult))
print(name,"는 어른일까요? ",is_audult) # ,사용할 경우는 str로 바꿀필요없고 띄어쓰기가 들어감


