sub1 = int(input("Enter marks of subject1: "))
sub2 = int(input("Enter marks of subject2: "))
sub3 = int(input("Enter marks of subject3: "))

total = (sub1 + sub2 + sub3) / 3

if (total<=50):
    print("You are fail and your grade is F")
elif(total>50 and total<=60):
    print("You are pass class with grade D")
elif(total>60 and total<=70):
    print("You are pass class with grade C")
elif(total>70 and total<=80):
    print("You are pass class with grade B")
elif(total>80 and total<=90):
    print("You are pass class with grade A")    
else:
    print("You are pass class with grade Ex")