### introducing the game's premise to the player
### randomly generating the number of bullets the player gets
from random import randint
import sys
bullet_bag = randint(30, 45)
answer_1 = ""
answer_2 = ""
answer_3 = ""
answer_4 = ""
answer_5 = ""
answer_6 = ""
answer_7 = ""
answer_8 = ""
answer_9 = ""
answer_10 = ""
tube_q = ""
north_south = ""
bullets_lost = 0
bullets_found = 0
taxi_luck = 0
negotiations = 0
print("Welcome to the Zombie Bullet Arcade.")
print("Test your survival instinct as you try to outrun the living dead.")
print("Each choice you make will cost you bullets, so choose wisely.")
print("This is hell on earth. You have %s bullets." % (bullet_bag))
### scenario 1
def scenario_1():
    global bullet_bag
    global answer_1
    print("...")
    print("...")
    print("...")
    print("We InTeRuPt ThIs PrOgRaMmE wItH uRgEnT nEwS.")
    print("ThE dEaD wAlK tHe EaRtH. aLl BeTs ArE oFf. GoOd LuCk.")
    print("The television cuts off. You hear groaning and shrieks.")
    print("You peer out of the window. Corpses stagger across the street.")
    answer_1 = input("What do you do? (leave/stay)")
    while answer_1 not in ("leave", "stay"):
        print("ERROR! INVALID ANSWER. TRY AGAIN. (leave/stay)")
        answer_1 = input("What do you do? (leave/stay)?")
    if answer_1 == "leave":
        print("Run!")
        print("A few bullets later, you're on your feet running away from the havoc.")
        bullet_bag = bullet_bag - randint(1, 5)
    else:
        print("You grab a few cans of beer and scramble into your bedroom.")
        print("You settle down to relax, when you hear BRAAAAINNNNS!")
        print("The zombies are outside your door. They can smell you.")
    return answer_1
    return bullet_bag
### scenario 2: stay
def scenario_2():
    global bullet_bag
    global answer_2
    print("You have %s bullets left. Use them wisely." % (bullet_bag))
    print("The living dead are knocking at your door.")
    print("Their groans sound more and more determined.")
    print("One punches through the window.")
    print("It won't be long until they break in...")
    answer_2 = input("What do you do? (leave/stay)")
    while answer_2 not in ("leave", "stay"):
        print("ERROR! INVALID ANSWER. TRY AGAIN. (leave/stay)")
        answer_2 = input("What do you do? (leave/stay)?")
    if answer_2 == "leave":
        print("Run!")
        print("A few bullets later, you're on your feet running away from the havoc.")
        bullet_bag = bullet_bag - randint(10, 13)
    else:
        print("You're trapped!")
        print("Surrounded!")
        print("You won't make the jump to the pavement.")
        print("You put the gun to your head.")
        print("Your finger trembles on the trigger.")
        print("You blow your own brains out.")
        print("Better dead than zombie food.")
        print("UNLUCKY, YOU LOSE.")
        sys.exit()
    return answer_2
    return bullet_bag
