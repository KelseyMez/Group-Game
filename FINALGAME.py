import random
import sys
import time

def typingprint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  
def typinginput(text):
  for character in text:

    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  value = input()  
  return value

print("""
 _____                                                                            _____ 
( ___ )                                                                          ( ___ )
 |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | 
 |   |                                                                            |   | 
 |   |   █████████                         ███                                    |   | 
 |   |  ███░░░░░███                       ░░░                                     |   | 
 |   | ░███    ░░░   ██████   █████ █████ ████  ████████    ███████               |   | 
 |   | ░░█████████  ░░░░░███ ░░███ ░░███ ░░███ ░░███░░███  ███░░███               |   | 
 |   |  ░░░░░░░░███  ███████  ░███  ░███  ░███  ░███ ░███ ░███ ░███               |   | 
 |   |  ███    ░███ ███░░███  ░░███ ███   ░███  ░███ ░███ ░███ ░███               |   | 
 |   | ░░█████████ ░░████████  ░░█████    █████ ████ █████░░███████               |   | 
 |   |  ░░░░░░░░░   ░░░░░░░░    ░░░░░    ░░░░░ ░░░░ ░░░░░  ░░░░░███               |   | 
 |   |                                                     ███ ░███               |   | 
 |   |                                                    ░░██████                |   | 
 |   |                                                     ░░░░░░                 |   | 
 |   |  ██████████ ████     ██████  █████                ███                  ███ |   | 
 |   | ░░███░░░░░█░░███    ███░░███░░███                ░░░                  ░███ |   | 
 |   |  ░███  █ ░  ░███   ░███ ░░░  ░███████    ██████  ████  █████████████  ░███ |   | 
 |   |  ░██████    ░███  ███████    ░███░░███  ███░░███░░███ ░░███░░███░░███ ░███ |   | 
 |   |  ░███░░█    ░███ ░░░███░     ░███ ░███ ░███████  ░███  ░███ ░███ ░███ ░███ |   | 
 |   |  ░███ ░   █ ░███   ░███      ░███ ░███ ░███░░░   ░███  ░███ ░███ ░███ ░░░  |   | 
 |   |  ██████████ █████  █████     ████ █████░░██████  █████ █████░███ █████ ███ |   | 
 |   | ░░░░░░░░░░ ░░░░░  ░░░░░     ░░░░ ░░░░░  ░░░░░░  ░░░░░ ░░░░░ ░░░ ░░░░░ ░░░  |   | 
 |   |                                                                            |   | 
 |   |                                                                            |   | 
 |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| 
(_____)                                                                          (_____)""")

print()
print()

typingprint ("""
The story begins with you, a normal person walking home from work, suddenly you are surrounded
by bright lights. You wake up and don't know where you are, confused and wondering how you got there.""")
time.sleep(1)

print()

typingprint ("""
When you look around you notice you are in a throne room and a man with a long robe and a crown
stands and introduces himself...""")
print("""
                             .
                            / \ 
                           _\ /_
                 .     .  (,'v`.)  .     .
                 \)   ( )  ,' `.  ( )   (/
                  \`. / `-'     `-' \ ,'/
                   : '    _______    ' :
                   |  _,-'  ,-.  `-._  |
                   |,' ( )__`-'__( ) `.|
                   (|,-,'-._   _.-`.-.|)
                   /  /<( o)> <( o)>\  \ 
                   :  :     | |     :  :
                   |  |     ; :     |  |
                   |  |    (.-.)    |  |
                   |  |  ,' ___ `.  |  |
                   ;  |)/ ,'---'. \(|  :
               _,-/   |/\(       )/\|   \-._
         _..--'.-(    |   `-'''-'   |    )-.`--.._
                  `.  ;`._________,':  ,'
                 ,' `/               \'`.
                      `------.------'        """) 
typingprint("""Hello brave hero from another world, my name is King Charles Elfheim, you have been summoned to 
this world by me to save our kingdom form a grave threat, the Demon King Yuno” 
you look at him in disbelief and he asks you 
“What is your name brave Hero?”
""")
time.sleep(1)
print()
username = typinginput("Enter your name to proceed: ").capitalize()

print()

typingprint (f"""{username} it is a fitting name for a hero such as yourself""")

print()

