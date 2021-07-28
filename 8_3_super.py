class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

# Flyable이 첫번째 파라미터 이므로 super사용시 Flyable만 실행
class FlyableUnit(Flyable, Unit):
    def __init__(self):
        super().__init__()

# 둘 다 사용위해서는 super 사용 X
class FlyableUnit2(Flyable, Unit):
    def __init__(self):
        Unit.__init__(self)
        Flyable.__init__(self)

dropship = FlyableUnit() 
dropship2 = FlyableUnit2() 