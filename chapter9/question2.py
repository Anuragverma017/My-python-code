import random

def game():
    with open ("chapter9/highscore.txt") as f:
        highscore= f.read()
        if highscore=="" :
            highscore=0
        else:
            highscore=int(highscore)

    score=random.randint(1,100)
    if score>highscore :
        with open ("chapter9/highscore.txt", "w") as f:
            f.write(str(score))
            print(f"The score is {score} and the high score is {highscore}")
    else:
        print(f"The score {score} is not grater then {highscore}")        

game()                                