def make_desc():
    desc1 = typinginput("Will you go on the mission and help King Charles? (yes/no) ").lower()
    print()
    if desc1 == "yes" or desc1 == "y":
        print()
        typingprint(f"Excellent, thank you {username} we are counting on you.")
        start_training()
    elif desc1 == "no" or desc1 == "n":
        typingprint("""
You decline and tell the king you want to return to your own world, one of the magicians in his 
court named Merlin, tells you the only way home is to defeat the demon king as he possess the magic
you need to return. He then tells you about all the suffering in the kingdom and how many lives it has ruined, 
the king then says “will you still not help” you have no choice but too.""")
        start_training()
    else:
        print()
        typingprint("Wrong input! Try again..."), make_desc()

def start_training():
    print()
    typinginput("Type anything to continue... ")
    print()
    typingprint("""
The king offers training from his most skilled knights to help you on your quest,  while training the knight 
Sir Lanclelot asks you what class of fighter you would like to be?

1.Sword Wielder
2.Archer
3.Assasssin
4.Martial Arts""")
    class_choosing()

userclass = "0"

def class_choosing():
    print()
    global userclass
    userclass = (typinginput("What classs would you like to be? (1/2/3/4)... "))
    if userclass == "1" :
        print()
        typingprint("You havce chosen to become a Sword Wielder. Good Luck Hero!!")
    elif userclass == "2" :
        print()
        typingprint("You havce chosen to become a Skilled Archer. Good Luck Hero!!")
    elif userclass == "3" :
        print()
        typingprint("You havce chosen to become a Sneaky Assassin. Good Luck Hero!!")
    elif userclass == "4" :
        print()
        typingprint("You havce chosen to become a Martial Artist. Good Luck Hero!!")
    else:
        print()
        typingprint("Wrong input, Try again... ")
        class_choosing()
        

make_desc()


hp = 15
str = 15
coins = 0
chance = 0

typingprint("""
After training for a month you are ready. Play a dice game to see your luck and either gain better stats or be unlucky""")

def dice_game():
    print()
    (typinginput("Type roll to start! "))
    roll = random.randint(1,6)
    global hp
    global str
    global coins
    if roll == 1 :
        typingprint ("""
+-------+
|       |
|   O   |
|       |
+-------+""")
        print()
        typingprint (f"You got unlucky and rolled a {roll}. ")
        hp -= 2
        str -= 2
        typingprint(f"Your new health is {hp} and your new strength is {str}")
    elif roll == 2 :
        typingprint ("""
+-------+
| O     |
|       |
|     O |
+-------+""")
        print()
        typingprint (f"You got unlucky and rolled a {roll}. ")
        hp -= 2
        str -= 2
        typingprint(f"Your new health is {hp} and your new strength is {str}")
    elif roll == 3 :
        typingprint ("""
+-------+
| O     |
|   O   |
|     O |
+-------+""")
        print()
        typingprint (f"You got lucky and rolled a {roll}. ")
        hp += 2
        str += 2
        coins += 5
        typingprint(f"Your new health is {hp} and your new strength is {str} and your new coin balance is {coins}")
    elif roll == 4 :
        typingprint ("""
+-------+
| O   O |
|       |
| O   O |
+-------+""")
        print()
        typingprint (f"You got lucky and rolled a {roll}. ")
        hp += 2
        str += 2
        coins += 5
        typingprint(f"Your new health is {hp} and your new strength is {str} and your new coin balance is {coins}")
    elif roll == 5 :
        typingprint ("""
+-------+
| O   O |
|   O   |
| O   O |
+-------+""")
        print()
        typingprint (f"You got very lucky and rolled a {roll}. ")
        hp += 4
        str += 4
        coins += 10
        typingprint(f"Your new health is {hp} and your new strength is {str} and your new coin balance is {coins}")
    elif roll == 3 :
        typingprint ("""
+-------+
| O   O |
| O   O |
| O   O |
+-------+""")
        print()
        typingprint (f"You got lucky and rolled a {roll}. ")
        hp += 6
        str += 6
        coins += 20
        typingprint(f"Your new health is {hp} and your new strength is {str} and your new coin balance is {coins}")
    else:
        dice_game()

dice_game()


def start_mission():
    global userclass
    typingprint("""
You begin your journey by walking away from the castle and into the woods. you don't know how long you have
been walking for but eventually you stumble across a run down building surrounded by the demon kings guards.
You realise this must be the correct place and prepare to fight.
 """)
    typinginput("Type attack to fight... ")
    if userclass == "1":
        typingprint("You charge in and use your fire as a wall so nobody can sneak up on you")
    elif userclass == "2":
        typingprint("You set up at a higher position, somewhere that gives you a full view of the area.")
    elif userclass == "3":
        typingprint("You wait until nightfall and use the shadows to your advantage.")
    elif userclass == "4":
        typingprint("You realise that they all have weapons of some sort. You're going to want to attack in secrecy and use your strength against them.")
    else:
        typingprint("No class was detected")

