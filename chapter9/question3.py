import os

os.makedirs("chapter9/13yearOld", exist_ok=True)

for i in range(1,21):
    with open(f"chapter9/13yearOld/{i}.txt", "w") as f:

        for j in range(1,11):
            multiply=str((f"{i} X {j} = {i*j}\n"))
            f.write(multiply)
    
        