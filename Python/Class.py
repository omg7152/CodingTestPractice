from random import *
# 유닛
class Unit:
    def __init__(self, name, hp, speed): # 생성자
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다." .format(self.name))

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]" .format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(Unit): # 상속
    def __init__(self, name, hp, speed, damage): # 생성자
        Unit.__init__(self, name, hp, speed) # Unit 생성자 호출
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 공격합니다. [공격력 : {2}]" .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다." .format(self.name, damage))
        self.hp -= damage
        if(self.hp <= 0):
            print("{0} : 파괴되었습니다." .format(self.name))
        else:
            print("{0} : 현재체력은 {1} 입니다." .format(self.name, self.hp))

# 공중 유닛
class FlyAbleUnit:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 : {2}]" .format(name, location, self.flying_speed))

# 공중 공격 유닛
class FlyAbleAttackUnit(AttackUnit, FlyAbleUnit): # 다중상속
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 속도 0
        FlyAbleUnit.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 건물 건설
class Building(Unit):
    def __init__(self, name, hp, location):
        super().__init__(name, hp, 0) # super 사용시 self 정보는 파라미터에 추가 X, 다중상속에서는 첫번째 부모클래스만 인식

# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    def stimpack(self):
        if(self.hp > 10):
            print("{0} : 스팀팩을 사용합니다. [HP 10 감소]" .format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용할 수 없습니다." .format(self.name))

# 탱크
class Tank(AttackUnit):
    seize_devlopment = False # 시즈모드 개발여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if self.seize_devlopment == False:
            return

        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다." .format(self.name))
            self.damage *= 2
            self.seize_mode = True
        else:
            print("{0} : 시즈모드를 해제 합니다." .format(self.name))
            self.damage /= 2
            self.seize_mode = False

# 레이스
class Wraith(FlyAbleAttackUnit):
    def __init__(self):
        FlyAbleAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False
    
    def clocking(self):
        if self.clocked == True:
            print("{0} : 클로킹 모드 해제 합니다." .format(self.name))
            self.clocked = False
        else:
            print("{0} : 클로킹 모드 설정 합니다." .format(self.name))
            self.clocked = True


def game_start():
    print("[알림] 새로운 게임을 시작 합니다.")

def game_over():
    print("Player : gg")
    print("[Player] 님이 게임에서 퇴장하였습니다.")

game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()


units = []
units.append(m1)
units.append(m2)
units.append(m3)
units.append(t1)
units.append(t2)
units.append(w1)

for unit in units:
    unit.move("1시")

Tank.seize_devlopment = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

for unit in units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()


for unit in units:
    unit.attack("1시")

for unit in units:
    unit.damaged(randint(5, 21))

game_over()






