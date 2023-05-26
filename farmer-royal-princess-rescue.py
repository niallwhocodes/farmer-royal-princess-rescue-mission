import time, sys, os, random

# Type-writer function
def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.035)
  
def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.035)
  value = input()  
  return value

# Function to clear terminal
def clearScreen():
  os.system("clear")

# Starting stats
health = 100
attack = 50
equipment_choice = None
dragons_health = 190
dragons_attack = 90
special_power = True


# Introduction

def welcome_message():
    print("""
█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀
▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄\n""")
    time.sleep(0.75)
    print("""
▀█▀ █▀█
░█░ █▄█\n""")
    time.sleep(0.75)
    print("""
▀█▀ █░█ █▀▀
░█░ █▀█ ██▄\n""")
    time.sleep(0.75)
    print("""
█▀ █░█ █▀█ █▀▀ █▀█
▄█ █▄█ █▀▀ ██▄ █▀▄\n""")
    time.sleep(1)
    print("""
▄▀█ █░█░█ █▀▀ █▀ █▀█ █▀▄▀█ █▀▀
█▀█ ▀▄▀▄▀ ██▄ ▄█ █▄█ █░▀░█ ██▄\n""")
    time.sleep(1)
    print("""
█▀▀ ▄▀█ █▀█ █▀▄▀█ █▀▀ █▀█
█▀░ █▀█ █▀▄ █░▀░█ ██▄ █▀▄\n""")
    time.sleep(1)
    print("""
█▀█ █▀█ █▄█ ▄▀█ █░░
█▀▄ █▄█ ░█░ █▀█ █▄▄\n""")
    time.sleep(1)
    print("""
█▀█ █▀█ █ █▄░█ █▀▀ █▀▀ █▀ █▀
█▀▀ █▀▄ █ █░▀█ █▄▄ ██▄ ▄█ ▄█\n""")
    time.sleep(1)
    print("""
█▀█ █▀▀ █▀ █▀▀ █░█ █▀▀
█▀▄ ██▄ ▄█ █▄▄ █▄█ ██▄\n""")
    time.sleep(1)
    print("""
█▀▄▀█ █ █▀ █▀ █ █▀█ █▄░█
█░▀░█ █ ▄█ ▄█ █ █▄█ █░▀█\n""")
    time.sleep(2.5)
    print("""
    (WITH DRAGONS)
""")
    time.sleep(2)
    press_enter()

def press_enter():
    start_button = typingInput("\n\nPress Enter to Play:\n> ")
    if start_button == "":
        typingPrint("\nENJOY!")
        time.sleep(2)
        clearScreen()
        intro()
    else:
        typingPrint("\nInvalid input. Please press enter!")
        press_enter()
        clearScreen()

def intro():
    typingPrint("You are an average farmer living in your mediocre village, doing another typical days worth of labor.\n")
    time.sleep(2)
    typingPrint("\nSuddenly your attention is grabbed by chatter and clamoring coming from the village square.\n\n")
    time.sleep(2)
    start_game()

def start_game():
    volunteer = typingInput("Do you decide to investigate the chatter or ignore it? (Investigate/Ignore):\n> ")
    if volunteer.lower() == "investigate":
        time.sleep(2)
        clearScreen()
        typingPrint("You put your tools down and head over to see what the commotion is.")
        time.sleep(2)
        typingPrint("\n\nYou discover there is a crowd of your fellow villagers gathered in front of some officials from the nearby ruling kingdom.")
        time.sleep(2)
        typingPrint("\n\nThey exclaim that the royal princess has been kidnapped by a dastardly wizard and on account of an intensive war that is currently\nbeing waged with a neighboring kingdom they're short on man power and need volunteers to aid in the princess's rescue.")
        time.sleep(3)
        ("\n\nNobody in the now silent and nervous crowd seems willing to volunteer.\n")
        rescue_decided()
        passed_gate()
        choose_your_path()
    elif volunteer.lower() == "ignore":
        typingPrint("\nYou decide it's none of your business and proceed to get back to work.")
        time.sleep(2)
        game_over()
    else:
        typingPrint("\nInvalid input. Please enter 'Investigate' or 'Ignore'.\n\n")
        start_game()
        clearScreen()

# Input for players name
def rescue_decided():
    volunteer_q = typingInput("\n\nDo you wish to volunteer? (Yes/No):\n> ")
    if volunteer_q.lower() == "yes":
        clearScreen()
        get_name = typingInput("The Head Official: Ah good, a volunteer! What is your name?\n\n(Type your name)\n> ")
        time.sleep(2)
        clearScreen()
        typingPrint(f"The Head Official: {get_name.capitalize()} is it? Come up to the front and stand with us.\n\n")
        typingPrint("Right, do we have any more volunteers?")
        time.sleep(2)
        typingPrint("\n\nThe crowd remains silent, many nervous looks and diverted eyes aplenty.\n\n")
        time.sleep(2)
        typingPrint(f"The Head Official: I see...\nWell, come with us {get_name.capitalize()}. We'll get you briefed and equipped for the journey ahead.\n\n")
        time.sleep(3)
        typingPrint("You follow the officials to a tent set up not too far from the village where you are briefed on your coming journey.\n")
        time.sleep(3)
        typingPrint("\nAn hour passes.")
        time.sleep(2)
        clearScreen()
        equipment_selection()
        front_of_castle()
    elif volunteer_q.lower() == "no":
        typingPrint("\nThe Head Official: Another letdown... Come on men, onto the next village!\n")
        time.sleep(2)
        clearScreen()
        typingPrint("\nNow the officials are gone you get back to your farming, those crops aren't going to harvest themselves!")
        time.sleep(2)
        game_over()
    else:
        typingPrint("\nInvalid input. Please enter 'Yes' or 'No'.")
        rescue_decided()

