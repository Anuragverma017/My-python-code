with open("chapter9/this.txt")as f:
    reading=f.read()
    
with open("chapter9/Copyof_this.txt")as f:
    reading2=f.read()

if(reading==reading2):
    print("this files are identicals")
else:
    print("No this files are not identicals or equal")        