### scenario 3: leave
def scenario_3():
    global bullet_bag
    global answer_3
    global tube_q
    global taxi_luck
    print("You have %s bullets left. Use them wisely." % (bullet_bag))
    print("London's a great city...")
    print("But not at the end of the world.")
    print("You need to get out of here, fast!")
    print("You're running and running until you can barely breathe.")
    print("When you stop to catch your breath you don't recognise where you are...")
    print("There don't seem to be any zombies here. But there is a tube station.")
    answer_3 = input("Getting out of London is priority number 1. Do you get a taxi or take the tube? (taxi/tube)")
    while answer_3 not in ("taxi", "tube"):
        print("ERROR! INVALID ANSWER. TRY AGAIN. (taxi/tube)")
        answer_3 = input("Do you get a taxi or take the tube? (taxi/tube)?")
    if answer_3 == "tube":
            print("You're so stressed. All the tunnels are confusing right now.")
            print("You just need to get on a train.")
            tube_q = input("Which line do you get? (circle/district)")
            while tube_q not in ("circle", "district"):
                print("ERROR! INVALID ANSWER. TRY AGAIN. (taxi/tube)")
                tube_q = input("Which line do you get? (circle/district)")
            if tube_q == "circle":
                print("You hop on the first carriage that pulls up.")
                print("It's pretty empty, so you sit opposite a family, huddled together")
                print("You remain alert, twitching with agitation.")
                print("As you approach your stop, you notice that the family look sick.")
                print("Their skin is turning green...")
                print("You can't look them in the eye, but you have to kill them.")
                print("Its the kindest thing to do.")
                print("A few shots and its done.")
                print("You exit the station pensive but alive.")
                bullet_bag = bullet_bag - randint(5, 8)
            else:
                print("You hop on a carriage...")
                print("A carriage full of zombies.")
                print("You just have to hold them off until the next stop.")
                print("And you're on the run again...")
                bullet_bag = bullet_bag - randint(8, 12)
    else:
        taxi_luck = randint(1, 4)
        if taxi_luck == 3:
            print("You hop in the nearest taxi.")
            print("As you catch your breath, the driver turns around...")
            print("BRAAAAINNNNS")
            print("A zombie! You try to open the door...")
            print("...but it's locked!")
            print("You reach for your gun...")
            print("...but you weren't quick enough!")
            print("UNLUCKY, YOU LOSE.")
            sys.exit()
        else:
            print("You hop in the nearest taxi.")
            print("As you catch your breath, the driver turns around...")
            print("**Alright mate? Where would you like to go?**")
            print("Get me out of here.")
    return bullet_bag
    return taxi_luck
    return answer_3
    return tube_q
### scenario 4
def scenario_4():
    global bullet_bag
    global answer_4
    global bullets_found
    global bullets_lost
    print("You have %s bullets left. Use them wisely." % (bullet_bag))
    print("You're on the outskirts of the city.")
    print("Looks like you got out just in time.")
    print("In the distance you see flames and panic.")
    print("You're not sure what to do next.")
    print("Maybe you need some supplies?")
    print("You spot a supermarket across the road.")
    answer_4 = input("Do you search the supermarket for supplies? (yes/no)")
    while answer_4 not in ("yes", "no"):
        print("ERROR! INVALID ANSWER. TRY AGAIN. (yes/no)")
        answer_4 = input("Do you search the supermarket for supplies? (yes/no)")
    if answer_4 == "yes":
        print("You enter...")
        print("It's pitch black and empty, but you keep going.")
        print("Looks like someone's already sorted through a lot of the stock.")
        bullets_found = randint(10, 25)
        bullet_bag = bullet_bag + bullets_found
        bullets_lost = randint(10, 20)
        bullet_bag = bullet_bag - bullets_lost
        print("Score! You found %s bullets!" % (bullets_found))
        print("As you exit the shop you're acosted by the living dead.")
        print("Unlucky! that cost you %s bullets!" % (bullets_lost))
    else:
        print("You choose not to check out the supermarket.")
        print("Hopefully you won't run out of bullets...")
    return answer_4
    return bullet_bag
    return bullets_found
    return bullets_lost
### scenario 5
def scenario_5():
    global bullet_bag
    global answer_5
    global north_south
    print("You have %s bullets left. Use them wisely." % (bullet_bag))
    print("You've got to move quickly...")
    print("It's your lucky day!")
    print("On the left side of the road, there's a shiny Maserati.")
    print("One the right side of the road, there's a beat up, greasy motorbike.")
    answer_5 = input("Which vehicle do you take? (car/bike)")
    while answer_5 not in ("car", "bike"):
        print("ERROR! INVALID ANSWER. TRY AGAIN. (car/bike)")
        answer_5 = input("Which vehicle do you take? (car/bike)")
    print("Now you need to decide where you're going!")
    print("A real crossroad.")
    print("Do you head north, for the hills, or South, to the beach?")
    north_south = input("Do you go North or South (north/south)")
    while north_south not in ("north", "south"):
        print("ERROR! INVALID ANSWER. TRY AGAIN. (north/south)")
        north_south = input("Do you go North or South (north/south)")
    return north_south
    return answer_5
    return bullet_bag