# Armoury. User chooses between opts a, b, c. Different stat changes based on this.

def equipment_selection():
    # Equipment Selection
    typingPrint("Alright! Now we have all the details out of the way, we don't expect you to take this task on with nothing\nbut the rags on your back, we have a selection of equipment for you to pick from.\n\nChoose wisely:\n\n")
    time.sleep(3)
    typingPrint("A) Sword, Shield, and Armor\n")
    time.sleep(1)
    typingPrint("Choosing Option A will double your health and attack points.\nYou're special ability is: Fire attacks only incur half the damage on you.\n\n")
    time.sleep(2)
    typingPrint("B) Cloak, Dagger, and Lockpick\n")
    time.sleep(1)
    typingPrint("Choosing Option B will have no change in your health and attack points.\nYou're special ability is: Lockpick (you can bypass any locked doors.)\n\n")
    time.sleep(2)
    typingPrint("C) Barrel of Beer, Rubber Chicken, and a Pair of Glasses with what appears to be a fake nose fashioned to it.\n")
    time.sleep(1)
    typingPrint("Choosing Option C will reduce your health by 10 points and increase your attack points by 10.\nYou're special ability is: UNKNOWN.\n\n")
    time.sleep(2)
    choice_a_b_c()


def choice_a_b_c():
    global equipment_choice
    equipment_choice = typingInput("So what will it be? (Choose A, B, or C)\n> ")
    time.sleep(2)
    if equipment_choice.lower() == "a":
        global health
        global attack
        global dragons_attack
        health = 200
        attack = 100
        dragons_attack = 45
        clearScreen()
        typingPrint("The Head Official: Someone who confronts their challenges with force and grit, I like that.")
        time.sleep(2.5)
        clearScreen()
        typingPrint(f"You have chosen option A.\nYour health is: {health}\nYour attack is: {attack}\nYour special ability has been activated")
        time.sleep(3)
        clearScreen()
    elif equipment_choice.lower() == "b":
        clearScreen()
        typingPrint("The Head Official: A cautious and pragmatic approach, seems you're quite the crafty one.")
        time.sleep(2.5)
        clearScreen()
        typingPrint(f"You have chosen option B.\nYour health is: {health}\nYour attack is: {attack}\nYour special ability has been activated")
        time.sleep(3)
        clearScreen()
    elif equipment_choice.lower() == "c":
        health = 90
        attack = 60
        clearScreen()
        typingPrint("The Head Official: ...What? Those are just miscellaneous items we had lying around. I mean... if you insist...?")
        time.sleep(2.5)
        clearScreen()
        typingPrint(f"You have chosen option C.\nYour health is: {health}\nYour attack is: {attack}\nYour special ability is still unknown.")
        time.sleep(3)
        clearScreen()
    else:
        typingPrint("\nInvalid input. Please choose A, B, or C.\n")
        choice_a_b_c()
    typingPrint("\nThe Head Official: Okay, now that you're geared up and know what the task at hand is we'll give you a map and a horse and set you on your way.\nAnd don't forget what we said in the briefing; there'll be a small troupe of soldiers and other volunteers who have already been sent ahead,\njoin up with them and rescue the princess together. Of with you now!\n")
    time.sleep(4)
    typingPrint("\nYou climb onto your horse and set out for the castle where the princess is being held by the evil wizard. The journey takes you two days.\n")
    time.sleep(3)
    clearScreen()

# You head to the front of the castle and are confronted by a riddle

# Riddle stats. Attempts start at zero and go up after each failed attempt. Attempts left reduces from 3 until the three attempts have occured. Required response for riddle is "dragon".
        
riddle_attempts = 0
attempts_left = 3
required_response = "dragon"

def front_of_castle():
    typingPrint("Upon your arrival at the wizards castle you approach the front gate and find a ghastly sight; the charred corpses of over half a dozen men.")
    time.sleep(2)
    typingPrint("\n\nYou notice a few of them have an insignia on what's left of their armor.")
    time.sleep(2)
    typingPrint("\n\nIt's the insignia of the kingdom, they must be the soldiers and other volunteers you were told about, what a grim end.")
    time.sleep(2)
    typingPrint("\n\nYou stand up with a feeling of loneliness and anxiety swelling inside you but you smoother your feelings and decide to continue.\n\n")
    time.sleep(2)
    clearScreen()
    typingPrint("You look ahead to the gate. It's huge, made of dense wood and reinforced with a thick but ornate iron frame.\n\n")
    time.sleep(2)
    typingPrint("A stone statue of a dragon stands on either side. There is a plaque in front of the gate.\n\n")
    time.sleep(2)
    global equipment_choice
    if equipment_choice.lower() == "b":
        typingPrint("You care not for the plaque and walk past it.\n\n") 
        time.sleep(1)
        typingPrint("You proceed to pick the gate's lock with your lockpick and open it.\n\n")
        time.sleep(1)
        open_door()
    else:
        typingPrint("The plaque has the following transcription:\n")
        time.sleep(1)
        riddle_plaque()
        riddle()    

