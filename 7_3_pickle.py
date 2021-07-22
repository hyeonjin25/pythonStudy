''' 프로그램 상에서 사용중인 데이터를 파일 형태로 저장해 줌 '''

import pickle

# wb -> binary로 쓰기
profile_file = open("profile.pickle","wb") # 인코딩 필요 없음
profile = {"이름":"김제니","나이":"22","취미":["노래","춤","연기"]}
print(profile)
pickle.dump(profile,profile_file) #profile에 있는 정보를 profile_file에 저장
profile_file.close()

# rb -> binary로 읽기
profile_file = open("profile.pickle","rb") # 인코딩 필요 없음
profile = pickle.load(profile_file) # file의 정보를 profile에 불러오기
print(profile)
profile_file.close()

# 더 간단하게 실행
# close 필요 없음
with open("profile.pickle", "rb") as profile_file: # file정보를 profile_file에 저장
    print(pickle.load(profile_file))

with open("study.txt","w",encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어용")
    
with open("study.txt","r",encoding="utf8") as study_file:
    print(study_file.read())