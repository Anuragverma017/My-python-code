class programmer:
    work="coding"
    joinYear=2026
    timing="9 to 5"
    salary= 1500000
    name=str(input("Enter your Name :"))

    def __init__(self,name, work, joinYear, timing, salary):
        self.work=work
        self.joinYear=joinYear
        self.timing=timing
        self.salary=salary
        print(f"work is {work}, Timing is {timing}, joinYear is {joinYear} , Salary is {salary} and his name is {name} ")

harry=programmer("Anurag", "coding", 2028, "9 to 5", 1600000)
