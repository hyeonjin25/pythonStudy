# 스타크래프트
from random import *

# 일반유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0}유닛이 생성되었습니다." .format(name))

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name,location,self.speed))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name,self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 공격유닛 - 일반유닛을 상속
class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))

# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    # 스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)" .format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용할 수 없습니다." .format(self.name))

# 탱크
class Tank(AttackUnit):
    # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능, 이동 불가
    seize_developed = False

    def __init__(self):
        super().__init__("탱크", 150, 1, 5)
        self.seize_mode = False

    def set_seiez_mode(self):
        if Tank.seize_developed == False:
            return
        
        # 현재 시즈모드가 아닐 때 -> 시즈모드 켜기
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True

        # 현재 시즈모드 일 때 -> 시즈모드 해제
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False


# 날 수 있는 유닛
class FlyableUnit:
    def __init__(self, flyingSpeed):
        self.flyingSpeed = flyingSpeed

    def fly(self, name, location):
        print("{0} : {1}방향으로 날아갑니다. [속도 {2}]"\
            .format(name,location,self.flyingSpeed))

# 공중 공격 유닛 클래스 -> 다중 상속
class FlyAttackUnit(AttackUnit, FlyableUnit):
    def __init__(self, name, hp, damage, flyingSpeed):
        AttackUnit.__init__(self, name, hp, 0, damage) #지상 speed 0
        FlyableUnit.__init__(self, flyingSpeed)

    #매소드 오버라이딩 -> 재정의해서 지상유닛과 같은 함수 사용할 수 있게 함
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 레이스
class Wraith(FlyAttackUnit):
    def __init__(self):
        FlyAttackUnit.__init__(self,"레이스", 30, 20, 5)
        self.clocked = False #클로킹 모드(해제 상태)
    
    def clocking(self):
        # 현재 클로킹모드가 아닐 때 -> 모드 켜기
        if self.clocked == False:
            print("{0} : 클로킹모드로 전환합니다.".format(self.name))
            self.clocked = True

        # 현재 클로킹모드 일 때 -> 모드 해제
        else:
            print("{0} : 클로킹모드를 해제합니다.".format(self.name))
            self.clocked = False

def game_start():
    print("[알림]새로운 게임을 시작합니다.")

def game_over():
    print("player : gg") # good game
    print("[player] 님이 게임에서 퇴장하셨습니다.")


# 실제 게임 시작
game_start()

# 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2기 생성
t1 = Tank()
t2 = Tank()

# 레이스 1기 생성
w1 = Wraith()

# 유닛 일괄 관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.seize_developed = True
print("탱크 시즈모드 개발이 완료되었습니다.")

# 공격 모드 준비 (마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
for unit in attack_units:
    if isinstance(unit, Marine): # 만들어진 객체가 특정 클래스의 인스턴스인지 확인
        unit.stimpack()
    if isinstance(unit, Tank):
        unit.set_seiez_mode()
    if isinstance(unit, Wraith):
        unit.clocking()

# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 공격
for unit in attack_units:
    unit.damaged(randint(5,21)) # 공격은 랜덤으로 받음 (1~20)

# 게임 종료
game_over()