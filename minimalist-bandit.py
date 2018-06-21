Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
symbols = ["DOLLAR SIGN", "BANANA", "CHERRY", "DIAMOND", "SEVEN", "BAR"]
import random
reel_1 = random.choice(symbols)
reel_2 = random.choice(symbols)
reel_3 = random.choice(symbols)
if reel_1 == reel_2 and reel_2 == reel_3:
    print("%s! %s! %s! LUCKY STRIKE! YOU WIN £10"% (reel_1, reel_2, reel_3))
elif reel_1 == reel_2 or reel_1 == reel_3 or reel_2 == reel_3:
    print("%s! %s! %s! NOT BAD, YOU WON £5" % (reel_1, reel_2, reel_3))
else:
    print("%s! %s! %s! YOU LOSE..." % (reel_1, reel_2, reel_3))