print()

typingprint("""
After training the King approachs you with a task. The task is to retreive an item from nearby and bring it back.""")

print()

def are_you_fighting():
    global chance
    global coins
    answer_k = typinginput("Will you accept the task? (yes,no) ").lower()
    if answer_k == "yes" or answer_k == "y":
        print()
        typingprint("Thank you for your help, time to head out.")
        start_mission()
    elif answer_k == "no" or answer_k == "n":
        print()
        typingprint("Well that is unfortunate.")
    else:
        print()
        typingprint("Wrong input, try again...")
        are_you_fighting()
        

    if answer_k == "yes" or answer_k == "y":
        typingprint("""
You beat the guards and obtain the item for the King. You make your way back to the castle and hand it over.
The King thanks you for your effort in retrieving it and gives you your reward""")
        chance += 1
        coins += 20
        print()
        typingprint(f"You now have {chance} extra lives and your new coin balance is {coins}")

are_you_fighting()

print()

typingprint("""
The King gives you an option.
you can proceed on your quest alone or you can bring 1 companion.
The choices are:
0. You go solo!
1. Is a Dwarf named Beatrice, she is a skilled tank and is equipped with a battle axe.
2. Is a Elf named Leon, he is a skilled hunter equipped with a longbow.
3. Is a Human named Asmareldia, she is a mage and is a equipped with a staff.""")
companionvalue = 0
print()
def comp_choosing():
    global companionvalue
    companion = typinginput("Which companion do you want(0,1,2,3)... ")
    if companion == "0":
            typingprint("You have chosen to go alone. Good luck on your travels.")
    elif companion == "1":
            companionvalue += 1
            print("""
    ,   A           
    / \, | ,       .--.
    |    =|= >    /.--.\ 
    \ /` | `      |====|
    `   |         |`::`|
        |     .-;`\..../`;-.
        /\\/  /  |...::...|  \ 
        |:'\ |   /'''::'''\   |
        \ /\;-,/\   ::   /\--;
        |\ <` >  >._::_.<,<__>
        | `""`  /   ^^   \|  |
        |       |        |\::/
        |       |        |/|||
        |       |___/\___| '''
        |        \_ || _/
        |        <_ >< _>
        |        |  ||  |
        |        |  ||  |
        |       _\.:||:./_
        |      /____/\____\ """)
            print()
            typingprint("You have chosen to travel with Beatrice the Tank. ")
    elif companion == "2":
            companionvalue += 1
            print("""
                                                                |
                                                            \.
                                                            /|.
                                                        /  `|.
                                                        /     |.
                                                    /       |.
                                                    /         `|.
                                                /            |.
                                                /              |.
                                            /                |.
        __                                 /                  `|.
        -\                              /                     |.
            \\                          /                       |.
            \\                      /                         |.
                \|                   /                           |\ 
                \#####\          /                             ||
            ==###########>     /                               ||
            \##==      \    /                                 ||
        ______ =       =|__/___                                ||
    ,--' ,----`-,__ ___/'  --,-`-==============================##==========>
    \               '        ##_______ ______   ______,--,____,=##,__
    `,    __==    ___,-,__,--'#'  ==='      `-'              | ##,-/
        `-,____,---'       \####\              |        ____,--\_##,/
            #_              |##   \  _____,---==,__,---'         ##
            #              ]===--==\                            ||
            #,             ]         \                          ||
            #_            |           \                        ||
            ##_       __/'             \                      ||
                ####='     |                \                    |/
                ###       |                  \                  |.
                ##       _'                    \                |.
                ###=======]                       \              |.
            ///        |                         \           ,|.
            //         |                           \         |.
                                                        \      ,|.
                                                        \    |.
                                                            \  |.
                                                            \|.
                                                            /.
                                                            |""")
            print()
            typingprint("You have chosen to travel with Leon the Hunter. ")
    elif companion == "3":
            companionvalue += 1
            print("""
              _,._      
  .||,       /_ _\\     
 \.`',/      |'L'| |    
 = ,. =      | -,| L    
  / || \    ,-'\"/,'`.   
    ||     ,'   `,,. `.  
    ,|____,' , ,;' \| |  
    (3|\    _/|/'   _| |  
    ||/,-''  | >-'' _,\\ 
    ||'      ==\ ,-'  ,' 
    ||       |  V \ ,|   
    ||       |    |` |   
    ||       |    |   \  
    ||       |    \    \ 
    ||       |     |    \ 
    ||       |      \_,-'
    ||       |___,,--")_\ 
    ||         |_|   ccc/
    ||        ccc/       
    ||                """)
            print()
            typingprint("You have chosen to travel with Asmarelida. ")
    else:
         typingprint("Wrong input, Try again..."), comp_choosing()