# Separate function for the plaque to help when the user doesn't guess the riddle. It will not re-print the plaque again. 
def riddle_plaque():
    plaque = print("""
 __| |__________________________________________________| |__
(__   __________________________________________________   __)
   | |                                                  | |
   | | I fly and I soar. I love gold, nothing more.     | |
   | | When I breathe it will kill, dark places I fill. | |
   | |                                                  | |
   | | What am I? (1 word)                              | |
 __| |__________________________________________________| |__
(__   __________________________________________________   __)
   | |                                                  | |
    \n""")

# Input for the riddle. If answer is correct; door open function runs. If answer is incorrect; it checks the attempts through the failed riddle function 

def riddle():
    global riddle_attempts
    time.sleep(0.50)
    riddle_response = typingInput("What is your answer?\n> ")
    global required_response
    if riddle_response.lower() == required_response:
        time.sleep(1)
        open_door()
    else:
        global riddle_attempts
        riddle_attempts += 1
        failed_riddle()

# Function checks how many attempts have occurred. If 3, game over, else new attempt function is called.
def failed_riddle():
    global riddle_attempts
    if riddle_attempts == 3:
        game_over()
    else:
        new_attempt()

# Function for having a new attempt at the riddle
def new_attempt():
    global attempts_left, riddle_attempts
    attempts_left -= 1        
    typingPrint(f"Incorrect Answer. You have {attempts_left} attempts left. (Attempt: {riddle_attempts}/3)\n")
    riddle()

# This resets the riddle counters as we have another riddle further on in the game.
def reset_riddle_counters():
    global riddle_attempts, attempts_left
    riddle_attempts = 0
    attempts_left = 3


# User beats the riddle/has a lockpick (option B)
def open_door():
    global riddle_attempts, equipment_choice, attempts_left
    if riddle_attempts == 0:
        typingPrint("\nNow you're just showing off, go onward into the castle and face your destiny!\n")
        time.sleep(2)
        clearScreen()
        reset_riddle_counters()
    elif equipment_choice.lower() == "b":
        typingPrint("Go onward into the castle and face your destiny!\n")
        reset_riddle_counters()
        time.sleep(2)
        clearScreen()
    else:
        typingPrint("Got there eventually, go onward into the castle and face your destiny!\n")
        time.sleep(2)
        clearScreen()
        riddle_attempts = 0
        attempts_left = 3

# Once user beats door, it takes you to courtyard of castle. Ask you to make a choice between Tavern or Pantry.

def passed_gate():
    time.sleep(2)
    typingPrint("The gate opens up to a large courtyard with many paths and buildings, there is nobody to be seen.\n\n")
    time.sleep(2)
    typingPrint("You decide to start searching for the princess in the most immediate structures.\n\n")
    time.sleep(2)
    typingPrint("You see a tavern and a walk-in pantry.\n\n")
    time.sleep(2)

def choose_your_path():
    path = typingInput("Enter the TAVERN or enter the PANTRY?\n> ")
    if (path.lower() == "tavern"):
        time.sleep(1)
        clearScreen()
        typingPrint("You enter the tavern.\n")
        typingPrint("After a brief search you conclude the princess isn't on this floor.\nYou noticed there was a mug of fresh beer on the counter and you're rather thirsty.\n")
        drink_choice()
    elif (path.lower() == "pantry"):
        time.sleep(1)
        clearScreen()
        typingPrint("You enter the pantry, the aroma of delicious food lingers in the air.\n\n")
        time.sleep(2)
        typingPrint("Do you decide to stop to fill your stomach or do you continue your search?\n\n")
        food_choice()
    else:
        typingPrint("Input not recognized, try again.\n")
        choose_your_path()

# If user chooses tavern. You are asked if you want a drink or not. You gain attack but lose health if you do. Move on if not.

def drink_choice():
        drink = typingInput("DO YOU DRINK THE BEER, YES OR NO?\n> ")
        global attack, health
        if (drink.lower() == "yes"):
            typingPrint("You take a large gulp of the beer.\n")
            time.sleep(2)
            typingPrint("\nYou feel like you can now take on the world but you're also a little wobbly.\n\n")
            time.sleep(2)
            typingPrint("YOUR ATTACK POWER INCREASES BY 10 AND YOUR HEALTH POINTS DECREASE BY 10!\n\n")
            health -= 10
            attack += 10
            typingPrint(f"Your health is: {health}\nYour attack is: {attack}\n")
            time.sleep(2)
            clearScreen()
            typingPrint("After wiping your mouth clean you hear a cry for help coming from upstairs.\n")
            time.sleep(2)
            typingPrint("\nYou stammer into action and run up the stairs as fast as you can, tripping a few times in the process.\n")
            time.sleep(2)
            clearScreen()
            upstairs_door()
        elif (drink.lower() == "no"):
            typingPrint("You don't have time to indulge, you have to keep your wits about you.\n")
            typingPrint("Immediately after deciding against the beer you hear a cry for help coming from upstairs.\n")
            typingPrint("With your wits still intact you dart up the stairs.\n")
            time.sleep(2)
            clearScreen()
            upstairs_door()
        else:
             typingPrint("Input not recognized, try again.\n")
             drink_choice()


