import random

def dice():
    return random.randint(1, 6)

count=0
while True:
    roll = dice()
    print(f" {count+1} Trial: {roll}")
    count+=1
    if roll == 6:
        break