comp_choosing()
typingprint("You start walking towards the town of Secondale, when there you see a tavern")
print()
def start_tavern():
    global coins
    global hp
    global str
    tavern = typinginput(f"""
What would you like to do?
*you have {coins} coins in your purse*
Type (sleep, gamble or exit)... """)
    if tavern == "sleep" or tavern == "s":
        hp += 10
        typingprint(f"""You had a restful night. You gained 10 health.
You have {hp} health and {str} strength...""")
    elif tavern == "exit" or tavern == "e":
        typingprint("Now leaving the tavern...")
    elif tavern == "gamble" or tavern == "g":
        if coins <= 0:
            typingprint("You can't gamble, insufficient coin amount")
            coins = 0
            start_tavern()
        else:
            gamble_result = random.randint(-8,5)
            coins += gamble_result
            if coins <= 0:
                coins = 0
            print()
            typingprint(f"you got {gamble_result} coins. your new coin balance is {coins}.")
            start_tavern()
    else:
         typingprint("Wrong input, Try again...")
         start_tavern()
start_tavern()


def save_mission():
    global userclass
    if userclass == "1":
        typingprint("You are strong enough to defeat the magician and you saved the Princess!")
    elif userclass == "2":
        typingprint("You are strong enough to defeat the magician and you saved the Princess")
    elif userclass == "3":
        typingprint("You are strong enough to defeat the magician and you saved the Princess")
    elif userclass == "4":
        typingprint("You are strong enough to defeat the magician and you saved the Princess")

def elie_mission():
    global str
    global coins
    typingprint ("""
When you leave the tavern in Secondale.
A messenger from the castle arrives with a letter from the king,
he requests your help with rescuing the princess who has been kidnapped by a magician who worships the demon king.
""")
    desc_em = typinginput("""
Do you want to save the princess? (yes,no) """).lower()
    if desc_em == "yes" or desc_em == "y":
        if str > 10:
            save_mission()
            coins += 10
            typingprint(f" The king rewards you for your bravery your new coin balance is {coins}!")

        else:
            typingprint("You do not have the strength required to defeat the magician, you are not able to save the princess")
            go_jail()

    elif desc_em == "no" or desc_em == "n":
        go_jail()
    else:
        typingprint("Wrong input try again..."), elie_mission()

def run_credits ():
    typingprint("Thank You for playing Saving Elfhiem")
    typingprint("This game was sponsored by sleepless nights, strained eyes and headaches...")
    typingprint("This game was a production of Desk 2")
    typingprint("Kelsey, Joe, Ragi, Elie!")
    sys.exit()

def go_jail():
    global coins
    if coins < 5:
        run_credits()
    else: 
        coins -= 5
        typingprint("You went to jail, you paid 5 coins to get out...")
        typingprint(f"You have {coins} coins left in your purse")

elie_mission()


typingprint ("""
While on your adventure you come across a town that appears 
to have been recently attacked, a man approaches you.""")

typingprint ("""
He introduces himself as Solomon. He is the chief of Leafdale village. He explains that this village is near the
demon lords territory and some of his troops have taken up residence in one of the nearby caves, 
the demons have been attacking the village at night and kidnapping villagers. 
""")

def desc_sq3():
    print()
    desc3 = typinginput("Will you brave hero please help our village and save our people? (yes/no)... ")
    if desc3 == "yes":
        print()
        typingprint("thank you brave hero, they will attack at tonight, good luck.")
        typingprint("""
You wait until nightfall and see a small group of low level demons, you swiflty defeat the demons that have attacked 
the town. After the battle, you notice one survior from the demons group, he begs you not to kill him and he will
show you where the captives are.""")
        start_quest()
    elif desc3 == "no":
        print()
        typingprint("some hero you are. You best be off before they come tonight.")
        leave_quest()
    else :
        print()
        typingprint("wrong input, try again"), desc_sq3()



