with open("chapter9/this.txt", "r")as f:
    read=f.read()
with open("chapter9/CopyOf_this.txt", "w")as f:    
    writeing=f.write(read)