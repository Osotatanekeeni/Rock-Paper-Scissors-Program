##PYTHON ROCK, PAPER, SCISSORS GAME
import random
def rps():

    print("~~~~~~~~ WELCOME TO A ROCK PAPER SCISSORS GAME!!! ~~~~~~~~")
    print("-- RULES OF THE GAME: ")
    print("    Enter R for rock, P for paper and S for scissors")
    print("    You need a score of 5 to win the game")
    print()
        
    #Keep track of the CPU's score
    cpu_score = 0

    #Keep track of the player's score
    player_score = 0

    print("YOUR SCORE: " + str(player_score))
    print("CPU SCORE: " + str(cpu_score))
    print("BEGIN!")
    #Rock, Paper, Scissors choices
    choices = {'R', 'P', 'S'}

    
    while(cpu_score != 5 and player_score != 5):
        player_choice = input("Rock, Paper or Scissors: ")
        cpu_choice = random.choice(['R', 'P', 'S'])

        if (player_choice.upper() == cpu_choice):
            print("**************************")
            print("CPU Played: "+cpu_choice)
            print("Tie!")
            print()
            print("PLAYER SCORE: "+str(player_score))
            print("CPU SCORE: " + str(cpu_score))
            print("**************************")
        elif (player_choice.upper() not in choices):
            print()
            print("Invalid input! Try again")
            print()
        else:
            if (player_choice.upper() == 'R' and cpu_choice == 'P'):
                cpu_score = cpu_score + 1
                print("**************************")
                print("You played: Rock")
                print("CPU Played: Paper")
                print()
                print("CPU WINS THIS ROUND!")
                print("PLAYER SCORE: "+str(player_score))
                print("CPU SCORE: " + str(cpu_score))
                print("**************************")
            elif (cpu_choice == 'R' and player_choice.upper() == 'P'):
                player_score = player_score + 1
                print("**************************")
                print("You played: Paper")
                print("CPU Played: Rock")
                print()
                print("YOU WIN THIS ROUND!")
                print("PLAYER SCORE: "+str(player_score))
                print("CPU SCORE: " + str(cpu_score))
                print("**************************")
            elif (player_choice.upper() == 'R' and cpu_choice == 'S'):
                player_score = player_score + 1
                print("**************************")
                print("You played: Rock")
                print("CPU Played: Scissors")
                print()
                print("YOU WIN THIS ROUND!")
                print("PLAYER SCORE: "+str(player_score))
                print("CPU SCORE: " + str(cpu_score))
                print("**************************")
            elif (cpu_choice == 'R' and player_choice.upper() == 'S'):
                cpu_score = cpu_score + 1
                print("**************************")
                print("You played: Scissors")
                print("CPU Played: Rock")
                print()
                print("CPU WINS THIS ROUND!")
                print("PLAYER SCORE: "+str(player_score))
                print("CPU SCORE: " + str(cpu_score))
                print("**************************")
            elif (player_choice.upper() == 'P' and cpu_choice == 'S'):
                cpu_score = cpu_score + 1
                print("**************************")
                print("You played: Paper")
                print("CPU Played: Scissors")
                print()
                print("CPU WINS THIS ROUND!")
                print("PLAYER SCORE: "+str(player_score))
                print("CPU SCORE: " + str(cpu_score))
                print("**************************")
            elif (cpu_choice == 'P' and player_choice.upper() == 'S'):
                player_score = player_score + 1
                print("**************************")
                print("You played: Scissors")
                print("CPU played: Paper")
                print()
                print("YOU WIN THIS ROUND!")
                print("PLAYER SCORE: "+str(player_score))
                print("CPU SCORE: " + str(cpu_score))
                print("**************************")

            if (player_score == 5):
                print("**********  YOU WIN!  **********")
            if (cpu_score == 5):
                print("**********  CPU WINS!  **********")
                
                

rps()
                
            

