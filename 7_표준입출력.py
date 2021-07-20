print("Python","Java", "JS", sep=",", end="? ") 
# sep: 중간에 기호넣기
# end: 줄바꿈 없애고 문장의 끝에 기호 추가
print("무엇이 더 재미있을까요?")

import sys
print("Python", file=sys.stdout) #표준 출력
print("Python", file=sys.stderr) #표준 에러

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject, score)
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")
    #ljust() : 왼쪽 정렬
    #rjust() : 오른쪽 정렬

for num in range(1,21):
    print("대기번호 : " + str(num).zfill(3))
    #zfill : 0으로 채우기

answer = input("아무 값이나 입력하세요 : ") # 항상 문자열 형태로 저장됨
print("입력하신 값은 " + answer + "입니다.")
