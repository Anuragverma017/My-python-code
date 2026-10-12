l=["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
word=input("Enter a word to search: ")
def search(word):
    if word in l:
        l.remove(word)
        print(f"{word} has been removed from the list.")
    else:
        print(f"{word} is not in the list.")
    return print(f"The updated list is: {l}")

search(word)  