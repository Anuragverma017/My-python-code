
with open("chapter9/log.txt","r")as f:
    read=f.read()
    if "python" in read:
        print("the word python is present in the log file.")
