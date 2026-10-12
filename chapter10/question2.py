import math
number=int(input("Enter the nubmer you want for calculation :"))
choise=str(input("What you want to do chose any one (square , cube or squareroot)"))

class calculator:
    def squareOf(self, square):
        print(f"The Square of given number is {square*square}")

    def squareRootOf(self, root):
        print(f"The Square root of a given number is {math.sqrt(root)}")

    def cubeOf(self, cube):   
        print(f"The cube of {cube} number is :{cube*cube*cube}")  

number_calculating=calculator()
if (choise=="square"):
    number_calculating.squareOf(number)
elif(choise=="squareroot"):
    number_calculating.squareRootOf(number)
elif(choise=="cube"):
    number_calculating.cubeOf(number) 
else:
    print("Please re run the program, their is an error")           
