with open("chapter9/donkey.txt", "r")as f:
    text=f.read()
    if "donkey" in text.lower():
        text=text.replace("donkey","monkey")
        with open("chapter9/donkey.txt", "w")as f:
            f.write(text)
        print("donkey word is replaced form the file with monkey")    
    else:
        print("No donkey keyword is present in the file.")      