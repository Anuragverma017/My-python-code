words=["donkey", "monkey", "ganda"]

with open("chapter9/donkey.txt", "r")as f:
    read=f.read()
for word in words:
    read=read.replace(word,"#"*len(word))
with open("chapter9/donkey.txt", "w")as f:
    f.write(read)        