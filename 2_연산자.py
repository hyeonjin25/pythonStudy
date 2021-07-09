'''
연산
'''
print(2**3) #2^3=8
print(5/3)
print(5%3) #5/3의 나머지
print(5//3) #5/3의 몫


'''
숫자처리 함수
'''
print(abs(-5)) #절댓값
print(pow(4,2)) #4의 2제곱
print(max(5,12)) #최댓값 찾기
print(min(5,12)) #최솟값 찾기
print(round(3.14)) #반올림

from math import *
print(floor(4.99)) #내림
print(ceil(3.14)) #올림
print(sqrt(16)) #제곱근


'''
랜덤 함수
'''
from random import *
print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random()*10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random()*10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random()*10 + 1)) # 0 ~ 10 이하의 임의의 값 생성
print(randrange(1,45)) # 1 ~ 45 미만의 임의의 값 생성
print(randint(1,45)) # 1 ~ 45 이하의 임의의 값 생성

list = [1,2,3,4,5]
print(list)
shuffle(list) #무작위로 순서 섞음
print(list)
print(sample(list,1)) # list에서 1개 뽑음