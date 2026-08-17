# Write your solution here
from random import choice

def roll(die:str):
    die_a = [3,3,3,3,3,6]
    die_b = [2,2,2,5,5,5]
    die_c = [1,4,4,4,4,4]
    if die=="A":
        options = die_a
    if die=="B":
        options = die_b
    if die=="C":
        options = die_c
    return choice(options)



def play(die1: str, die2: str, times: int):
    win1 = 0
    win2 = 0
    tie = 0
    for i in range(0,times):
        roll_die1 = roll(die1)
        roll_die2 = roll(die2)
        if roll_die1>roll_die2:
            win1+=1
        elif roll_die1<roll_die2:
            win2+=1
        else:
            tie+=1
    return win1, win2, tie
        


if __name__ == "__main__":
    result = play("A", "B", 100)
    print(result)