def start_quest():
    global coins
    print()
    desc4 = typinginput("If you spare the demon you can follow him to the cave where the villigers are being held. (spare/kill)... ")
    if desc4 == "spare":
        print()
        typingprint("""He gestures to you a thanks and runs off, you follow at a distance to make sure it isnt a trap
and see that he has walked into the first cave.""")
    elif desc4 == "kill":
        coins += 15
        typingprint(f"""The villagers reward you, you now posses {coins} coins... They also thank you for your help 
and point you to the direction of the caves to rescue the kidnapped villagers""")
    else:
        typingprint("Wrong input, Try again...")
        start_quest()
        


    
def leave_quest():
    print()
    typingprint("You leave and can hear screaming in the distance from which you came.")


desc_sq3()
print()
typingprint ("As you were walking and you find the three caves")

print("""
**********************************************************************************
*                    /   \              /'\       _                              *
*\_..           /'.,/     \_         .,'   \     / \_                            *
*    \         /            \      _/       \_  /    \     _                     *
*     \__,.   /              \    /           \/.,   _|  _/ \                    *
*          \_/                \  /',.,''\      \_ \_/  \/    \                   *
*                           _  \/   /    ',../',.\    _/      \                  *
*             /           _/m\  \  /    |         \  /.,/'\   _\                 *
*           _/           /MMmm\  \_     |          \/      \_/  \                *
*          /      \     |MMMMmm|   \__   \          \_       \   \_              *
*                  \   /MMMMMMm|      \   \           \       \    \             *
*                   \  |MMMMMMmm\      \___            \_      \_   \            *
*                    \|MMMMMMMMmm|____.'  /\_            \       \   \_          *
*                    /'.,___________...,,'   \            \   \        \         *
*                   /       \          |      \    |__     \   \_       \        *
*                 _/        |           \      \_     \     \    \       \_      *
*                /                               \     \     \_   \        \     *
*                                                 \     \      \   \__      \    *
*                                                  \     \_     \     \      \   *
*                                                   |      \     \     \      \  *
*                                                    \ms          |            \ *
********************************************************************************** """)

def cave1():
    typingprint(""" 
You enter the cave and see the villagers that have been kidnapped and they are being held by one of the Demon kings generals nammed,
Bealzabub, the villagers appear unharmed, you attack Bealzabub and defeat him.
After you defeat him you set the villagers free.
""")
    typinginput_cave1 = typinginput("Would you like to go back and explore the other caves or leave and go to the shop (back/shop)")
    if typinginput_cave1 == "back":
        typingprint("Exiting cave 1")
        enter_cave()
    elif typinginput_cave1 == "shop":
        typingprint("Exiting cave 1")
        the_shop()
    else:
        typingprint("Wrong input"), cave1()

#def game_over():
    #typingprint ("GAME OVER")
    #sys.exit()

def cave2():
    global chance
    global hp
    if chance == 0 :
        print()
        typingprint("The cave was a trap. You die Game Over")
        run_credits()
    elif chance == 1 :
        hp -= hp
        hp += 15
        typingprint(f"The cave was a pitfall trap. on the brink of death you used the item, your health has been restored to {hp}HP")
        chance -=1
        typinginput_cave2 = typinginput("Would you like to go back and explore the other caves or leave and go to the shop (back/shop)")
        if typinginput_cave2 == "back":
            typingprint("Exiting cave 2, but BEAWARE of entering again...")
            enter_cave()
        elif typinginput_cave2 == "shop":
            typingprint("Exiting cave 2")
            the_shop()
        else:
            typingprint("Wrong input"), the_shop()
    
    
f_item = 0
f_item_times = 1
h_n_s_times = 1
def the_shop():
    global hp
    global str
    global coins
    global h_n_s_times
    global f_item
    global f_item_times
    shop_typinginput = typinginput("""
        
1. Buy HP and strength 
2. Buy the forbidden item
3. Go back to the caves
4. Continue journey
What do you want to do? (1/2/3/4)...""")
    if shop_typinginput == "1":
        if h_n_s_times == 0:
            typingprint("You already redeemed the health and strength boost!")
            the_shop()
        else:
            typingprint(f"You have {coins} in your purse...")
            h_n_s = typinginput("Would you like to buy 10 health and 10 strengh for 15 coins (yes/no)...")
            if h_n_s == "yes":
                if coins < 15:
                    typingprint ("Insufficient amount..."), the_shop()
                else:
                    coins -= 15
                    hp += 10
                    str += 10
                    h_n_s_times -= 1
                    typingprint(f"You now have {hp} health and {str} strengh, and your coin balance is now {coins}")
                    the_shop()
            elif h_n_s == "no":
                typingprint("Returning to the shop...")
                the_shop()
            else:
                typingprint("Wrong input...")
                print()
                typingprint("Returning to the shop")
                the_shop()
    elif shop_typinginput == "2":
        if f_item_times == 0:
            typingprint("You already redeemed the forbidden item!")
            the_shop()
        else:
            typingprint(f"You have {coins} in your purse...")
            f_item_buy = typinginput("Would you like to buy the forbidden item for 30 coins (yes/no)...")
            if f_item_buy == "yes":
                if coins < 30:
                    typingprint("Insufficient amount of coins..."), the_shop()
                else:
                    coins -= 30
                    f_item_times -= 1
                    f_item += 1
                    typingprint(f"You now have {f_item} forbidden item, and your coin balance is now {coins}")
                    the_shop()
            elif f_item_buy == "no":
                typingprint("Returning to the shop...")
                the_shop()
            else:
               typingprint("Wrong input..."), the_shop() 
    elif shop_typinginput == "3":
        enter_cave()
    elif shop_typinginput == "4":
        print()
    else:
        typingprint("Wrong input..."), the_shop()




