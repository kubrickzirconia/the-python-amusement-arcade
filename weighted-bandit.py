symbols = ["DOLLAR SIGN", "DOLLAR SIGN", "BANANA", "BANANA", "CHERRY", "CHERRY", "DIAMOND", "SEVEN", "SEVEN", "BAR", "BAR"]
import random
reel_1 = random.choice(symbols)
reel_2 = random.choice(symbols)
reel_3 = random.choice(symbols)
if reel_1 == reel_2 and reel_2 == reel_3:
    if reel_1 == "DIAMOND":
      print("%s! %s! %s! WOW, VERY RARE! JACKPOT! YOU WIN $$$$$$"% (reel_1, reel_2, reel_3))
    else:
      print("%s! %s! %s! LUCKY STRIKE! YOU WIN £10"% (reel_1, reel_2, reel_3))
elif reel_1 == reel_2 or reel_1 == reel_3 or reel_2 == reel_3:
    print("%s! %s! %s! NOT BAD, YOU WON £5" % (reel_1, reel_2, reel_3))
else:
    print("%s! %s! %s! YOU LOSE..." % (reel_1, reel_2, reel_3))
