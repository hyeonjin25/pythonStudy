'''
퀴즈
'''
# 댓글 단 사람 중 추첨해서 1명은 치킨, 3명은 커피 쿠폰
# 조건1: 댓글은 20명이 달았고, 아이디는 1~20
# 조건2: 무작위로 추첨하되, 중복 불가
# 조건3: random 모듈의 shuffle과 sample을 활용

from random import *

users = range(1,21) # 1부터 20까지 숫자 생성 -> 타입이 range가 됨
users = list(users) # -> 타입을 list로 바꿈
shuffle(users)
winners = sample(users, 4)
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}" .format(winners[0]))
print("커피 당첨자 : {0}" .format(winners[1:]))
print("-- 축하합니다. --")