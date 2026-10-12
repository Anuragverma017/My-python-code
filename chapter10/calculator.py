class calculator:
    def __init__(self):
        self.input=int(input("Enter your value for calculation : "))
        self.calculate_for=input("Enter what you want to do 'cube', 'square' or 'squareroot'")
        if "cube"==str(self.calculate_for):
            print(f"This is the cude",self.cube**3)
        elif "square"==str(self.calculate_for):
            print(f"The square is :{self.input**2}")
        else:
            print(f"The squareroot is : {self.calculate_for**1/2}")

calculate=calculator()



    