# If user chooses pantry. You are asked if you want a eat or searcg. You gain health if you eat. Move on if search.

def food_choice():
        food = typingInput("EAT OR SEARCH?\n> ")
        global health, attack
        if (food.lower() == "eat"):
            typingPrint("\nYou grab a large roasted ham and take a hearty bite out of it.\n")
            typingPrint("\nYour hunger sated, you feel stronger than ever.\n")
            typingPrint("\nYOU GAIN 10 HEALTH POINTS!\n")
            health += 10
            typingPrint(f"Your health is: {health}\nYour attack is: {attack}\n")
            time.sleep(3)
            clearScreen()
            typingPrint("Immediately after swallowing down your meal, you hear a cry for help coming from upstairs.\n\n")
            typingPrint("With a full belly; you dart upstairs.\n")
            time.sleep(4)
            clearScreen()
            upstairs_door()
        elif (food.lower() == "search"):
            typingPrint("\nYou decide you shouldn't really be induldging right now, you've got a job to do after all.\n")
            typingPrint("\nAs you are looking for any clues in the pantry you hear a cry for help coming from upstairs.\n")
            typingPrint("\nYou hurry up the stairs as fast as you can.\n")
            time.sleep(4)
            clearScreen()
            upstairs_door()
        else:
             typingPrint("Input not recognized, try again.\n")
             food_choice()

# User heads upstairs after hearing noise. Confronted with another riddle door.

def upstairs_door():
    typingPrint("After running up the stairs you come to a locked door.\n\n")
    time.sleep(2)
    global equipment_choice
    if equipment_choice.lower() == "b":
        typingPrint("Special Ability Activated. No need to waste your time on this stupid riddle.\n") 
        time.sleep(2)
        typingPrint("You use your lockpick to open the door.\n")
        time.sleep(2)
        open_upstairs_door()
        wizard_game()
    else:
        typingPrint("Similar to the gate at the front of the castle there is a plaque, it reads:\n")
        time.sleep(2)
        upstairs_riddle_plaque()
        upstairs_riddle()

def upstairs_riddle_plaque():
    plaque = print("""
 __| |__________________________________________________| |__
(__   __________________________________________________   __)
   | |                                                  | |
   | | I am always near, but never far.                 | |
   | |                                                  | |
   | | I am always around, but never seen.              | |
   | |                                                  | |
   | | I am often avoided, but I always catch up.       | |
   | |                                                  | |
   | | I will come when your old and grey,              | |
   | | or maybe even the very next day.                 | |
   | |                                                  | |
   | | I will come with cold embrace,                   | |
   | | and give you rest with which you must face.      | |
   | |                                                  | |
   | | I can come early but I'll never be late.         | |
   | |                                                  | |
   | | I am everyone's final fate.                      | |
   | |                                                  | |
   | |                                                  | |
   | | What am I? (1 word)                              | |
 __| |__________________________________________________| |__
(__   __________________________________________________   __)
   | |                                                  | | 
    \n""")
        

# Function works the same as front door riddle. If correct answer/lockpick you proceed. If wrong x3, game over

upstairs_required_response = "death"

def upstairs_riddle():
    global riddle_attempts, upstairs_required_response, attempts_left
    time.sleep(0.5)
    upstairs_riddle_response = typingInput("What is your answer?\n> ")
    if upstairs_riddle_response.lower() == upstairs_required_response:
        time.sleep(1)
        open_upstairs_door()
        wizard_game()
    else:
        riddle_attempts += 1
        attempts_left -= 1
        failed_upstairs_riddle()
        

def open_upstairs_door():
    global riddle_attempts, equipment_choice
    if riddle_attempts == 0:
        typingPrint("\nNow you're just showing off, go onward into the room and face your destiny!\n")
        time.sleep(2)
        clearScreen()
    elif equipment_choice.lower() == "b":
        typingPrint("Go onward into the room and face your destiny!\n")
        time.sleep(2)
        clearScreen()
    else:
        typingPrint("Got there eventually, go through the door and face what's ahead.\n")
        time.sleep(2)
        clearScreen()

def failed_upstairs_riddle():
    global riddle_attempts, attempts_left
    if riddle_attempts == 3:
        game_over()
    else:
        upstairs_new_attempt()

def upstairs_new_attempt():
    global riddle_attempts, attempts_left        
    typingPrint(f"Incorrect Answer. You have {attempts_left} attempts left. (Attempt: {riddle_attempts}/3)\n")
    time.sleep(1)
    upstairs_riddle()


# Once you enter the room there is a wizard who knows the location of the princess. He challenges you to a game of rock, paper, scissors. The wizard will direct you to the princess no matter what but if you beat him once out of three attempts he will give you an additional clue. If he wins you lose your special abilities. 

def wizard_game():
    typingPrint("You enter the room and you realise the screams you hear are from an iPhone 4 playing a recording.\n")
    time.sleep(2)
    typingPrint("\nYou see a wizard smirking in the corner of the room. He approaches you and proclaims: \n")
    time.sleep(2)
    print( """
 __________________________________
(  "To save the princess and rise  )
(   to fame, I'll give you a clue  )
(     should you win this game!"   )
'----------------------------------'           
             \            /^\ 
              \      /\   "V"
               \    /__ \  I
                \  //..\ \ I
                 \ \].`[/  I
                   /l\/j\  (]
                  /. ~~ ,\/I
                  \\L__j^\/I
                   \/--v}  I
                   |    |  I
                   |    |  I
                   |    l  I
                 _/j  L l\_!
""")
    time.sleep(2)
    typingPrint("The Wizard challenges you to a mighty game of...\n")
    time.sleep(2)
    typingPrint("\n~_~ Rock, Paper, Scissors ~_~\n")
    time.sleep(2)
    typingPrint("\nThe Wizard: Win once out of three attempts and I will hand over my clue, but lose and I will drain your special ability!\n\n")
    time.sleep(1)
    rock_paper_scissors()

