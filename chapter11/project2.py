import random

guss_valu = random.randint(1, 100)

gussed = False
i = 0

while gussed == False:

    value = int(input("Enter the value: "))
    i += 1

    if value == guss_valu:
        gussed = True
        print(f"You guessed the correct value. You took {i} guesses")

    elif value < guss_valu - 10:
        print("Your input value is smaller. Give a bigger value")

    elif value < guss_valu - 5:
        print("Your input value is close to the guess value")

    elif value < guss_valu:
        print("Your input value is very close to the guess value")

    elif value > guss_valu + 10:
        print("Your input value is bigger. Give a smaller value")

    elif value > guss_valu + 5:
        print("Your input value is bigger but close to the guess value")

    elif value > guss_valu:
        print("Your input value is bigger but very close to the guess value")