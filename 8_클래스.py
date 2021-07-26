# 스타크래프트

# 일반유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        print("{0}유닛이 생성되었습니다." .format(self.name))

# 공격유닛 - 일반유닛을 상속
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name,self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 객체들
# 마린 : 공격 유닛, 군인, 총을 쏠 수 있음
# 탱크 : 공격 유닛, 탱크, 포를 쏠 수 있음, 일반 모드 / 시즈 모드
marine1 = Unit("마린",40)
marine2 = Unit("마린",40)
tank = Unit("탱크",150)

# 외부에서 멤버변수 접근
print("유닛 이름 : {0}, 공격력 : {1}" .format(marine1.name, marine1.hp))

# 클래스 확장
marine1.death = True
if marine1.death:
    print("{0}이 죽었습니다." .format(marine1.name))

# 파이어뱃 : 공격, 유닛 
firebat1 = AttackUnit("파이어뱃",50,16)
firebat2 = AttackUnit("파이어뱃",50,16)

firebat2.attack("5시")
firebat1.damaged(25)
firebat2.attack("5시")
firebat1.damaged(25)