card1 = ("""
 _____
|1    |
|     |
|  &  |
|     |
|____1|""")

card2 = ("""
 _____
|2    |
|  &  |
|     |
|  &  |
|____2|""")

card3 = ("""
 _____
|3    |
| & & |
|     |
|  &  |
|____3|""")

card4 = ("""
 _____
|4    |
| & & |
|     |
| & & |
|____4|""")

card5 = ("""
 _____
|5    |
| & & |
|  &  |
| & & |
|____5|""")

card6 = ("""
 _____ 
|6    |
| & & | 
| & & |
| & & |
|____6|""")

card7 = ("""
 _____
|7    |
| & & |
|& & &|
| & & |
|____7|""")

card8 = ("""
 _____
|8    |
|& & &|
| & & |
|& & &|
|____8|""")

card9 = ("""
 _____
|9    |
|& & &|
|& & &|
|& & &|
|____9|""")

card10 = ("""
 _____ 
|10 & |
|& & &|
|& & &|
|& & &|
|___0I|""")


def ragi_mission():
    typingprint("You were walking and feel a sadistic aura that make your hair raise.")
    print()
    typingprint("You see a feared mage in sight and he welcomes you and asks you if you want play?")
    print()
    typinginput_rm = typinginput("Do you want to play? ")

    if typinginput_rm == "yes" or typinginput_rm == "y":
        typingprint("""The game is simple; try get as close to 21 points as you can without going over 21.
You will be given 2 cards and you either take extra cards to add points or stop,
if you stop and I (the mage) have more than you; you will face the consequences...""")
        ragi_game()
    elif typinginput_rm == "no" or typinginput_rm == "n":
        typingprint("hahaha it's too late to run away")
        print()
        typingprint("""The game is simple; try get as close to 21 points as you can without going over 21.
You will be given 2 cards and you either take another card to add points or stop,
if you stop and I (the mage) have more than you; you will face the consequences...""")
        ragi_game()
    else:
        typingprint("Worng input...Try again.")
        ragi_mission()

sum = 0

def ragi_game():
    global sum
    draw1 = random.randint(1,10)
    if draw1 == 1:
        typingprint(card1)
    elif draw1 == 2:
        typingprint(card2)
    elif draw1 == 3:
        typingprint(card3)
    elif draw1 == 4:
        typingprint(card4)
    elif draw1 == 5:
        typingprint(card5)
    elif draw1 == 6:
        typingprint(card6)
    elif draw1 == 7:
        typingprint(card7)
    elif draw1 == 8:
        typingprint(card8)
    elif draw1 == 9:
        typingprint(card9)
    elif draw1 == 10:
        typingprint(card10)
    else:
        typingprint("Code broke")

    draw2 = random.randint(1,10)
    if draw2 == 1:
        typingprint(card1)
    elif draw2 == 2:
        typingprint(card2)
    elif draw2 == 3:
        typingprint(card3)
    elif draw2 == 4:
        typingprint(card4)
    elif draw2 == 5:
        typingprint(card5)
    elif draw2 == 6:
        typingprint(card6)
    elif draw2 == 7:
        typingprint(card7)
    elif draw2 == 8:
        typingprint(card8)
    elif draw2 == 9:
        typingprint(card9)
    elif draw2 == 10:
        typingprint(card10)
    else:
        typingprint ("code broke")
    
    sum = draw1 + draw2
    print()
    typingprint(f"You drew a {draw1} and a {draw2}, your total now is {sum}...")
    print()
    typingprint("What's your next step... be careful...")
    hit()



