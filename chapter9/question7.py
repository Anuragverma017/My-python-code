# now i will findout that on which line the text was writend


with open("chapter9/log.txt","r")as f:
    lines=f.readlines()
    line_no=1
    for line in lines:
        if "python" in line:
            print(f"python word is present in the line no:{line_no}")
        else:
            line_no+=1    



