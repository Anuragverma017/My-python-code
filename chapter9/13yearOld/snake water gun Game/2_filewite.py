f = "this for writing inside the file, that i want to create "
file = open("chapter9/myfile.txt", "a")
file.write("This is the updated append text for the file and this will get appended to the file.")
file2 = open("chapter9/myfile.txt", "r")
print(file2.read())
file.close() # it is needed to close the file that is open but using with open we can avoid closing the file manually


print()
# with open is the best way to open and close a file .
with open("chapter9/myfile.txt", "r") as file:
    print(file.read())