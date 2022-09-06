gun = 20

def checkPoint(soldiers):
    global gun
    gun -= soldiers
    print("남은총 : " + str(gun) + "정")

def checkPoint2(gun, soldiers):
    gun -= soldiers
    print("남은총 : " + str(gun) + "정")

print("전체총 : " + str(gun) + "정")

checkPoint(2)
checkPoint2(gun, 2)