### scenario 6: car
def scenario_6():
    global answer_6
    global bullet_bag
    print("You have %s bullets left. Use them wisely." % (bullet_bag))
    print("You hop in the car and feel the expensive leather interior welcome you.")
    print("Perhaps the zombie apocalypse isn't so bad.")
    print("You could get used to luxury!")
    print("You pull out and drive along the open road...")
    print("vrrrroooooommm")
    print("Hold on...")
    print("You're low on petrol!")
    print("You pull into the next service station to get more fuel.")
    print("As you're filling your new sports car with petrol, you see somebody.")
    print("There's a shop assistant behind the desk.")
    print("Why is he still doing his job?")
    print("Has he not noticed that it's the end of the world?")
    print("Maybe the chaos hasn't reached here yet...")
    print("He spots you and beckons you to pay.")
    print("So you enter the station to pay for your petrol...")
    if north_south == "north":
        print("Stood behind the counter is a lean man, wearing a set of overalls.")
        print("His large eyes stare into yours and he smiles.")
        print("His crooked teeth are yellowed and chipped, but he seems friendly.")
        print("You notice his hair is matted and his nails are dirty.")
        print("**Hello There!**")
        print("He chuckles!")
        print("**Would you like to play a game?**")
        print("You really should get going...")
        print("...but you get the impression that you don't have the option to decline his game.")
        print("So you ask him what the game is.")
        print("**Why, heads or tails! What else could it be?**")
        print("He picks up a shiny gold coin and twirls it in his fingers.")
        answer_6 = input("Do you pick heads or tails? (heads/tails)")
        while answer_6 not in ("heads", "tails"):
            print("ERROR! INVALID ANSWER. TRY AGAIN. (heads/tails)")
            answer_6 = input("Do you pick heads or tails? (heads/tails)")
        if answer_6 == "heads":
            print("The shop assistant smirks...")
            print("He reaches into the cash register...")
            print("...")
            print("**Looks like it's your lucky day.**")
            print("You hold out your hand.")
            print("He places a bullet in your palm.")
            print("**Have a nice day!**")
            print("The assistant waves as you leave the station.")
            bullet_bag = bullet_bag + 1
        else:
            print("The shop assistant smirks...")
            print("He reaches into the cash register...")
            print("...")
            print("**goodbye.**")
            print("...")
            print("He shot you clean through the skull!")
            print("Maybe he thought you were one of the undead...")
            print("Or maybe he just wanted your car!")
            print("UNLUCKY, YOU LOSE.")
            sys.exit()
    else:
        print("Stood behind the counter is a stocky young man, wearing a Nike tracksuit.")
        print("He must be about 19 years old.")
        print("He's got spiked black hair and a prominent brow line.")
        print("You ask him if it's just him running the shop.")
        print("**My Dad left me in charge of the shop. He left about twenty minutes ago**")
        print("He seems suspicious of you. His hands are in his pockets and he's scowling.")
        print("**Would you like to play a game?**")
        print("Wanting to get back on his good side, you say yes!")
        print("*Okay, do you want heads or tails?")
        print("He fumbles around in his pocket looking for a coin.")
        print("He finds one and places it decisively on the counter.")
        answer_6 = input("Do you pick heads or tails? (heads/tails)")
        while answer_6 not in ("heads", "tails"):
            print("ERROR! INVALID ANSWER. TRY AGAIN. (heads/tails)")
            answer_6 = input("Do you pick heads or tails? (heads/tails)")
        if answer_6 == "tails":
            print("The shop assistant smirks...")
            print("He reaches into the cash register...")
            print("...")
            print("**Looks like it's your lucky day.**")
            print("You hold out your hand.")
            print("He places a bullet in your palm.")
            print("**Have a nice day!**")
            print("The assistant waves as you leave the station.")
            bullet_bag = bullet_bag + 1
        else:
            print("The shop assistant smirks...")
            print("He reaches into the cash register...")
            print("...")
            print("**goodbye.**")
            print("...")
            print("He shot you clean through the skull!")
            print("Maybe he thought you were one of the undead...")
            print("Or maybe he just wanted your car!")
            print("UNLUCKY, YOU LOSE.")
            sys.exit()
    return answer_6
    return bullet_bag
