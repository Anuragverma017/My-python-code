n = int (input("Enter a number "))

for j in range(1, n+1):
    for i in range(1, n+1):
        print("*"*(i), end=" ")
        i+=1
        print()