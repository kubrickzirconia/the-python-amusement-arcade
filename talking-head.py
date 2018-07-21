###list of fortunes
fortunes = ["Chances are you'll be dead by next summer. Follow these words if you want to make it out alive.", "I see the dollar signs in your eyes. Will it pay off?", "Your good vibes will get you far, but how far and how long for?"]
rhetorical_questions = ["you'll get all you ever wanted.", "the future is bright.", "you'll find your soulmate.", "England will win the World Cup"]
eight_ball = ["most likely", "outlook good", "reply hazy", "better not tell you now", "very doubtful", "don't count on it"]
lucky_objects = ["cat", "convertible", "lady bird", "feather", "golden tooth", "teddy bear"]
lucky_colour = ["red", "blue", "yellow", "purple", "green", "black", "white", "orange", "pink"]
###introductory text to print
print("Greetings companion, my name is Talking Head.")
print("I am the Python Amusment Arcade's automated fortune telling machine.")
print("I sense you are troubled. Let me guess...")
###selecting a fortune
import random
fortune_one = random.choice(fortunes)
fortune_two = random.choice(rhetorical_questions)
fortune_three = random.choice(eight_ball)
fortune_four = random.choice(lucky_objects)
fortune_five = random.choice(lucky_colour)
###printing the result
print("All you need to know is this: %s" % (fortune_one))
print("You're desperate to know if %s." % (fortune_two))
print("Well... %s !!!" % (fortune_three))
print("Look out for a %s... it holds the key to everything." % (fortune_four))
print("Your lucky colour is %s!" % (fortune_five))
print("Thank you for listening. Cross my palm with cold hard cash to hear more.")
