
'''
The program generates a random score between 1 and 100.

It reads the previous high score from the file hiscroe.txt.

If the file is empty, it assumes the previous high score is 0.

It then prints your current score.

If your current score is higher than the high score, it updates the file with the new high score.
'''

import random
def game(): 
    score = random.randint(1,100)
    with open("highscore.txt")as f:
        highscore=f.read()
        if(highscore!=""):
            highscore= int(highscore)
        else:
            highscore =0 
    print(f"your score : {score}")
    if(score>highscore):
        with open("highscore.txt","w")as f:
            f.write(str(score))

game()    