### scenario 7: travelling north biking
def scenario_7():
    global bullet_bag
    global answer_7
    print("You have %s bullets left. Use them wisely." % (bullet_bag))
    print("It feels like you've been driving for days.")
    print("Are you even still in England?")
    print("In the near distance you see mountains.")
    print("Hang on a minute! You're in Scotland!!")
    print("Wonder where's best to go now?")
    print("I bet if you could get to those mountains you'd feel safe.")
    print("But which road do you take?")
    answer_7 = input("Do you go left or right? (left/right)")
    while answer_7 not in ("left", "right"):
        print("ERROR! INVALID ANSWER. TRY AGAIN. (left/right)")
        answer_7 = input("Do you go left or right? (left/right)")
    if answer_7 == "left":
        print("Ah! loads of zombies!")
        if answer_5 == "car":
            print("Luckily, you're pretty well protected in your car!")
        else:
            print("The motorbike offers you little protection so you'll have to shoot them down as you go...")
            print("Keep riding, keep shooting!")
            bullet_bag = bullet_bag - randint(8, 15)
    else:
        print("Luckily there are only a couple of zombies over here...")
        if answer_5 == "car":
            print("You're pretty well protected in your car anyway!")
        else:
            print("The motorbike offers you little protection so you'll have to shoot them down as you go...")
            print("Keep riding, keep shooting!")
            bullet_bag = bullet_bag - randint(4, 7)
    if bullet_bag > 0:
        print("You made it!")
        print("You stand on the mountains staring down at the chaos")
        print("Maybe you could live a life in the mountains...")
    else:
        print("You tried to make it through...")
        print("But you ran out of bullets...")
        print("So the zombies got to you before you reached the mountains.")
        print("UNLUCKY, YOU LOSE.")
        sys.exit()
    return bullet_bag
### scenario 8: travelling south cow
def scenario_8():
    global bullet_bag
    global answer_8
    print("You have %s bullets left. Use them wisely." % (bullet_bag))
    print("You're cruising down the south coast.")
    print("And everything's going pretty smoothly...")
    print("What's that blocking the road ahead?")
    print("COWS!")
    print("There are some cows grazing right in the middle of this winding country road!")
    print("You try to get them to move...")
    print("But they won't budge.")
    print("There don't seem to be any other options...")
    answer_8 = input("Do you shoot the cows? (shoot/no)")
    while answer_8 not in ("shoot", "no"):
        print("ERROR! INVALID ANSWER. TRY AGAIN. (shoot/no)")
        answer_8 = input("Do you shoot the cows? (shoot/no)")
    if answer_8 == "shoot":
        print("You start shooting the cows!")
        bullet_bag = bullet_bag - randint(5, 8)
        print("**HEY, WHAT DO YOU THINK YOU'RE DOING!**")
        print("A disgruntled farmer with a shotgun is staring you down.")
        print("He looks erratic...")
        print("You have no choice but to take him out to...")
        if bullet_bag > 1:
            print("You turn your gun to the farmer...")
            print("You pull the trigger...")
            print("Another death on your hands.")
            print("You drive off, wondering if it's all worth it!")
            bullet_bag = bullet_bag - 1
        else:
            print("You turn your gun to the farmer...")
            print("You pull the trigger...")
            print("But you're out of bullets!")
            print("He smirks and cocks his gun.")
            print("He shot you! Perhaps you deserved it for ruining his livelihood...")
            print("YOU LOSE.")
            sys.exit()
    else:
        print("You really need to get going!")
        print("Are you sure you don't want to shoot them?")
        answer_8 = input("Do you shoot the cows? (shoot/no)")
        while answer_8 not in ("shoot", "no"):
            print("ERROR! INVALID ANSWER. TRY AGAIN. (shoot/no)")
            answer_8 = input("Do you shoot the cows? (shoot/no)")
        if answer_8 == "shoot":
            print("You start shooting the cows!")
            bullet_bag = bullet_bag - randint(5, 8)
            print("**HEY, WHAT DO YOU THINK YOU'RE DOING!**")
            print("A disgruntled farmer with a shotgun is staring you down.")
            print("He looks erratic...")
            print("You have no choice but to take him out to...")
            if bullet_bag > 1:
                print("You turn your gun to the farmer...")
                print("You pull the trigger...")
                print("Another death on your hands.")
                print("You drive off, wondering if it's all worth it!")
                bullet_bag = bullet_bag - 1
            else:
                print("You turn your gun to the farmer...")
                print("You pull the trigger...")
                print("But you're out of bullets!")
                print("He smirks and cocks his gun.")
                print("He shot you! Perhaps you deserved it for ruining his livelihood...")
                print("YOU LOSE.")
                sys.exit()
        else:
            if bullet_bag > 3:
                print("You fire three warning shots into the sky.")
                print("The cows scarper!")
                print("The cows were scared away... Now you have a clear path to continue your journey...")
                bullet_bag = bullet_bag - 3
            else:
                print("You're wasting precious time!")
                print("You try firing a warning shot...")
                print("But you don't have enough bullets to scare them away!")
                print("In the time you've wasted the corpses are staggering closer...")
                print("You're surrounded by death. The zombies are stumbling closer.")
                print("A member of the living dead is looming over you.")
                print("You aim your gun at him. You pull the trigger, but nothing happens...")
                print("You check the barrel... you're out of bullets!")
                print("His teeth sink deep into your skin. ")
                print("As you feel death encroach, you look into your attacker's cold blank eyes...")
                print("UNLUCKY, YOU LOSE.")
                sys.exit()
    return bullet_bag
    return answer_8
