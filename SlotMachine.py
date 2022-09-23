#slot machine game
import math
#variables
tokens = 0
print("Beverly's Super Fun Slot Machine!")

tokens = int(input("Enter the starting number of tokens you wish to use: "))
bet = 0

while bet < 4:
    bet = int(input("How much do you wish to bet? (Maximum of 3 tokens, or 4 to cash out): "))
#randomizer
    if (bet < 4):
        import random
        slot1 = random.randrange(1, 6)
        slot2 = random.randrange(1, 6)
        slot3 = random.randrange(1, 6)
        print("{", slot1, "}", "{", slot2, "}", "{", slot3, "}")
#if you win
        if slot1 == slot2 and slot2 == slot3:
            win = math.pow(slot1, bet)
            print("WINNER!")
            print("You win", win, "tokens!" )
            tokens += win
            print("Total tokens: ", tokens)
#if you lose
        else:
            print("Sorry, you lose", bet, "tokens.")
            tokens -= bet
            print("Total tokens: ", tokens)
#cash out
else:
    print("Thanks for playing!")