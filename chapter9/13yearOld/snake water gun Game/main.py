

import random


computer= random.choice(['snake', 'water', 'gun'])
you= input("Enter your choice: snake, water, gun: ")

if computer==you:
    print(f"Draw You and computer chose same thing {computer}")
else:
    if computer=='snake' and you=='water':
        print(f"You lose, computer chose {computer}")
    elif computer=='water' and you=='snake':
        print(f"You win, computer chose {computer}")
    elif computer=='water' and you=='gun':
        print(f"You lose, computer chose {computer}")
    elif computer=='gun' and you=='water':
        print(f"You win, computer chose {computer}")
    elif computer=='gun' and you=='snake':
        print(f"You lose, computer chose {computer}")
    elif computer=='snake' and you=='gun':
        print(f"You win, computer chose {computer}")    