### variables
import sys
from random import randint
winning_pot = 0

### functions
def initial_wager():
    print("Your options are:")
    print("snake eyes (combined roll of 2)")
    print("ace deuce (combined roll of 3)")
    print("yo (combined roll of 11)")
    print("boxcars (combined roll of 12)")
    print("hi lo (combined roll of 2 or 12)")
    print("three way (combined roll of 2, 3, or 12)")
    player_bet = input("What do you bet?")
    while player_bet not in ("snake eyes", "ace deuce", "yo", "boxcars", "hi lo", "three way"):
        print("Come on... what do ya bet?")
        player_bet = input("What'll it be?")
    if player_bet == "snake eyes":
        snake_eyes()
    elif player_bet == "ace deuce":
        ace_deuce()
    elif player_bet == "yo":
        yo()
    elif player_bet == "boxcars":
        boxcars()
    elif player_bet == "hi lo":
        hi_lo()
    elif player_bet == "three way":
        three_way()
    else:
        print("hmmm... somehow you broke the game... thanks a bunch!")

def wager():
    quit = input("Well, aren't you lucky? Type 'quit' to quit whilst you're ahead. Type anything else to continue playing...")
    if quit == "quit":
        print("might be a wise decision! You won £%s" % (winning_pot))
        sys.exit()
    else:
            print("Your options are:")
            print("snake eyes (combined roll of 2)")
            print("ace deuce (combined roll of 3)")
            print("yo (combined roll of 11)")
            print("boxcars (combined roll of 12)")
            print("hi lo (combined roll of 2 or 12)")
            print("three way (combined roll of 2, 3, or 12)")
            player_bet = input("What do you bet?")
            while player_bet not in ("snake eyes", "ace deuce", "yo", "boxcars", "hi lo", "three way"):
                print("Come on... what do ya bet?")
                player_bet = input("What'll it be?")
            if player_bet == "snake eyes":
                snake_eyes()
            elif player_bet == "ace deuce":
                ace_deuce()
            elif player_bet == "yo":
                yo()
            elif player_bet == "boxcars":
                boxcars()
            elif player_bet == "hi lo":
                hi_lo()
            elif player_bet == "three way":
                three_way()
            else:
                print("hmmm... somehow you broke the game... thanks a bunch!")

def snake_eyes():
    global winning_pot
    die1 = randint(1, 6)
    die2 = randint(1, 6)
    die3 = die1 + die2
    print("Dice say %s and %s" % (die1, die2))
    if die3 == 2:
        print("Congratulations...")
        winning_pot = winning_pot + 10
        wager()
    else:
        print("Ooh, unlucky, sucker! You lose, I keep the cash! Haha!")
        sys.exit()
    return winning_pot

def ace_deuce():
    global winning_pot
    die1 = randint(1, 6)
    die2 = randint(1, 6)
    die3 = die1 + die2
    print("Dice say %s and %s" % (die1, die2))
    if die3 == 3:
        print("Congratulations...")
        winning_pot = winning_pot + 10
        wager()
    else:
        print("Ooh, unlucky, sucker! You lose, I keep the cash! Haha!")
        sys.exit()
    return winning_pot

def yo():
    global winning_pot
    die1 = randint(1, 6)
    die2 = randint(1, 6)
    die3 = die1 + die2
    print("Dice say %s and %s" % (die1, die2))
    if die3 == 11:
        print("Congratulations...")
        winning_pot = winning_pot + 10
        wager()
    else:
        print("Ooh, unlucky, sucker! You lose, I keep the cash! Haha!")
        sys.exit()
    return winning_pot

def boxcars():
    global winning_pot
    die1 = randint(1, 6)
    die2 = randint(1, 6)
    die3 = die1 + die2
    print("Dice say %s and %s" % (die1, die2))
    if die3 == 12:
        print("Congratulations...")
        winning_pot = winning_pot + 10
        wager()
    else:
        print("Ooh, unlucky, sucker! You lose, I keep the cash! Haha!")
        sys.exit()
    return winning_pot

def hi_lo():
    global winning_pot
    die1 = randint(1, 6)
    die2 = randint(1, 6)
    die3 = die1 + die2
    print("Dice say %s and %s" % (die1, die2))
    if die3 == 2:
        print("Congratulations...")
        winning_pot = winning_pot + 5
        wager()
    elif die3 == 12:
        print("Congratulations...")
        winning_pot = winning_pot + 5
        wager()
    else:
        print("Ooh, unlucky, sucker! You lose, I keep the cash! Haha!")
        sys.exit()
    return winning_pot

def three_way():
    global winning_pot
    die1 = randint(1, 6)
    die2 = randint(1, 6)
    die3 = die1 + die2
    print("Dice say %s and %s" % (die1, die2))
    if die3 == 2:
        print("Congratulations...")
        winning_pot = winning_pot + 2
        wager()
    elif die3 == 3:
        print("Congratulations...")
        winning_pot = winning_pot + 2
        wager()
    elif die3 == 12:
        print("Congratulations...")
        winning_pot = winning_pot + 2
        wager()
    else:
        print("Ooh, unlucky, sucker! You lose, I keep the cash! Haha!")
        sys.exit()
    return winning_pot

### exposition
print("Psssst - hey, you, these kid games are fun and all, but do you want some real excitement?")
print("Interested? Okay, this is how it works!")
print("Two dice - I roll, you bet. If you win, you get cash.")
print("You can take the money and walk whenever you want, or keep playing for more money.")
print("But if you lose a bet, I keep the money.")
print("Got it?")
initial_wager()
