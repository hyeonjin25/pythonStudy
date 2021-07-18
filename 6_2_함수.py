'''
기본값 넣기
'''
def profile(name, age = 23, main_lang = "파이썬"):
    print("이름: {0} 나이:{1}\t 주 사용 언어:{2}" \
        .format(name, age, main_lang)) #줄바꿈 할 떄는 역슬래시 후 엔터

profile("김제니")
profile("김지수", 24, "자바")
profile("박채영", main_lang="C언어", age=22) #순서 바꾸기


'''
가변인자 넣기
'''
def profile2(name, age, *lang):
     print("이름: {0} 나이:{1}" .format(name, age), end=" ") #끝날때 줄바꿈없음
     for l in lang:
         print(l, end=" ")
     print() #줄바꿈

profile2("김제니", 23, "python", "Java", "C", "C++", "C#")
profile2("김지수", 24, "python", "Java")
profile2("박채영", 22,  "C", "C++", "C#")

'''
지역변수와 전역변수
'''
gun = 10
def checkpoint(soldiers): #경계근무
    gun = 20
    #global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}" .format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}" .format(gun))
    return gun

print("전체 총 : {0}" .format(gun))
checkpoint(2)
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}" .format(gun))