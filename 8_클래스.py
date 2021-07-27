# 스타크래프트

# 일반유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0}유닛이 생성되었습니다." .format(self.name))

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name,location,self.speed))

# 공격유닛 - 일반유닛을 상속
class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed)
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

# 객체들
# 마린 : 공격 유닛, 군인, 총을 쏠 수 있음
# 탱크 : 공격 유닛, 탱크, 포를 쏠 수 있음, 일반 모드 / 시즈 모드
marine1 = Unit("마린",40,20)
marine2 = Unit("마린",40,20)
tank = Unit("탱크",150,30)

# 외부에서 멤버변수 접근
print("유닛 이름 : {0}, 공격력 : {1}" .format(marine1.name, marine1.hp))

# 클래스 확장
marine1.death = True
if marine1.death:
    print("{0}이 죽었습니다." .format(marine1.name))

# 파이어뱃 : 공격, 유닛 
firebat1 = AttackUnit("파이어뱃",50,16,20)
firebat2 = AttackUnit("파이어뱃",50,16,20)

firebat2.attack("5시")
firebat1.damaged(25)
firebat2.attack("5시")
firebat1.damaged(25)

# 발키리 : 공중 공격 유닛
valkyrie = FlyAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")
valkyrie.move("3시")

# 벌쳐 : 지상유닛
vulture = AttackUnit("벌쳐", 80, 10, 20)
vulture.move("11시")
