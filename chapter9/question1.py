with open("chapter9/poem.txt", "r") as f:
    poem = f.read()
if "twinkle" in poem:
    print("The poem contains the word 'twinkle'.")
else:
    print("The poem does not contain the word 'twinkle'.")    
# with open("chapter9/poem.txt", "r") as f:
#     content = f.read().lower()

# if "twinkle" in content:
#     print("Word is present")
# else:
#     print("Word is not present")