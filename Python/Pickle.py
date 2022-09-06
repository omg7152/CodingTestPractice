
import pickle
profile_file = open("profile.pickle", "wb")
profile = {"이름" : "안세웅", "나이" : 27, "취미" : ["축구", "농구", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile 정보를 profile_file 에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # profile_file 의 정보를 profile 에 저장
print(profile)
profile_file.close()