def hit():
    global sum
    global hp
    global str
    global coins
    global companionvalue
    if sum > 21:
        print()
        typingprint("You went over 21, you lost! I'm throwing you in jail haha")
        mage_jail()
    else:
        draw_or_stop = typinginput(" Would you like to draw or stop? (draw/stop)... ").lower()
        if draw_or_stop == "draw" or draw_or_stop == "d":
            draw3 = random.randint(1,10)
            if draw3 == 1:
                typingprint(card1)
            elif draw3 == 2:
                typingprint(card2)
            elif draw3 == 3:
                typingprint(card3)
            elif draw3 == 4:
                typingprint(card4)
            elif draw3 == 5:
                typingprint(card5)
            elif draw3 == 6:
                typingprint(card6)
            elif draw3 == 7:
                typingprint(card7)
            elif draw3 == 8:
                typingprint(card8)
            elif draw3 == 9:
                typingprint(card9)
            elif draw3 == 10:
                typingprint(card10)
            else:
                typingprint("Code broke")
            sum += draw3
            print()
            typingprint(f" your new total is {sum}")
            hit()

        elif draw_or_stop == "stop" or draw_or_stop == "s":
            mage_value = random.randint(12,21)
            typingprint(f"The mage got {mage_value} points!")
            if sum > mage_value:
                str += 10
                coins += 15
                typingprint(f" You won!! your new coin balance is {coins}.")
                print()
                typingprint(f"The mage gives you a strength potion, your new strength is {str}")
                print()
                typingprint("Going to the shop...")
                the_shop()
            elif sum == mage_value:
                str += 5
                coins += 5
                print()
                typingprint(f"You drew!! your new coin balance is {coins}")
                print()
                typingprint(f"The mage gives you a strength potion for your bravery, your new strength is {str}")
                print()
                typingprint("Going to the shop...")
                the_shop()
            elif sum < mage_value:
                print()
                typingprint("You are going to jail!")
                mage_jail()
        else:
            ("Wrong input..."), hit()
    



def mage_jail():
    global companionvalue
    global coins
    if companionvalue == 1:
        print()
        typingprint ("Your companion bailed you out of jail!")
        print()
        typingprint("Going to the shop...")
        the_shop()
    elif companionvalue == 0:
        if coins < 12:
            typingprint("You do not have enough coins to pay your way out of jail.")
            run_credits()
        else:
            coins -= 10
            typingprint (f"You paid 10 coins to get out of jail, you have {coins} left in your purse!")
            typingprint("Going back to the shop...")
            the_shop()
    else:
        typingprint("code broke")



def enter_cave():
    print()
    cave_choice = int(typinginput("Which cave would you like to explore (1,2,3)... "))
    if cave_choice == 1:
        typingprint ("Entering Cave 1")
        print()
        cave1()
    elif cave_choice == 2:
        print()
        typingprint("Entering cave 2")
        print()
        cave2()
    elif cave_choice == 3:
        print()
        typingprint("Entering cave 3")
        print()
        ragi_mission()
    else:
        typingprint("Wrong input, Try again...")
        enter_cave()

enter_cave()

boss_hp = 100

