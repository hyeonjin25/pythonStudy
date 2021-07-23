# 스타크래프트

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0}유닛이 생성되었습니다." .format(self.name))
        print("체력 {0}, 공격력 {1}\n" .format(self.hp, self.damage))

# 객체들
# 마린 : 공격 유닛, 군인, 총을 쏠 수 있음
# 탱크 : 공격 유닛, 탱크, 포를 쏠 수 있음, 일반 모드 / 시즈 모드
marine1 = Unit("마린",40,5)
marine2 = Unit("마린",40,5)
tank = Unit("탱크",150,35)

# 외부에서 멤버변수 접근
print("유닛 이름 : {0}, 공격력 : {1}" .format(marine1.name, marine1.hp))

# 클래스 확장
marine1.death = True
if marine1.death:
    print("{0}이 죽었습니다." .format(marine1.name))