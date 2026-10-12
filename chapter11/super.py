class programmer:
    def w1(self):
        print("this is a programmer class1 funtion")
class second(programmer):
    def __init__(self):
        print("this is a programmer class2 funtion")
class thirdclass(second):
    def w3(self):
        super().__init__()
        print("this is a programmer class3 funtion")

object=thirdclass()
object.w3()

        
