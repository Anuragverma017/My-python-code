l=[1,2,3,4,5,6,7,8,9,10]
for i , item in enumerate(l):
    
    with open ("tablefile.txt","w")as f:
        f.write(f"The table of {i} is ")