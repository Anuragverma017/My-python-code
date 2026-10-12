post=str("This is a post and this post contain a word that is harry because i watch his python tutorial and i am learning python from that tutorial and this is a good tutorial for learning python")

input = str(input("Enter a word to search in the post: "))
if (input in post):
    print("The word is present in the post")
else:
    print("The word is not present in the post, sorry"  )