def boss_health():
    global boss_hp
    global f_item

    print("""
X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X
|                           ,,'``````````````',,                            |
X                        ,'`                   `',                          X
|                      ,'                         ',                        |
X                    ,'          ;       ;          ',                      X
|       (           ;             ;     ;             ;     (               |
X        )         ;              ;     ;              ;     )              X
|       (         ;                ;   ;                ;   (               |
X        )    ;   ;    ,,'```',,,   ; ;   ,,,'```',,    ;   ;               X
|       (    ; ',;   '`          `',   ,'`          `'   ;,' ;              |
X        )  ; ;`,`',  _--~~~~--__   ' '   __--~~~~--_  ,'`,'; ;     )       X
|       (    ; `,' ; :  /       \~~-___-~~/       \  : ; ',' ;     (        |
X  )     )   )',  ;   -_\  o    /  '   '  \    o  /_-   ;  ,'       )   (   X
| (     (   (   `;      ~-____--~'       '~--____-~      ;'  )     (     )  |
X  )     )   )   ;            ,`;,,,   ,,,;',            ;  (       )   (   X
| (     (   (  .  ;        ,'`  (__ '_' __)  `',        ;  . )     (     )  |
X  )     \/ ,".). ';    ,'`        ~~ ~~        `',    ;  .(.", \/  )   (   X
| (   , ,'|// / (/ ,;  '        _--~~-~~--_        '  ;, \)    \|', ,    )  |
X ,)  , \/ \|  \\,/  ;;       ,; |_| | |_| ;,       ;;  \,//  |/ \/ ,   ,   X
|",   .| \_ |\/ |#\_/;       ;_| : `~'~' : |_;       ;\_/#| \/| _/ |.   ,"  |
X#(,'  )  \\\#\ \##/)#;     :  `\/       \/   :     ;#(\##/ /#///  (  ',)# ,X
|| ) | \ |/ /#/ |#( \; ;     :               ;     ; ;/ )#| \#\ \| / | ( |) |
X\ |.\\ |\_/#| /#),,`   ;     ;./\_     _/\.;     ;   `,,(#\ |#\_/| //.| / ,X
| \\_/# |#\##/,,'`       ;     ~~--|~|~|--~~     ;       `',,\##/#| #\_// \/|
X  ##/#  #,,'`            ;        ~~~~~        ;            `',,#  #\##  //X
|####@,,'`                 `',               ,'`                 `',,@####| |
X#,,'`                        `',         ,'`                        `',,###X
|'  spb                          ~~-----~~                               `' |
X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X""")

    typingprint(f"""
You finally reach the Demon Kings castle, upon entering the castle the Demon King greets you with a smile
he says "I have been waiting {username}, lets begin...
 """)
    if f_item == 1:
        boss_hp /= 2
        f_item -= 1
        typingprint(f"You begin by using the forbidden item. The Demon Kings health is now {boss_hp} ")
    elif f_item == 0:
        boss_fight()



def boss_fight():
    typinginput("Type att to attack Yuno the demon King...")
    boss_dmg()
    boss_stop()
    print()
    player_hp()
    print()
    the_end()
    print()




def boss_dmg():
    global boss_hp
    global hp
    boss_damage = random.randint(0,6)
    hp -= boss_damage
    if hp <= 0:
        hp = 0
        typingprint(f"the boss dealt {boss_damage} damage, you now have {hp}HP")
        stop()
    else:
        typingprint(f"the boss dealt {boss_damage} damage, you now have {hp}HP")


def player_hp():
    global boss_hp
    global hp
    global str
    player_dmg = random.randint(0,str)
    boss_hp -= player_dmg
    if boss_hp <= 0:
        boss_hp = 0
        typingprint(f"You dealt {player_dmg} damage, Yuno now has {boss_hp}HP")
        boss_stop()
    else:
        typingprint(f"You dealt {player_dmg} damage, Yuno now has {boss_hp}HP")

def stop():
    global hp
    global chance
    if chance == 0:
        typingprint("You have died")
        typingprint("GAME OVER")
        run_credits()
    elif chance == 1:
        hp = 0
        hp += 30
        chance -= 1
        print()
        typingprint(f"You have been defeated. You used the item, your health is restored to {hp}HP. ")
        typingprint("Respawning at a tavern...")
        start_tavern()
        typingprint("You have been awarded a double attack.")
        boss_fight()


def the_end():
    if hp <=0 or boss_hp <= 0:
        typingprint ("The end...")
        typingprint("Game Over")
        run_credits()

def boss_stop():
    global boss_hp
    if boss_hp == 0:
        typingprint("You have defeated Demon King Yuno")
        typingprint("""
After you defeat Yuno the Demon King you make your way back to the Capital of Elfhiem. When you arrive tired
after your long journey back, you are greeted by crowds of people celebrating you, the king is waiting personally to thank you
for saving the kingdom, he invites you to a banquet in your honour. There he offers you to become a lord of leafdale village.
he also understands if you want to return home but he says "lets wait for that... Lets celebrate!!".
 """)
        run_credits()
    elif boss_hp <=0:
        boss_hp = 0
        typingprint("The Demon Kings health is 0. You have won.")
the_end()


boss_health()
#boss_fight()

while hp != 0 or boss_hp != 0 :
        boss_fight()
        # if hp == 1:
        #     stop()
        # elif hp <= 1:
        #     stop()
        # elif boss_hp == 1:
        #     typingprint("You have won")
        # elif boss_hp <= 1:
        #     typingprint("you win")

def run_credits ():
    typingprint("CREDITs credits credit credits")
    print()
    typingprint("This game was spomserd by sleepless nights")
    print()
    typingprint("This game was a production of Desk 2")
    print()
    typingprint("Kelsey Joe Ragi Elie")
    sys.exit()
  