# List of choices the wizard can make
game_random_options = [
    "Rock",
    "Paper",
    "Scissors"
]
game_attempts = 0

# Rock, paper, scissors game.

def rock_paper_scissors():
    global game_attempts, game_random_options
    wizards_choice = random.choice(game_random_options)
    users_choice = typingInput("Make your choice: Rock, Paper, Scissors\n> ")
    if users_choice.lower() == "rock" and wizards_choice == "Scissors":
        typingPrint(f"\nThe Wizard chose {wizards_choice}. You Win! The wizard will now give you your clue!\n")
        time.sleep(2)
        defeat_wizard()
    elif users_choice.lower() == "rock" and wizards_choice == "Paper":
        typingPrint(f"\nThe Wizard chose {wizards_choice}. Wizard Wins! Try Again.\n")
        game_attempts += 1
        defeated_by_wizard()
    elif users_choice.lower() == "rock" and wizards_choice == "Rock":
        typingPrint(f"\nThe Wizard chose {wizards_choice}. It's a tie! Try Again.\n")
        game_attempts += 1
        defeated_by_wizard()
    elif users_choice.lower() == "paper" and wizards_choice == "Scissors":
        typingPrint(f"\nThe Wizard chose {wizards_choice}. Wizard Wins! Try Again.\n")
        game_attempts +=1
        defeated_by_wizard()
    elif users_choice.lower() == "paper" and wizards_choice == "Paper":
        typingPrint(f"\nThe Wizard chose {wizards_choice}. It's a tie! Try Again.\n")
        game_attempts += 1
        defeated_by_wizard()
    elif users_choice.lower() == "paper" and wizards_choice == "Rock":
        typingPrint(f"\nThe Wizard chose {wizards_choice}. You Win! The wizard will now give you your clue!\n")
        defeat_wizard()
    elif users_choice.lower() == "scissors" and wizards_choice == "Rock":
        typingPrint(f"\nThe Wizard chose {wizards_choice}. Wizard Wins! Try Again.\n")
        game_attempts +=1
        defeated_by_wizard()
    elif users_choice.lower() == "scissors" and wizards_choice == "Scissors":
        typingPrint(f"\nThe Wizard chose {wizards_choice}. It's a tie! Try Again.\n")
        game_attempts += 1
        defeated_by_wizard()
    elif users_choice.lower() == "scissors" and wizards_choice == "Paper":
        typingPrint(f"\nThe Wizard chose {wizards_choice}. You Win! The wizard will now give you your clue!\n")
        defeat_wizard()
    else:
        typingPrint("Invalid response, please try again!\n\n")
        rock_paper_scissors()

# Outcome if you defeat the wizard
def defeat_wizard():
    clearScreen()
    typingPrint("The Wizard looked shocked. He had never lost this mighty game before.\n")
    time.sleep(2)
    print("""
 ______________________________________
(  "Go to the balcony that overlooks   )
(   the grand hall. There you will see )
(   your princess. As you won I will   )
(   give you my hint. The fastest way  )
(   down may not always be the best.   )
(            Now, be gone!"            )
'--------------------------------------'         
             \            /^\ 
              \      /\   "V"
               \    /__ \  I
                \  //..\ \ I
                 \ \]O`[/  I
                   /l\/j\  (]
                  /. ~~ ,\/I
                  \\L__j^\/I
                   \/--v}  I
                   |    |  I
                   |    |  I
                   |    l  I
                 _/j  L l\_!
    """)
    time.sleep(6)
    typingPrint("You proudly scurry out the room and make your way to the balcony that overlooks the grand hall.\n")
    time.sleep(4)
    clearScreen()
    balcony_choice_opening_text()

# Outcome if you are defeated
def defeated_by_wizard():
    global game_attempts
    if game_attempts == 3:
        clearScreen()
        typingPrint("The Wizard looked smug. His undefeated run was still in tact.\n")
        time.sleep(1.50)
        print("""
 ______________________________________
(  "Go to the balcony that overlooks   )
(  the grand hall. There you will see  )
(  your princess. As you have been     )
(  defeated, I will rid you of your    )
(  special ability.  Now, be gone!"    )
'--------------------------------------'        
             \            /^\ 
              \      / \  "V"
               \    /__ \  I
                \  //..\ \ I
                 \ \]>`[/  I
                   /l\/j\  (]
                  /. ~~ ,\/I
                  \\L__j^\/I
                   \/--v}  I
                   |    |  I
                   |    |  I
                   |    l  I
                 _/j  L l\_!
    """)
        lose_special_ability()
        time.sleep(6)
        typingPrint("\nYou scurry out the room feeling discouraged and make your way to the balcony that overlooks the grand hall.\n")
        time.sleep(4)
        clearScreen()
        balcony_choice_opening_text()
    
    else:
        rock_paper_scissors()

