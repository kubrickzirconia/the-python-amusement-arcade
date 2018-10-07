### setting up variable
lives_remaining = 3
### introduction to the quiz
print("Welcome to the Crazy Mad Quiz, World Cup 2018 edition!")
print("Think you followed the world cup closely?")
print("Take our quiz to test your knowledge!")
### question one
def question_one():
    global lives_remaining
    print("Question One")
    print("You have %s lives remaining" % (lives_remaining))
    print("Who won the golden boot?")
    print("a. Kylian M'bappe")
    print("b. Harry Kane")
    print("c. Eden Hazard")
    answer_one = input("Type a, b, or c...")
    while answer_one not in ('a', 'b', 'c'):
            print("error, please type a or b or c to answer")
            answer_one = input("Type a, b, or c...")
    if answer_one == "b":
            print("Correct answer! Next question...")
            return lives_remaining
    else:
        print("Wrong answer! You lose a life!")
        lives_remaining -= 1
        return lives_remaining
### question two
def question_two():
    global lives_remaining
    print("Question Two")
    print("You have %s lives remaining" % (lives_remaining))
    print("What was the score at half time in the England v Croatia semi final?")
    print("a. 1-2")
    print("b. 1-0")
    print("c. 0-0")
    answer_two = input("Type a, b, or c...")
    while answer_two not in ('a', 'b', 'c'):
        print("error, please type a or b or c to answer")
        answer_two = input("Type a, b, or c...")
    if answer_two == "b":
        print("Correct answer! Next question...")
        return lives_remaining
    else:
        print("Wrong answer! You lose a life!")
        lives_remaining -= 1
        return lives_remaining
### question three
def question_three():
    global lives_remaining
    print("Question Three")
    print("You have %s lives remaining" % (lives_remaining))
    print("M'bappe is the first teenager to score in a world cup final since...")
    print("a. Lionel Messi")
    print("b. Zinedine Zidane")
    print("c. Pele")
    answer_three = input("Type 'a', 'b', or 'c'...")
    while answer_three not in ('a', 'b', 'c'):
            print("error, please type a or b or c to answer")
            answer_three = input("Type a, b, or c...")
    if answer_three == "c":
        print("Correct answer! Next question...")
        return lives_remaining
    else:
        print("Wrong answer! You lose a life!")
        lives_remaining -= 1
        return lives_remaining
### question four
def question_four():
    global lives_remaining
    print("Question Four")
    print("You have %s lives remaining" % (lives_remaining))
    print("How far did reigning champions Germany make it in 2018?")
    print("a. They got knocked out at the group stages")
    print("b. They made the quarter finals")
    print("c. They were defeated by Mexico in the final 16")
    answer_four = input("Type 'a', 'b', or 'c'...")
    while answer_four not in ('a', 'b', 'c'):
            print("error, please type a or b or c to answer")
            answer_four = input("Type a, b, or c...")
    if answer_four == "a":
        print("Correct answer! Next question...")
        return lives_remaining
    else:
        print("Wrong answer! You lose a life!")
        lives_remaining -= 1
        return lives_remaining
### question five
def question_five():
    global lives_remaining
    print("Question Five")
    print("You have %s lives remaining" % (lives_remaining))
    print("Throughout the tournament, how many games resulted in a nil nil draw?")
    print("a. 4")
    print("b. 6")
    print("c. 1")
    answer_five = input("Type 'a', 'b', or 'c'...")
    while answer_five not in ('a', 'b', 'c'):
            print("error, please type a or b or c to answer")
            answer_five = input("Type a, b, or c...")
    if answer_five == "c":
        print("Correct answer! Next question...")
        return lives_remaining
    else:
        print("Wrong answer! You lose a life!")
        lives_remaining -= 1
        return lives_remaining
### question six
def question_six():
    global lives_remaining
    print("Question Six")
    print("You have %s lives remaining" % (lives_remaining))
    print("Who scored the first penalty awarded by VAR in a World Cup ever?")
    print("a. Antoine Griezmann against Australia")
    print("b. Diego Costa against Portugal")
    print("c. Harry Kane against Panama")
    answer_six = input("Type 'a', 'b', or 'c'...")
    while answer_six not in ('a', 'b', 'c'):
            print("error, please type a or b or c to answer")
            answer_six = input("Type a, b, or c...")
    if answer_six == "a":
        print("Correct answer! Next question...")
        return lives_remaining
    else:
        print("Wrong answer! You lose a life!")
        lives_remaining -= 1
        return lives_remaining
