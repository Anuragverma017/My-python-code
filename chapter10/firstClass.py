class job:
    salary= 1200000
    language= "py"

    def __init__(self):
        print("this is a dunder method , which call itself by default")

    def employee(self):
        print(f"this is using the parameter writen by self , will get changed by given parameters {self}")
anurag=job()
anurag.employee()