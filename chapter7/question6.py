num = int(input("Enter a number for fectorial: "))
fectorial=1
for i in range(1, num):
    fectorial=fectorial*(i+1)
    print(fectorial)
print("The fectorial of", num, "is", fectorial)    