### question seven
def question_seven():
    global lives_remaining
    print("Question Seven")
    print("You have %s lives remaining" % (lives_remaining))
    print("The 2018 mascot, Zabikava, is based on which animal?")
    print("a. Wolf")
    print("b. Tiger")
    print("c. Cat")
    answer_seven = input("Type 'a', 'b', or 'c'...")
    while answer_seven not in ('a', 'b', 'c'):
            print("error, please type a or b or c to answer")
            answer_seven = input("Type a, b, or c...")
    if answer_seven == "a":
        print("Correct answer! Next question...")
        return lives_remaining
    else:
        print("Wrong answer! You lose a life!")
        lives_remaining -= 1
        return lives_remaining
### question eight
def question_eight():
    global lives_remaining
    print("Question Eight")
    print("You have %s lives remaining" % (lives_remaining))
    print("Which player won the Golden Ball?")
    print("a. Paul Pogba")
    print("b. Thibaut Courtois")
    print("c. Luka Modric")
    answer_eight = input("Type 'a', 'b', or 'c'...")
    while answer_eight not in ('a', 'b', 'c'):
            print("error, please type a or b or c to answer")
            answer_eight = input("Type a, b, or c...")
    if answer_eight == "c":
        print("Correct answer! Next question...")
        return lives_remaining
    else:
        print("Wrong answer! You lose a life!")
        lives_remaining -= 1
        return lives_remaining
### question nine
def question_nine():
    global lives_remaining
    print("Question Nine")
    print("You have %s lives remaining" % (lives_remaining))
    print("Which goal did fans vote as the 'Goal of the Tournament' on FIFA.com?")
    print("a. Toni Kroos against Sweden")
    print("b. Benjamin Pavard against Argentina")
    print("c. Jesse Lingard against Panama")
    answer_nine = input("Type 'a', 'b', or 'c'...")
    while answer_nine not in ('a', 'b', 'c'):
            print("error, please type a or b or c to answer")
            answer_nine = input("Type a, b, or c...")
    if answer_nine == "b":
        print("Correct answer! Final question...")
        return lives_remaining
    else:
        print("Wrong answer! You lose a life!")
        lives_remaining -= 1
        return lives_remaining
### question ten
def question_ten():
    global lives_remaining
    print("Question Ten")
    print("You have %s lives remaining" % (lives_remaining))
    print("Which country scored the most own goals throughout the tournament?")
    print("a. Nigeria")
    print("b. Egypt")
    print("c. Russia")
    answer_ten = input("Type 'a', 'b', or 'c'...")
    while answer_ten not in ('a', 'b', 'c'):
            print("error, please type a or b or c to answer")
            answer_ten = input("Type a, b, or c...")
    if answer_ten == "c":
        print("Correct answer!")
        return lives_remaining
    else:
        print("Wrong answer! You lose a life!")
        lives_remaining -= 1
        return lives_remaining
### executing the quiz
import sys
if lives_remaining > 0:
    question_one()
else:
    print("YOU HAVE 0 LIVES. UNLUCKY! YOU LOSE.")
    sys.exit()
if lives_remaining > 0:
    question_two()
else:
    print("YOU HAVE 0 LIVES. UNLUCKY! YOU LOSE.")
    sys.exit()
if lives_remaining > 0:
    question_three()
else:
    print("YOU HAVE 0 LIVES. UNLUCKY! YOU LOSE.")
    sys.exit()
if lives_remaining > 0:
    question_four()
else:
    print("YOU HAVE 0 LIVES. UNLUCKY! YOU LOSE.")
    sys.exit()
if lives_remaining > 0:
    question_five()
else:
    print("YOU HAVE 0 LIVES. UNLUCKY! YOU LOSE.")
    sys.exit()
if lives_remaining > 0:
    question_six()
else:
    print("YOU HAVE 0 LIVES. UNLUCKY! YOU LOSE.")
    sys.exit()
if lives_remaining > 0:
    question_seven()
else:
    print("YOU HAVE 0 LIVES. UNLUCKY! YOU LOSE.")
    sys.exit()
if lives_remaining > 0:
    question_eight()
else:
    print("YOU HAVE 0 LIVES. UNLUCKY! YOU LOSE.")
    sys.exit()
if lives_remaining > 0:
    question_nine()
else:
    print("YOU HAVE 0 LIVES. UNLUCKY! YOU LOSE.")
    sys.exit()
if lives_remaining > 0:
    question_ten()
else:
    print("YOU HAVE 0 LIVES. UNLUCKY! YOU LOSE.")
    sys.exit()
###text to print if the player wins the quiz
if lives_remaining > 0:
    print("Congratulations! You made it to the end of the quiz! You win!")
    print("You successfully defeated the Crazy Mad Quiz, World Cup 2018 edition!")
else:
    print("Unlucky, you lost all of your lives....")
    print("You failed to defeat the Crazy Mad Quiz, World Cup 2018 edition.")
