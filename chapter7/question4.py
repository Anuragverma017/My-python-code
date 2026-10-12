num =int(input("Enter a number"))
prime=0
for i in range(num):
    if num%(i+1)==0:
        prime+=1

if prime>2:
    print("Not a prime number")
elif prime==1:
    print("1 is neither prime nor composite")    
else:
    print("This is a prime number")
