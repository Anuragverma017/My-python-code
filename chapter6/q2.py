print("Enter marks of three subjects, should not be negative: ")
subject1=int(input("Enter marks of subject1: "))
if subject1<0:
    print("marks should not be negative, re enter marks of subject1: ")
    subject1=int(input("Enter marks of subject1: "))

subject2=int(input("Enter marks of subject2: "))
if subject2<0:
    print("marks should not be negative, re enter marks of subject2: ")
    subject2=int(input("Enter marks of subject2: "))

subject3=int(input("Enter marks of subject3: "))
if subject3<0:
    print("marks should not be negative, re enter marks of subject3: ")
    subject3=int(input("Enter marks of subject3: "))

total=(subject1+subject2+subject3)/3
if total>=40 and subject1>=33 and subject2>=33 and subject3>=33:
    print("congratulations you are pass")
elif total<40:
    print("sorry you are fail due to total marks less than 40%")
elif subject1<33:
    print("sorry you are fail due to subject1 marks less than 33%")
elif subject2<33:
    print("sorry you are fail due to subject2 marks less than 33%")
elif subject3<33:
    print("sorry you are fail due to subject3 marks less than 33%")
elif subject1<33 and subject2<33:
    print("sorry you are fail due to subject1 and subject2 marks less than 33%")
elif subject1<33 and subject3<33:
    print("sorry you are fail due to subject1 and subject3 marks less than 33%")
elif subject2<33 and subject3<33:
    print("sorry you are fail due to subject2 and subject3 marks less than 33%")
else:
    print("sorry you are fail due to subject1, subject2 and subject3 marks less than 33%")                    