### scenario 9
def scenario_9():
    global bullet_bag
    global answer_9
    print("You have %s bullets left. Use them wisely." % (bullet_bag))
    print("**ATTENTION ALL**")
    print("**WE HAVE SUPPLIES AND A BOAT**")
    print("**WE ARE TRANSPORTING ALL CIVILIANS TO SAFETY**")
    print("**THIS IS THE SCOTTISH GOVERNMENT**")
    print("**PLEASE PROCEED TO THE COAST**")
    print("The megaphone they're using must be pretty powerful...")
    print("Because you can hear it from up in the mountains!")
    print("It sounds legit - this could be a chance of safety!")
    print("Standing between you and sanctuary is 3 miles of rocky road...")
    print("So you start running!")
    print("")
    answer_9 = input("Do you shoot the sheep? (shoot/no)")
    while answer_9 not in ("shoot", "no"):
        print("ERROR! INVALID ANSWER. TRY AGAIN. (shoot/no)")
        answer_9 = input("Do you shoot the sheep? (shoot/no)")
    if answer_9 == "shoot":
        print("You start shooting...")
        print("And the nearby wildlife get startled...")
        print("The noise has attracted the attention of several zombies")
        print("Hopefully you have enough bullets to make it to the ship...")
        bullet_bag = bullet_bag - randint(5, 15)
    else:
        print("You really need to get out of the mountains!")
        print("Are you sure you don't want to shoot them?")
        answer_9 = input("Do you shoot the sheep? (shoot/no)")
        while answer_9 not in ("shoot", "no"):
            print("ERROR! INVALID ANSWER. TRY AGAIN. (shoot/no)")
            answer_9 = input("Do you shoot the sheep? (shoot/no)")
        if answer_9 == "shoot":
            print("You start shooting...")
            print("And the nearby wildlife get startled...")
            print("The noise has attracted the attention of several zombies")
            print("Hopefully you have enough bullets to make it to the ship...")
            bullet_bag = bullet_bag - randint(5, 15)

        else:
            if bullet_bag > 3:
                print("You fire three warning shots into the sky.")
                print("The sheep scarper!")
                print("The sheep were scared away... Now you have a clear path to run to the ship!")
                bullet_bag = bullet_bag - 3
            else:
                print("You're wasting precious time!")
                print("You try firing a warning shot...")
                print("But you don't have enough bullets to scare them away!")
                print("In the time you've wasted the corpses are staggering closer...")
                print("You're surrounded by death. The zombies are stumbling closer.")
                print("A member of the living dead is looming over you.")
                print("You aim your gun at him. You pull the trigger, but nothing happens...")
                print("You check the barrel... you're out of bullets!")
                print("His teeth sink deep into your skin. ")
                print("As you feel death encroach, you look into your attacker's cold blank eyes...")
                print("UNLUCKY, YOU LOSE.")
                sys.exit()
    return bullet_bag
    return answer_9
