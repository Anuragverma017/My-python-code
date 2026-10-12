class student:
    def std(self):
        return print("anurag")

e=student()
e.std() #this is a way of calling method by its ()

# in property decorator 
# we convert method() into a veriable name (attribute)

class college:
    @property
    def  person(self):
        return print("IIT Delhi")

t=college()
t.person    # property is called by name of the veriable 
    