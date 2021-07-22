# print("Python","Java", "JS", sep=",", end="? ") 
# # sep: 중간에 기호넣기
# # end: 줄바꿈 없애고 문장의 끝에 기호 추가
# print("무엇이 더 재미있을까요?")

# import sys
# print("Python", file=sys.stdout) #표준 출력
# print("Python", file=sys.stderr) #표준 에러

# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     print(subject, score)
# for subject, score in scores.items():
#     print(subject.ljust(8), str(score).rjust(4), sep=":")
#     #ljust() : 왼쪽 정렬
#     #rjust() : 오른쪽 정렬

# for num in range(1,21):
#     print("대기번호 : " + str(num).zfill(3))
#     #zfill : 0으로 채우기

# answer = input("아무 값이나 입력하세요 : ") # 항상 문자열 형태로 저장됨
# print("입력하신 값은 " + answer + "입니다.")

# 빈자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))
# 양수일 떄는 +로 표시, 음수일 떈 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
# 왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<10}".format(500))

# 3자리마다 콤마찍기
print("{0:,}" .format(100000000000))
print("{0:+,}" .format(100000000000))
print("{0:+,}" .format(-100000000000))
# 3자리마다 콤마찍고, 부호 붙이면서, 왼쪽정렬로, 30자리 가지고, 빈칸 ^로 채우기
print("{0:^<+30,}" .format(-100000000000))

# 소수점 출력
print("{0:f}" .format(5/3))
# 소수점 둘째 자리수 까지만 출력 (소수점 셋째 자리에서 반올림)
print("{0:.2f}" .format(5/3))