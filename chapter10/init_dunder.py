class employee:


    name="employee"
    langugage="JS"
    salary=1200000

    def __init__(self, name, language, salary):
        self.name= name
        self.language= language
        self.salary= salary

harry =employee("anurag", "python", 1300000)
print(f"name is {harry.name}. Language  is{harry.language} and salary is {harry.salary} ")

