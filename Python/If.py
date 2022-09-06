weather = "맑음"

if weather == "비":
    print("우산을 챙기세요.")
elif weather == "미세먼지":
    print("마스크를 챙기세요.")
else:
    print("날씨가 좋습니다.")

weather2 = input("오늘 날씨는?\n")

if weather2 == "비" or weather2 == "눈":
    print("우산을 챙기세요.")
elif weather2 == "미세먼지":
    print("마스크를 챙기세요.")
else:
    print("날씨가 좋습니다.")