def lose_special_ability():
    global equipment_choice, dragons_attack, health, attack, special_power
    if equipment_choice.lower() == "a":
        dragons_attack = 90
        typingPrint("The dragon's attack is no longer halved - good luck in battle!\n")
        typingPrint(f"Your health is: {health}\nYour attack is: {attack}\nYour special ability has been removed")
        special_power = False
    elif equipment_choice.lower() == "b":
        typingPrint("You lose your lock-pick.\n")
        typingPrint(f"Your health is: {health}\nYour attack is: {attack}\nYour special ability has been removed")
        special_power = False
    else:
        typingPrint("You lose your crate of beers.\n")
        typingPrint(f"Your health is: {health}\nYour attack is: {attack}\nYour special ability has been removed")
        special_power = False

# User heads to balcony (as directed by the wizard). You see the dragon surronding the princess. There are two ways down. Stairs or Jump. You must choose. If you take the stairs (as hinted by the Wizard), you are granted extra health. You lose health if you jump

def balcony_choice_opening_text():
    typingPrint("You look out from castle balcony and you see... none other than a mighty dragon, it's body coiling around the princess.\n\n")
    time.sleep(2)
    typingPrint("You pause in shock as the dragon stares at you from across the room, it's eyes at the same level as yours.\n\n")
    time.sleep(3)
    print("""
           _--^^^#####/ /      \ \#####^^^--_
        _-^##########/ / (    ) \ \##########^-_
       -############/ /  |\^^/|  \ \############-
     _/############/ /  ((@::@))  \ \############\_
    /#############( (    \ \/ /    ) )#############\ 
   -###############\ \    (oo)    / /###############-
  -#################\ \  / VV \  / /#################-
 -###################\ \/      \/ /###################-
_#/|##########/\######(    /\    )######/\##########|\#_
 |/ |#/\#/\#/\/  \#/\##\  |  |  /##/\#/  \/\#/\#/\#| \|
 `  |/  V  V  `   V  \#\| |  | |/#/  V   '  V  V  \|  '
    `   `  `      `   / | |  | | \   '      '  '   '
                     (  | |  | |  )
                    __\ | |  | | /__
                   (vvv(VVV) (VVV)vvv)
\n\n""")
    time.sleep(2)
    typingPrint("From what you can see there are two ways down. What do you do?\n")
    typingPrint("1. Jump down the curtain from the balcony?\n")
    typingPrint("2. Run down the stairs?\n")
    balcony_decision()

def balcony_decision():
    global health, attack
    choice = int(typingInput("Enter your choice (1 or 2):\n> "))
    if choice == 1:
        typingPrint("You jump down the curtain from the balcony and land hard on the ground below.\n")
        health -= 10
        typingPrint(f"You lose 10 health points. Your health is now: {health}\n")
        time.sleep(2)
        clearScreen()
        dragon_battle()
    elif choice == 2:
        typingPrint("You run down the stairs and avoid the dangerous jump. You find a med-kit on the stairs and apply it.\nYou start to feel a bit fatiqued from taking the stairs.\n")
        health += 10
        attack -= 5
        typingPrint(f"You gained 10 health points and lose 5 attack points.\nYour health is now: {health}\nYour attack is now: {attack}\n")
        time.sleep(2)
        clearScreen()
        dragon_battle()
    else:
        typingPrint("Invalid choice! Please enter 1 or 2.\n")
        balcony_decision()

# You get the dragon and get asked if you wish to attack or run. Attack will do as it says and start an attack sequence, run will make you turn around and go back to your farm (game over).

battle_choice = None

def dragon_battle():
    global special_power, battle_choice
    typingPrint("You approach the dragon and prepare yourself for battle!\n")
    battle_choice = typingInput("You have two options. Do you ATTACK or do you RUN?\n> ")
    if battle_choice.lower() == "attack" and special_power == True:
        special_power_battle()
    elif battle_choice.lower() == "attack" and special_power == False:
        no_special_power_battle()
    elif battle_choice.lower() == "run":
        typingPrint("Yeaaaaaah... not for me - you preclaim. You turn around and go back to your farm.\n")
        time.sleep(2)
        game_over()
    else:
        typingPrint("Invalid Selection. Please type (Run/Attack).\n")

# Outcome if you defeated the wizard
def special_power_battle():
    global equipment_choice
    if equipment_choice.lower() == "c":
        battle_option_c()
    elif equipment_choice.lower == "b":
        you_attack_dragon()
    else:
        you_attack_dragon()

# Outcome if you were defeated by the wizard
def no_special_power_battle():
    global equipment_choice
    if equipment_choice.lower() == "c":
        you_attack_dragon()
    elif equipment_choice.lower == "b":
        you_attack_dragon()
    else:
        you_attack_dragon()
    
# You attack the dragon. If you dont defeat it, the dragon attacks back.
def you_attack_dragon():
    global attack, dragons_health
    dragons_health -= attack
    if dragons_health <= 0:
        time.sleep(1)
        game_won()
    else:
        dragon_attacks_you()
        