### scenario 10
def scenario_10():
    global bullet_bag
    global answer_10
    global answer_5
    global negotiations
    print("You have %s bullets left. Use them wisely." % (bullet_bag))
    print("You made it to the coast!")
    print("And your future suddenly looks bright...")
    print("There's a ship docked.")
    print("You see several people running around.")
    print("They look like they're organising something...")
    print("Maybe they're looking to set sail! Maybe you could join them!")
    print("But standing between you and the ocean is a large, steep cliff face.")
    print("It looks precarious.")
    print("But you have no choice. You can hear the zombies hot on your tail.")
    print("You need to get down from the cliffs.")
    if answer_5 == "car":
        print("You think fast.")
        print("You're searching the car for anything that might help you scale the cliffs.")
        print("You unlock the boot.")
        print("Lucky you... you found a rope!")
        print("You safely scale the cliff.")
        print("You're relieved when your feet touch the floor.")
        print("You're running across the beach towards the ship.")
    else:
        print("You're all out of options.")
        print("You brace yourself... Rev your motor")
        print("You drive off the cliff face, hoping to pull a Tony Hawk style stunt.")
        print("The landing is pretty rough. The motorbike is destroyed and you're pretty beat up")
        print("You're covered in blood. There's a huge gash down the side of your leg.")
        print("....")
        print("...")
        print("It seems like something can smell your blood...")
        print("A small horde of zombies approach!")
        print("Start shooting! You've got to hold them off as you stagger towards the ship.")
        bullet_bag = bullet_bag - randint(8, 10)
    if bullet_bag > 0:
        print("You have %s bullets left. Use them wisely." % (bullet_bag))
        print("You're running up to the ship...")
        print("**OI! HANDS UP!**")
        print("The captain is pointing a gun to your head.")
        print("Maybe he thinks you could be a zombie.")
        print("Maybe he wants to kill you and take your supplies...")
        print("You're pretty experienced with your gun by now.")
        print("You're confident that you can pull it out and shoot him before he shoots you...")
        print("But maybe he just wants to talk.")
        answer_10 = input("Do you negotiate or start shooting? (negotiate/shoot)")
        while answer_10 not in ("negotiate", "shoot"):
            print("ERROR! INVALID ANSWER. TRY AGAIN. (negotiate/shoot)")
            answer_10 = input("Do you negotiate or start shooting? (negotiate/shoot)")
        if answer_10 == "shoot":
            print("You start shooting.")
            print("He's got a pretty big crew.")
            print("Hopefully you have enough bullets to shoot them all...")
            print("Otherwise, the survivors are bound to leave you for dead!")
            bullet_bag = bullet_bag - randint(10, 20)
        else:
            negotiations = randint(1, 2)
            if negotiations == 2:
                print("Negotiations are tricky at the best of times...")
                print("But this is the end of the world!")
                print("And the captain wasn't in the mood to chat.")
                print("So you got a bullet in the back of the head.")
                print("You were so close!")
                print("YOU LOSE.")
                sys.exit()
            else:
                print("Seems like the captain kind of likes you.")
                print("Negotiations went well.")
                print("You're all aboard! And he's letting you ride top of deck.")
    else:
        print("You're surrounded by death. The zombies are stumbling closer.")
        print("A member of the living dead is looming over you.")
        print("You aim your gun at him. You pull the trigger, but nothing happens...")
        print("You check the barrel... you're out of bullets!")
        print("His teeth sink deep into your skin. ")
        print("As you feel death encroach, you look into your attacker's cold blank eyes...")
        print("UNLUCKY, YOU LOSE.")
        sys.exit()
    return bullet_bag
    return answer_5
    return answer_10
### EXECUTING CODE
scenario_1()
if bullet_bag > 0 and answer_1 == "leave":
    scenario_3()
elif bullet_bag > 0 and answer_1 == "stay":
    scenario_2()
    if bullet_bag > 0:
        scenario_3()
    else:
        print("You're surrounded by death. The zombies are stumbling closer.")
        print("A member of the living dead is looming over you.")
        print("You aim your gun at him. You pull the trigger, but nothing happens...")
        print("You check the barrel... you're out of bullets!")
        print("His teeth sink deep into your skin. ")
        print("As you feel death encroach, you look into your attacker's cold blank eyes...")
        print("UNLUCKY, YOU LOSE.")
        sys.exit()
else:
    print("You're surrounded by death. The zombies are stumbling closer.")
    print("A member of the living dead is looming over you.")
    print("You aim your gun at him. You pull the trigger, but nothing happens...")
    print("You check the barrel... you're out of bullets!")
    print("His teeth sink deep into your skin. ")
    print("As you feel death encroach, you look into your attacker's cold blank eyes...")
    print("UNLUCKY, YOU LOSE.")
    sys.exit()
if bullet_bag > 0:
    scenario_4()