# Dragon attacks back if you dont already defeat it.
def dragon_attacks_you():
    global health, dragons_attack
    typingPrint("You deal a mighty blow to the dragon, rending some of it's scales and causing it to cry out in pain.")
    typingPrint("\n\nThe furious dragon retaliates with a mighty flame attack.\n\n")
    health -= dragons_attack
    if health <= 0:
        typingPrint("The dragon's breath overcomes you and reduces your body to a pile of ash. Better luck next time!\n")
        time.sleep(2)
        clearScreen()
        time.sleep(2)
        print("""
MMMMMMMMMMMMMMMMMMMMMMMMMWNXX0kdloxOKXXNWMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMW0dlccc:;;;;:cclo0WMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMWX0xc;;;,;;,,,,,;;;:dXMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMWKdc::;;,,,;;,,,,,;,,;:oONMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMNkc,,,,;;,,,,,,,,,,;,,',::oOXWWMMMMMMMMMMMM
MMMMMMMMMMMMWXX0kkl,,,,,;,',,,'',,,,,;,'',,;:lddONMMMMMMMMMM
MMMMMMMMMWX0xc::;;;;;;,,,'',;'.',,,,,,;;,',;;;;;cxO0KXWMMMMM
MMMMMMNOxdl:;'','.',,,,;;,;;;,,,,,,,,,;;,',,,,,,;;;::ldkXMMM
MMMWXkoc;;;;;,'''.',;,,,,,,,,;;;,,,,,,,,'.',,,,,,,,,,,,;l0WM
MMMNkc:,,,;;,,''',;;,,,,,'',,,,,,,'''''','''',;;;,,;;,;:cxKW
NWN0dc;;;;;;,,,,,,;;,,,;;;;;;,'','',,;;',;;;,,;;;:clllcokXNW
NNNX0kxxdoodolllcc:::;;,;::::;,,;;:;:::;;ccclodxk0KKKK00XWMM
MMMMMMMMWNNNNNNNNXXK0OkkxxxxkkOOO0000000000KXXNWWMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMWWWWWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMM
        \n""")
        time.sleep(6)
        game_over()
    else:
        typingPrint(f"The attack causes damage but you survive. Your health is {health}.\n\n")
        attack_again()
        you_attack_dragon()

def attack_again():
    second_battle_choice = typingInput("You are still going strong. Do you want to ATTACK again or do you RUN?\n> ")
    if second_battle_choice.lower() == "attack" and special_power == True:
        special_power_battle()
    elif second_battle_choice.lower() == "attack" and special_power == False:
        no_special_power_battle()
    elif second_battle_choice.lower() == "run":
        typingPrint("Well... I tried my best - you preclaim. You turn around and go back to your farm.\n")
        time.sleep(2)
        game_over()
    else:
        typingPrint("Invalid Selection. Please type (Run/Attack).\n")

# If you chose option C at the start and you still have your special ability; this will be activated.
def battle_option_c():
    global battle_choice
    if battle_choice.lower() == "attack":
        typingPrint("SPECIAL ABILITY ACTIVATED: BEER POWER\n")
        special_attack()
    elif battle_choice.lower() == "run":
        typingPrint("Yeaaaaaah... not for me - you preclaim. You turn around and go back to your farm.\n")
        time.sleep(2)
        game_over()
    else:
        typingPrint("Invalid Selection. Please type (Run/Attack).\n")

# The special attack is used instead of a normal attack. This is a beer throw and defeats the dragon immediately (the dragon is allergic to beer).
def special_attack():
    typingPrint("You throw your beer and rubber chicken at the dragon.\n")
    typingPrint("You hear a sizzling sound\n")
    time.sleep(2)
    typingPrint("The Dragon starts disintegrating. It turns out this beast is allergic to yeast.\n")
    game_won()

        
# What appears if you win the game and defeat the dragon.
def game_won():
    typingPrint("\nYou deal a devastating blow to the dragon, scales and blood flying through the air as the dragon screams in agony!")
    time.sleep(2)
    typingPrint("\n\nYou are then met with a brief silence followed by a thunderous quake as the dragon's lifeless body topples to the ground.")
    typingPrint("\n\nYou have successfully slain the dragon. Now go forth and greet your princess.\n")
    time.sleep(1)
    typingPrint("1 STEP...\n")
    time.sleep(2)
    typingPrint("   2 STEP...\n")
    time.sleep(1)
    typingPrint("       3 ST..\n")
    print("**THE PRINCESS SLAPS YOU ACROSS THE CHEEK**\n\n")
    time.sleep(3)
    typingPrint("Princess: What took you so long?\n")
    time.sleep(2)
    typingPrint("You look bemused!?! You and the princess walk back to your kingdom...")
    time.sleep(1.50)
    typingPrint("seperately...")
    time.sleep(4)
    typingPrint("six feet apart")
    time.sleep(2)
    clearScreen()
    time.sleep(2.50)
    print("""
                                                        ,jf
   _am,    ,_am,  ,_g_oam,    _am,   _g_ag,   _am,   koewkovg   _mm_
 ,gF  @._-gF   @-"  jf   @  ,gF  @  ^ NX  #_,gF  @     jf      qK  "
 8Y      8Y    d   j#   jF .8Y  ,d   dY     8Y   d    jf       *b,
jK   ,  jK   ,N   jN   jF  :K  ,Z  ,jF     jK  ,Z"  ,jfk,       dN.
 NbpP    NbpP    dP   dFk_o8NbpP"V^dF       NbpY"V^"dF "dYo-"*h,W"
                         ,gF',@'
                        :8K  j8
                         "*w*"

    \n""")
    typingPrint("YOU HAVE BEATEN THE GAME - WELL DONE")
    time.sleep(5)
    quit()


# What appears if you lose the game at any point
def game_over():
    clearScreen()
    time.sleep(2.50)
    print("""

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⢀⣤⣤⣤⣶⣶⣷⣤⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣶⣶⠀⠀⠀⠀⣠⣾⣿⣿⡇⠀⣿⣿⣿⣿⠿⠛⠉⠉⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⠀⠀⠀⠀⠀⢀⣿⣿⣶⡀⠀⠀⠀⠀⠀⣾⣿⣿⣿⡄⠀⢀⣴⣿⣿⣿⣿⠁⢸⣿⣿⣿⣀⣤⡀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣴⣶⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⣼⣿⣿⣿⣧⠀⠀⠀⠀⢰⣿⣿⣿⣿⣇⣠⣿⣿⣿⣿⣿⡏⢠⣿⣿⣿⣿⣿⡿⠗⠂⠀⠀
⠀⠀⠀⣰⣾⣿⣿⠟⠛⠉⠉⠉⠉⠋⠀⠀⠀⣰⣿⣿⣿⣿⣿⣇⣠⣤⣤⣿⣿⣿⢿⣿⣿⣿⣿⢿⣿⣿⡿⠀⣼⣿⣿⡟⠉⠁⢀⣀⡄⠀⠀
⠀⢀⣾⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣴⣿⣿⣿⣿⡿⣿⣿⣿⡏⠈⢿⣿⣿⠏⣾⣿⣿⠃⢠⣿⣿⣿⣶⣶⣿⣿⣿⡷⠦⠀
⢠⣾⣿⡿⠀⠀⠀⣀⣠⣴⣶⣿⣿⡷⠀⣠⣿⣿⣿⣿⡿⠟⣿⣿⣿⣠⣿⣿⣿⠀⠀⠀⠀⠁⢸⣿⣿⡏⠀⣼⣿⣿⣿⠿⠛⠛⠉⠀⠀⠀⠀
⢸⣿⣿⠣⣴⣾⣿⣿⣿⣿⣿⣿⡿⠃⣰⣿⣿⣿⠋⠁⠀⠀⠸⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠸⠿⠿⠀⠀⠛⠛⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠸⣿⣿⣆⣉⣻⣭⣿⣿⣿⡿⠋⠀⠀⢿⣿⡿⠁⠀⠀⠀⠀⠀⠹⠟⠛⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠙⠿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣶⣶⣶⣶⣦⣄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣷⠄⣤⣤⣤⣤⣶⣾⣷⣴⣿⣿⣿⣿⠿⠿⠛⣻⣿⣿⣷⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣄⠀⣶⣶⣤⡀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠋⢠⣿⣿⣿⠿⠛⠋⠉⠛⣿⣿⣿⠏⢀⣤⣾⣿⣿⡿⠋⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⠓⢹⣿⣿⣷⠀⠀⠀⠀⢀⣶⣿⡿⠁⠀⣾⣿⣿⣟⣠⣤⠀⠀⢸⣿⣿⣿⣾⣿⣿⣿⡟⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⡿⠛⠉⠸⣿⣦⡈⣿⣿⣿⡇⠀⠀⣰⣿⣿⡿⠁⠀⢸⣿⣿⣿⣿⣿⠿⠷⢀⣿⣿⣿⣿⡿⠛⣿⣿⣿⡀⠀⠀⠀
⠀⠀⠀⠀⢀⣼⣿⣿⡿⠋⠀⠀⠀⠀⣿⣿⣧⠘⣿⣿⣿⡀⣼⣿⣿⡟⠀⠀⢀⣿⣿⣿⠋⠁⠀⣀⣀⣼⣿⣿⡟⠁⠀⠀⠘⣿⣿⣧⠀⠀⠀
⠀⠀⠀⠀⣼⣿⣿⡟⠀⠀⠀⠀⠀⣠⣿⣿⣿⠀⢹⣿⣿⣿⣿⣿⡟⠀⠀⠀⣼⣿⣿⣷⣶⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠸⣿⣿⡆⠀⠀
⠀⠀⠀⠀⢹⣿⣿⣇⠀⠀⢀⣠⣴⣿⣿⣿⡿⠀⠈⣿⣿⣿⣿⡟⠀⠀⠀⢰⣿⣿⣿⠿⠟⠛⠉⠁⠸⢿⡟⠀⠀⠀⠀⠀⠀⠀⠘⠋⠁⠀⠀
⠀⠀⠀⠀⠈⢻⣿⣿⣿⣾⣿⣿⣿⣿⣿⠟⠁⠀⠀⠸⣿⣿⡿⠁⠀⠀⠀⠈⠙⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠛⠿⠿⠿⠿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    CREATED BY: TEAM 2
    ADENIYI, MEHEMED, NIALL, NICKOLAS, WAHBALLA, YEMI
                    
""")
    typingPrint("You didn't save the princess!\n\n")

    restart()

def restart():
    restart_game = typingInput("Do you wish to play again? (Yes/No)\n> ")
    if restart_game.lower() == "no":
        exit()
    elif restart_game.lower() == "yes":
        clearScreen()
        time.sleep(2)
        welcome_message()
    else:
        typingPrint("Invalid input. Please type: yes or no\n")
        restart()

welcome_message()