else:
    print("You're surrounded by death. The zombies are stumbling closer.")
    print("A member of the living dead is looming over you.")
    print("You aim your gun at him. You pull the trigger, but nothing happens...")
    print("You check the barrel... you're out of bullets!")
    print("His teeth sink deep into your skin. ")
    print("As you feel death encroach, you look into your attacker's cold blank eyes...")
    print("UNLUCKY, YOU LOSE.")
    sys.exit()
if bullet_bag > 0:
    scenario_5()
else:
    print("You're surrounded by death. The zombies are stumbling closer.")
    print("A member of the living dead is looming over you.")
    print("You aim your gun at him. You pull the trigger, but nothing happens...")
    print("You check the barrel... you're out of bullets!")
    print("His teeth sink deep into your skin. ")
    print("As you feel death encroach, you look into your attacker's cold blank eyes...")
    print("UNLUCKY, YOU LOSE.")
    sys.exit()
if bullet_bag > 0 and answer_5 == "car":
    scenario_6()
    if bullet_bag > 0 and north_south == "north":
        scenario_7()
    elif bullet_bag >0 and north_south == "south":
        scenario_8()
    else:
        print("You're surrounded by death. The zombies are stumbling closer.")
        print("A member of the living dead is looming over you.")
        print("You aim your gun at him. You pull the trigger, but nothing happens...")
        print("You check the barrel... you're out of bullets!")
        print("His teeth sink deep into your skin. ")
        print("As you feel death encroach, you look into your attacker's cold blank eyes...")
        print("UNLUCKY, YOU LOSE.")
        sys.exit()
elif bullet_bag > 0 and north_south == "north":
    scenario_7()
elif bullet_bag > 0 and north_south == "south":
    scenario_8()
else:
    print("You're surrounded by death. The zombies are stumbling closer.")
    print("A member of the living dead is looming over you.")
    print("You aim your gun at him. You pull the trigger, but nothing happens...")
    print("You check the barrel... you're out of bullets!")
    print("His teeth sink deep into your skin. ")
    print("As you feel death encroach, you look into your attacker's cold blank eyes...")
    print("UNLUCKY, YOU LOSE.")
    sys.exit()
if bullet_bag > 0 and north_south == "north":
    scenario_9()
elif bullet_bag > 0 and north_south == "south":
    scenario_10()
else:
    print("You're surrounded by death. The zombies are stumbling closer.")
    print("A member of the living dead is looming over you.")
    print("You aim your gun at him. You pull the trigger, but nothing happens...")
    print("You check the barrel... you're out of bullets!")
    print("His teeth sink deep into your skin. ")
    print("As you feel death encroach, you look into your attacker's cold blank eyes...")
    print("UNLUCKY, YOU LOSE.")
    sys.exit()
### winning the game
if bullet_bag > 0 and north_south == "north":
    print("You're soaking wet and freezing cold.")
    print("You are exhausted and injured.")
    print("You're on a boat.")
    print("You're on a boat!")
    print("The sea air fills your lungs.")
    print("For the first time today you feel safe.")
    print("You savour the moment, gazing out across the blue seas.")
    print("In the distance you see Scandanavia.")
    print("You might have actually escaped the mess back home.")
    print("No more zombies staggering around London, falling into the Thames.")
    print("No, you're far away from that now.")
    print("Congratulations! You survived...")
    print("Until the sequel!")
elif bullet_bag > 0 and north_south == "south":
    print("You're soaking wet and freezing cold.")
    print("You are exhausted and injured.")
    print("You're on a boat.")
    print("You're on a boat!")
    print("The sea air fills your lungs.")
    print("For the first time today you feel safe.")
    print("You savour the moment, gazing out across the blue seas.")
    print("In the distance you see Calais.")
    print("You might have actually escaped the mess back home.")
    print("No more zombies staggering around London, falling into the Thames.")
    print("No, you're far away from that now.")
    print("Congratulations! You survived...")
    print("Until the sequel!")
else:
    print("You're surrounded by death. The zombies are stumbling closer.")
    print("A member of the living dead is looming over you.")
    print("You aim your gun at him. You pull the trigger, but nothing happens...")
    print("You check the barrel... you're out of bullets!")
    print("His teeth sink deep into your skin. ")
    print("As you feel death encroach, you look into your attacker's cold blank eyes...")
    print("You were so close. You can see the ocean stretch out across the horizon.")
    print("UNLUCKY, YOU LOSE.")
