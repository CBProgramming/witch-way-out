# Agile Development Project The Delusionist's
# Witch Way Out

import random
import os
import time

def intro():
    print ("\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n")
    print ("""You have woken up in a strange room, it’s dark and scary. You shout out “Mum…… Dad!!!”.""")
    print ("There is only silence, oddly far more deafening. You take a look around, trying to make out what little you can.")
    print ("As your eyes adjust you can make out the shape of a window, the outline of the curtain is illuminated by what little light is coming in from outside.")
    print ("You look to your left, eyes now more adjusted to the dark, to see the outline of a door.\n ")

def invalid_option(choice,last_number):
    valid_option = False
    while valid_option == False:
        if choice < 1 or choice > last_number:
            print ("Invalid choice, please choose again\n")
            valid_option = True            
        else:
            valid_option = True
        
        
def firstroom(puzzle_answer):

 

    valid_choice = False

    note_obtained = False

    while valid_choice == False:

        print ("PLEASE CHOOSE ONE OF THE FOLLOWING OPTIONS:", )

        print ("Option 1: Go to the door")

        print ("Option 2: Go to the window")

        playerchoice = input("Option 3: Search the room\n")

        if playerchoice.isdigit():

            playerchoice = int(playerchoice)

        if playerchoice == 1:

            print("You make your way over to the door, the floorboards creaking step by step. You can make out faint details of the door.")

            print("It looks old and decrepit, paint peeling off with cracks covering the door. You reach out for the handle and can feel the rusted rough surface. You turn the knob.")

            print("""The door is locked, “Of course” you say to yourself. Looking around, trying to find a way through, you notice a keypad. “This keypad must open the door” you think to yourself.\n""")

            valid_choice = True

        elif playerchoice == 2:

            print("You make your way over to the window, the floorboards creaking step by step. You open the curtains and peer out.")

            print ("It’s barred. Clearly whoever brought you here doesn’t want you to leave. Looking out further beyond the bars all you can see are trees and rocks casting silhouettes in the dim moonlight.\n")

            print ("As you stare into the abyss you are suddenly filled with dread. You remember! You remember what happened to you... how you got into this situation and what put you here.")

            print ("You were taken here by the witches, their only goal is to rid the world of children!\n")

            valid_choice = False

        elif playerchoice == 3:

            if note_obtained == True:

                print ("You've already searched the room and there is nothing left to find.\n")

            else:

                print ("You look around the room and you find a chest of drawers on the other side of the room tucked neatly in the corner, the handles shining in the pale light.\n")

                note_obtained = the_list(puzzle_answer)

        else:

            print ("Invalid Option")

    return playerchoice

 

def the_list(the_clue):

    unknown_choice = False

    while unknown_choice == False:

        playerchoice = input("Option 1: Check the drawers\n")

        if playerchoice.isdigit():

            playerchoice = int(playerchoice)       

        if playerchoice == 1:

            print ("You slowly make your way over to the drawers, hoping to find something of interest. When you get to the drawers you notice that there’s a thick layer of dust on top with patches that are far more thin, as though someone wiped the dust with there hand.")

            print ("Looking through the drawers you find that they’re empty for the most part, that is until you get to the final bottom draw, where you find a piece of paper.")
            print ("Observing the find you realise that it’s a list, a list of names.\n")

            print ("Thinking who these people could be you start coming up with theories “Could they be the names of future victims or maybe past victims?” For all you know they could be the names of other witches, like some sort of counsil.")

            print ("Keep the list?\n")

            unknown_choice = True

    unknown_choice = False

    while unknown_choice == False:

        print ("Option 1: Yes")

        playerchoice = input("Option 2: No\n")

        if playerchoice.isdigit():

            playerchoice = int(playerchoice)

        if playerchoice == 1:

            print ("Looking back down to where you found the list you find another piece of paper, this one looks more like it was ripped from a notebook.")

            print ("The paper has a number on it. Hope suddenly rises within you at the fact that this could be the keycode for the door and your first step towards escaping this hell.\n")

            if the_clue % 2 == 0:

                print ("""The paper reads "The number is even"\n""")

               

            else:

                print ("""The paper reads "The number is odd"\n""")

            unknown_choice = True

            note_taken = True

        elif playerchoice == 2:

            firstroom(the_clue)

    return note_taken

def minigame_a(answer_puzzle,progress):
    secret_number = answer_puzzle
    guess = 0
    tries = 0
    n = 9999

    print("Guess the number keypad.")
    print("There is a secret number between 1 to 100.")
    game_on = False
    while game_on == False:

        while guess != secret_number and tries < 9999:
            valid_number = False
            while valid_number == False:
                guess = input("\nPlease input your guess. ")
                if guess.isdigit() == True:
                    valid_number = True
                else:
                    print("\n Not a valid number.")

            guess = int(guess)

            if guess > secret_number and tries < n-1:
                print("That is too high.")
            elif guess < secret_number and tries < n-1:
                print("That is too low.")

            tries = tries + 1
        if guess == secret_number:
            print("\nYou guessed secret number correctly!\n")
            if progress == "none":
                progress = "number guess complete"
                update_progress(progress)
            game_on = True
        else:
            print("Keep trying")
            tries = 0
            game_on = False
    return progress
            
    
def corridor():
    
    correct_option = False
    print ("\n", "\n", "\n", "\n")
    print ("You hear a beep come from the keypad and a click at the door signifying that it is now unlocked.")
    print ("Walking through the paint chipped door way, you find yourself in a hallway. As you walk down the dark hallway you start to look around to see what else this place has in store for you.\n")
    print ("There is a slight sound of wind from down the hallway and you can make out curtains flapping from what you assume to be a broken window.")
    print ("In the darkness and with what little pale light that is protruding from the windows, you can see old paintings on the walls covered in cobwebs.\n")
    print ("""The walls themselves have most of the wallpaper torn off. “Webs... they seem to be a common thing in this place” you think to yourself. Descending further down you are met with three doors.\n""")
    while correct_option == False:
        print ("PLEASE CHOOSE ONE OF THE FOLLOWING OPTIONS:", )
        print ("Option 1: The first door")
        print ("Option 2: The second door")
        playerchoice = input("Option 3: The third door\n")
        if playerchoice.isdigit():
            playerchoice = int(playerchoice)
        if playerchoice == 1:
            print ("This door is locked\n")
            correct_option = False
        elif playerchoice == 2:
            print ("This door is also locked\n")
            correct_option = False
        elif playerchoice == 3:
            print ("You walk over to one of the doors and check to see if it’s open It is.\n")                  
            correct_option = True
        else:
            print ("Invalid Option")

    return playerchoice
# This part of the code completes the corridor section of the code.
def third_door():
    print ("\n", "\n", "\n", "\n")

    print ("You find yourself frozen in fear with your hand stuck on the handle, keeping it held down wondering what could be on the other side and how you can prepare yourself.")
    print ("Gathering up all the mental strength you possibly can, you open the door with a shaky hand. You peek your head into the room first to check for anything... Nothing.\n")
    print ("You are met with an empty room, that is apart from a candle sat there in the centre of the room. There is something comforting about it.")
    print ("Walking around a dark house for so long it is nice to see some form of light.\n")
    print ("It is on an old round table, nothing fancy. It is old and decrepit, full of cracks and the wood is chipping away much like everything else in the house.")
    print ("You notice that there is a phone on the table along with the candle. All of a sudden the phone starts to ring, startling you in the process.")
    print ("You dare not answer it. Instead you just wait it out, it stops ringing after some time and the answer machine begins to record aloud.\n")
    print ("""The message says that a cult member is on their way over to start the ritual and will be over as soon as possible, "I need to get out of here!\n" """)
    #Timer
    the_choice = False
    while the_choice == False:
        print ("PLEASE CHOOSE ONE OF THE FOLLOWING OPTIONS:", )
        print ("Option 1: Search the room")
        playerchoice = input("Option 2: Leave the room\n")
        if playerchoice.isdigit():
            playerchoice = int(playerchoice)
        if playerchoice == 1:
            print ("After calming down from the scare you decide to have a look around the room, barely lit by the candle, though far better light than what the moon has been offering.")
            print ("You notice a slight stench. It smells like someone just left out a dinner to rot, the smell filling the room.")
            print ("As you peer into the corner of the room you see a desk, you make your way over to it.\n")
            
            the_choice = True
        elif playerchoice == 2:
            print ("You leave the room")
            corridor()
        else:
            print ("Invalid Option")
    return playerchoice
# This section completes the Third door function with many print statements and options

def hangman_game(completed_hangman, progress):
    print("WELCOME TO HANGMAN")
    print("YOU HAVE GOT 8 ATTEMPTS TO GUESS THE WORD")
    letters = ""
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    prompt = ("\n1 = Name of Animals"
              "\n2 = Name of Games"
              "\n3 = Name of Fruits"
              "\n4 = Name of Movie"
              "\n5 = Name of Birds"
              "\n6 = Name of Flowers"
              "\n7 = Name of Country"
              "\n8 = Random word\n")
    hangman = True
    while hangman == True: 
        turns = 10
        guessed = ' '
        word = print("\nPlease enter your choice:")
        valid_choice = False
        while valid_choice == False:
            choice= input(prompt)
               
            if choice == "1":
                print("\nGuess the  name of Animals")
                word = random.choice(["tiger", "lion", "deer", "bear", "dog", "cat", "pig", "horse", "goat", "sheep", "squirrel", "gorilla", "monkey", "camel", "giraffe", "hippo", "rhino", "zebra", "panda", "frog",
                                      "crocodile", "whale", "alligator","dolphin", "octopus", "jellyfish", "mouse", "fox", "buffalo", "cow", "rat", "rabbit" ])
                valid_choice = True
            elif choice == "2":
                print("\nGuess the name of Games")
                word = random.choice(["pacman", "super mario", "clash of clans", "donkey kong", "tomb raider", "street fighter", "candy crush", "call of duty", "street of rage", "pong", "god of war", "mortal kombat",
                                      "grand theft auto", "resident evil","guitar hero", "dragon age", "the witcher", "tetris", "fallout", "mass effect", "space invaders", "sim city", "rock band", "duck hunt","silent hill",
                                      "paperboy", "journey", "pokemon"])
                valid_choice = True
            elif choice == "3":
                print("\nGuess the name of Fruits")
                word = random.choice(["apple", "orange", "mango", "guava", "pear", "apricot", "banana", "avocado", "blackberry",  "peach","blueberry", "grape", "coconut", "pomegranate", "kiwi", "lemon", "watermelon",
                                      "plum", "raisins","pineapple", "strawberry" ])
                valid_choice = True
            elif choice == "4":
                print("\nGuess the name of Movies")
                word = random.choice(["home alone", "die hard", "lucy", "titanic", "the wizard of oz", "terminator", "the lion king", "the godfather", "the jesus film",
                                      "jurassic park", "raiders of the lost ark","harry potter", "the shawshank redemption", "schindlers list", "the dark knight", "fight club", "pulp fiction", "forrest gump",
                                      "transformers", "back to the future", "citizen kane", "psycho", "city of god", "the matrix", "braveheart", "gladiator", "the avengers", "the ten commandments", "scarface" ])
                valid_choice = True

            elif choice == "5":
                print("\nGuess the name of Birds")
                word = random.choice([ "crow", "pigeon", "peacock", "eagle","vulture", "chicken", "duck", "turkey", "swan", "ostrich", "woodpecker", "peacock", "dove", "magpie", "flamingo", "penguin", "sparrow", "toucan", 
                                       "parrot", "hummingbird", "owl" ])
                valid_choice = True                    
                                     
            elif choice == "6":
                print("\nGuess the name of Flowers")
                word = random.choice([ "rose", "lily", "daffodils","lotus", "cactus", "daisy", "tulip", "rhododendron", "aloe vera", "orchids", "sunflower", "pansy", "hibiscus", "dahlia", "lavender", "lilac",
                                      "marigold", "snowdrops" ])
                valid_choice = True

            elif choice == "7":
                print("\nGuess the name of Countries")
                word = random.choice(["afghanistan","australia", "argentina", "bahrain", "bangladesh", "belgium", "bhutan", "brazil", "bulgaria", "canada", "china", "colombia", "congo", "cyprus", "denmark", "egypt", 
                                      "finland", "france", "germany", "greece", "hong kong", "hungary", "iceland", "india", "ireland", "island", "iraq", "iran", "israel", "italy", "japan", "kenya", "korea", "kuwait",
                                      "latvia", "libya", "malaysia", "maldives", "mexico", "nepal", "netherlands", "new zealand", "nigeria", "norway", "oman", "pakistan", "peru", "philippines", "poland", "portugal",
                                      "qatar", "saudi arabia", "spain", "sri lanka", "sweden", "switzerland", "syria", "thailand", "united kingdom", "ukraine", "vietnam", "zimbabwe" ])
                valid_choice = True
            

            elif choice == "8":
                print("\nGuess the random word")
                word = random.choice(["tiger", "lion", "deer", "bear", "dog", "cat", "pig", "horse", "goat", "sheep", "squirrel", "gorilla", "monkey", "camel", "giraffe", "hippo", "rhino", "zebra", "panda", "frog",
                                      "crocodile", "whale", "alligator","dolphin", "octopus", "jellyfish", "mouse", "fox", "buffalo", "cow", "rat", "rabbit","pacman", "super mario", "clash of clans", "donkey kong",
                                      "tom raider", "street fighter", "candy crush", "call of duty", "street of rage", "pong", "god of war", "mortal kombat","grand theft auto", "resident evil","guitar hero", "dragon age",
                                      "the witcher", "tetris","fallout", "mass effect", "space invadors", "sim city", "rock band", "duck hunt", "silent hill", "paperboy", "journey", "pokemon","apple", "orange", "mango",
                                      "guava", "pear", "apricot", "banana", "avocado", "blackberry","blueberry", "grape", "coconut", "pomegranate", "kiwi", "lemon", "watermelon","plum", "raisins","pineapple", "strawberry",
                                      "horror story", "love story", "hate story", "home alone", "die hard", "lucy", "titanic", "the wizard of oz", "terminator", "the lion king", "the godfather", "the jesus film",
                                      "jurassic park", "raidors of the lost ark","harry potter", "the shawshank redemption", "schindler's list", "the dark knight", "fight club", "pulp fiction", "forest gump", "transformers",
                                      "back to future", "citizen kane", "psycho", "city of god", "the matrix", "braveheart", "gladiator", "the avengers", "the ten commandments", "scarface","crow", "pigeon", "peacock", "eagle",
                                      "vulture", "chicken", "duck", "turkey", "swan", "ostrich", "woodpeacock", "dove", "magpie", "flamingo", "penguin", "sparrow", "toucan","parrot", "humingbird", "owl", "rose", "lili",
                                      "daffodils", "lotus", "cactus", "daisy", "tulip", "rhododendron", "aloevera", "orchids", "sunflower", "pansy", "hibicus", "dahlia", "lavender", "lilac", "marigold", "snowdrops", "afghanistan",
                                      "australia", "argentina", "bahrain", "bangladesh", "belgium", "bhutan", "brazil", "bulgaria", "canada", "china", "colombia", "congo", "cyprus", "denmark", "egypt","finland", "france",
                                      "germany", "greece", "hong kong", "hungary", "iceland", "india", "ireland", "island", "iraq", "iran", "israel", "italy", "japan", "kenya", "korea", "kuwait","latvia", "libya","malaysia",
                                      "maldives", "mexico", "nepal", "netherlands", "new zealand", "nigeria", "norway", "oman", "pakistan", "peru", "philippines", "poland", "portugal","qatar", "saudi arabia", "spain", "sri lanka",
                                      "sweden", "switzerland", "syria", "thailand", "united kingdon", "ukraine", "vietnam", "zimbabwe" ])

                valid_choice = True

            else:
                print("\nOnly the list from above is valid")

       


        while int(choice) > 0 and completed_hangman == False:
            msg = ""
            missed = 0
            for letter in word:
                if letter in guessed:
                    msg = msg + letter
                else:
                    msg = msg + "*" 
                    missed += 1

            if msg == word:
                print(msg)
                print("YOU ARE CORRECT, THE WORD WAS: ", word)
                if progress == "number guess complete":
                    progress = "hangman complete"
                    update_progress(progress)                
                completed_hangman = True
                hangman = False
            else:
                print ("\nGUESS THE WORD:", msg)
            if completed_hangman != True:
                guess = input()


            
            

            if guess == "":
                if completed_hangman != True:
                    print("\nENTER A VALID LETTER: ")
            elif guess in validLetters:
                guessed = guessed + guess
                if guess not in letters:
                    if len(letters) < 1:
                        letters = letters + guess
                    else:
                        letters = letters + "," + guess
            else:
                if completed_hangman != True:
                    print("\nENTER A VALID LETTER: ")
            
               


            if guess not in word:
                turns = turns - 1
                if turns == 9:
                    print("The letter is not in the word, please try again!")
                    print("                                       |---¬")
                    print("                                       |   O")
                    print("                                       |    ")
                    print("                                       |    ")
                    print("                                      /_\   ")
                    print("You have already guessed", letters) 
                    
                elif turns == 8:
                    print("                                       |---¬")
                    print("                                       |   O")
                    print("                                       |   |")
                    print("                                       |    ")
                    print("                                      /_\   ")
                    print("You have already guessed", letters) 
                   
                elif turns == 7:
                    print("                                       |---¬")
                    print("                                       |   O")
                    print("                                       |   |")
                    print("                                       |  / ")
                    print("                                      /_\   ")
                    print("You have already guessed", letters) 
                    
                elif turns == 6:
                    print("                                       |---¬")
                    print("                                       |   O")
                    print("                                       |   |")
                    print("                                       |  / \ ")
                    print("                                      /_\   ")
                    print("You have already guessed", letters) 
                    
                elif turns == 5:
                    print("                                       |---¬")
                    print("                                       |   O")
                    print("                                       |   |")
                    print("                                       | _/ \ ")
                    print("                                      /_\   ")
                    print("You have already guessed", letters) 
                    
                elif turns == 4:
                    print("                                       |---¬")
                    print("                                       |   O")
                    print("                                       |   |")
                    print("                                       | _/ \_ ")
                    print("                                      /_\   ")
                    print("You have already guessed", letters) 
                    
                elif turns == 3:
                    print("                                       |---¬")
                    print("                                       |   O")
                    print("                                       |  -|")
                    print("                                       | _/ \_ ")
                    print("                                      /_\   ")
                    print("You have already guessed", letters) 
                      
                elif turns == 2:
                    print("                                       |---¬")
                    print("                                       |   O")
                    print("                                       |  -|- ")
                    print("                                       | _/ \_ ")
                    print("                                      /_\   ")
                    print("You have already guessed", letters)                    
                    
                elif turns == 1:
                    print("YOU HAVE FAILED TO GUESS THE WORD:",word)
                    print("TRY AGAIN")
                    letters = ""
                    break


    return completed_hangman, progress



def desk(game_progress):
    print ("As you approach the other side of the desk there is a drawer.")
    option_choice = False
    while option_choice == False:
        playerchoice = input("Option 1: Check the desk\n")
        if playerchoice.isdigit():
            playerchoice = int(playerchoice)
        if playerchoice == 1:
            print ("When you get to the desk you see that it doesn’t have any handles. You notice it is slightly open, enough for to force your fingers in and open it.")
            print ("As you expected... cobwebs, lots of them. You see a box buried within the webs. You pull it out and see that is has a picture of a key on it.\n")
            hangman_completed = False
            while hangman_completed == False:
                hangman_completed, game_progress = hangman_game(hangman_completed, game_progress)
            print ("\nThe chest opens, revealing a key. Thinking, or at least hoping, that it opens the other two doors and that you can finally leave this place.\n")
            option_choice = True
        else:
            print ("Invalid Option")
    #option_choice = False
    #while option_choice == False:
        #print ("You use the stool and now your able to reach the key\n")
        #playerchoice = input("Option 1: Pick up key\n")
        #if playerchoice.isdigit():
            #playerchoice = int(playerchoice)
        #if playerchoice == 1:
            #print ("You have picked up the key")
            #option_choice = True
        #else:
            #print ("Invalid Option")
    return playerchoice
# This is a desk option as would make it more complicated to place it int the third room function

def leave():
    leave_choice = False
    while leave_choice == False:
        print ("Do you want to leave the room?\n")
        print ("1.Yes")
        playerchoice = input("2.No\n")
        if playerchoice.isdigit():
            playerchoice = int(playerchoice)
        if playerchoice == 1:
            #Corridor_part2
            leave_choice = True
        elif playerchoice == 2:
            leave_choice = False
    else:
        print ("Invalid Option")

    return playerchoice
# Also had to make a seperate function for the leave the room as wanted to make a multple options 

def corridor_part2():
    print ("\n", "\n", "\n", "\n")
    print ("You are back in the corridor and you have the key.")
    print ("""Maybe you should try one of the other doors with the key?\n""")
    progression = False
    while progression == False:
        print ("Option 1: First door")
        print ("Option 2: Second Door")
        playerchoice = input("Option 3: Third door\n")
        if playerchoice.isdigit():
            playerchoice = int(playerchoice)
        if playerchoice == 1:
               print ("You attempt to open the first door with the key...")
               print ("But the key doesnt seem to fit, maybe try another door.\n")
               progression = False
        elif playerchoice == 2:
               print ("The key fits, you unlock the door and slowly creep in.")
               progression = True
        elif playerchoice == 3:
               print ("You have already been in this room, there's no point going back in.")
               progression = False
        else:
            print ("Invalid Option")
# With having already a corridor made, to continue with the story have had to make a new corridor with different print statements
    return playerchoice
           
def second_door():
    print ("\n", "\n", "\n", "\n")
    print ("Wasting no time, you don’t even think about preparing yourself and, full of excitement that you might finally leave, you open the door and walk in.")
    print ("Again, nothing. However this time it’s pitch black and oddly very cold.\n")
    print ("You get about three steps into the room when you hear the door slam behind you, making you jump out of your skin.")
    print ("Stood there, paralyzed in fear, not knowing what to do, the only thing that is audible is your own breathing. At that point you hear a scuffle, like clothes rubbing together.\n")
    print ("You halt your breathing to listen out and realise in horror that you can hear someone, or something else, breathing from across the room.")
    print ("Panic sets in and you turn around, rapidly trying to open the door... but it won't budge!")
    print ("Now you can hear floorboards behind you creaking... whatever is in that room with you is slowly making its way towards you as yo slam on the door, trying to get it open!\n")
    
    choose = False
    useoftools = 0
    while choose == False:
        playerchoice = input("Option 1: Search the room\n")
        if playerchoice.isdigit():
            playerchoice = int(playerchoice)
        if playerchoice == 1:
            print ("Searching around the room you see a key hanging from a hook high on the wall")
            print ("You cant reach it as you're too small. You see a small stool which might be enough to let you reach the key.\n")
            choose = True
        else:
            print("Invalid choice")
    choose = False
    while choose == False:
        useoftools = input("Option 2: Use the stool\n")
        if useoftools.isdigit():
            useoftools = int(useoftools)
        if useoftools == 2:
            choose = True
        else:
            print("Invalid choice")

    print ("You use the stool to reach the key and you place the key in your pocket.\n")

        

# This is door number 2 where you will need to search for a key and using options            
        
    return playerchoice, useoftools

def corridor_part3():
    print ("\n", "\n", "\n", "\n")
    print ("You rush out back into the hallway, slamming the door shut behind you. Sitting there on the floor, you have never felt so relieved in your life. You pick yourself up, determined to escape.")
    print ("This key must open the last door...\n")
    print ("You need to get out before the time runs out!")
    final_choice = False
    while final_choice == False:
        print ("Option 1: First door")
        print ("Option 2: Second door")
        playerchoice = input("Option 3: Third door\n")
        if playerchoice.isdigit():
            playerchoice = int(playerchoice)
        if playerchoice == 1:
            final_choice = True
        elif playerchoice == 2:
            print ("No need to go back in that door, its a dead end.\n")
            final_choice = False
        elif playerchoice == 3:
            print ("You've already been through this door, there's nothing else to do there.\n")
            final_choice = False
        else:
            print ("Invalid Option")
    return playerchoice
# This section is corridor part3 where there is different options compared to corridor 1,2

def first_door():
    print ("\n", "\n", "\n", "\n")
    print ("You make your way over to the other door and open it. You see a staircase leading down into an abyss.")
    print ("Making your way down, the stairs creak loudly each step of the way, the walls bare and cold.\n")
    print ("The stairs themselves, also bare, just look like layers of wooden rectangles going up diagonally, no banister or anything to hold onto, just walls on each side.")
    print ("You reach the bottom of the stairs,  ending up in another room. It’s darker than usual, but as you look around you can see ornaments.")
    print ("Not surprisingly, and much like everything else in this place, they look old and dirty.\n")
    print ("You can see and old, dusty mirror on the wall. As far as you can tell you’re in the bottom hallway.")
    print
    print ("Suddenly you remember that the witches will be back soon. With that, a sense of urgency strikes you, however you know that if you’re in the main hallway that the exit should be close.\n")
    print ("You turn around, gazing into the distance you can see a pale outline of a rectangle shape. You realise that it’s the light shining through the door.")
    print ("""You make haste and run towards the door. You try to open the door… locked. “Of course it’s locked!” you say out loud.\n""")
    print ("You see that there is another keypad nested into it on the right side on the wall, near the handle.")
    print ("It looks different to the others. This one seems to have shapes instead of numbers. You touch the one of the shapes... nothing.")
    print
    print ("You see that each shape is on a disc that rotates vertically, much like a combination padlock.\n")
    print ("After trying to turn the discs, they don’t seem to move. As you are trying to figure out what you need to do to get it to work you notice a hole on the right side of the keypad.")
    print ("From the looks of it you need to insert an object that is spherical in shape and the size of a large bouncy ball.")
    print ("With your freedom being in reach at this point, you gather the courage to move on.\n")
    print ("You turn around and peer down the pitch black hallway and notice a door on the left side, assuming that it’s the door to the living room.")
    print ("There is also another doorway further down towards the other end of the hallway, you assume that this is the door to the kitchen")

def door_one():
    darkend_choice = False
    while darkend_choice == False:
        print ("Option 1: First door")
        playerchoice = input("Option 2: Second door\n")
        if playerchoice.isdigit():
            playerchoice = int(playerchoice)
        if playerchoice == 1:
            print ("You walk over to the first door on your right in anticipation, you know that the witches are out. With the thought of having the same experience as the room upstairs, you’re more cautious this time round.")
            print ("With one hand on the handle you turn it and open the door. To your surprise, you see light. Not just some small meek candle, but a burning fireplace that lights up the room.")
            print ("You move towards the fireplace, grateful that there’s some warmth since the closest you’ve came to comfort was the candle.\n")
            print ("Looking above the fireplace, on the mantelpiece you see a rather large ornament in the center, with smaller ornaments on both sides.")
            print("Going to both edges of the mantelpiece, the large one in the centre took the form of a symbol, not one that you’re familiar with, nor is it one that seems to be particularly friendly or pleasing to the eye.")
            print ("There is nothing of use on here so you look around the room a bit more.")
            print ("You see the window boarded up completely with no light coming through at all and a large cabinet in the corner of the room, to the right of the window.")
            darkend_choice = True
        elif playerchoice == 2:
            print ("""A strange aura around you screams not to go in. You think to yourself "I deffinatly need to check the first door!" \n""")
            darkend_choice = False
    return playerchoice

def doorone_part2():
    print ("\n", "\n", "\n", "\n")
    print ("You walk over to the cabinet and, looking through the glass pattern, you see more trinkets. Some do have a menacing look and others are just more ornaments and symbols.")
    print ("Glancing down you notice that there are two drawers under the display. You open one of the drawers and see a wooden box with a diamond shape that has a circle within it.")
    print ("You open up that box and see a small orb like object.  You take it, thinking that this may be what you need to leave the house.\n")
    smart_choice = False
    while smart_choice == False:
        print ("Option 1: Back to the hallway")
        playerchoice = input("Option 2: Back to the fireplace\n")
        if playerchoice.isdigit():
            playerchoice = int(playerchoice)
        if playerchoice == 1:
            print ("You exit the room back into the dark hallway, the area just outside the door gently lit up by the fire. You stand just outside the living room. ")
            smart_choice = True
        elif playerchoice == 2:
            print ("You move back to the fireplace still happy with the fact you have some warmth.\n")
            smart_choice = False
    return playerchoice

def hallway_part2():
    calling_choice = False
    while calling_choice == False:
        print ("Option 1: Try the orb")
        playerchoice = input("Option 2: Walk down the hallway\n")
        if playerchoice.isdigit():
            playerchoice = int(playerchoice)
        if playerchoice == 1:
            print ("You walk over to the door and place the orb into the small hole on the side of the door and wait… nothing happens.")
            print ("Confused and annoyed you try everything you can think of to get it to work. Eventually the orb falls out. Exhausted and losing hope you carry on through the nightmare.\n")
            calling_choice = False
        elif playerchoice == 2:
            print ("You decide to walk down to the other door towards the end of the hallway.")
            calling_choice = True
    return playerchoice

def doortwo():
    print ("\n", "\n", "\n", "\n")
    print ("As you walk further down the hallway getting closer to the second door that you assume is the kitchen, you notice a putrid smell coming from the door.")
    print ("Again you open the door slowly to a dimly lit room. The windows are not boarded up this time however, which allows the dim moonlight to shine through.")
    print ("Immediately you see where the smell is coming from, a sink full of some sort of thick black mass. You're not sure whether it’s old cutlery, pots, pans or even rotting food or flesh for all you know!\n")
    print ("From the looks of the place this room is hardly ever used. A lot of the cupboards have their doors ripped off and drawers missing.")
    print
    print ("You see a cupboard hung on the wall, directly to your right as you walk into the room.")
    print ("It seems to be a little high up for you to reach so you have to climb on the counter to reach it, as you do you notice that the top feels sticky with who knows what.")
    print ("You stand up and open the cupboard. You see a lot of old papers that have some sort of foreign writing on them.\n")
    print ("It looks to be in spanish as far as you can tell, although it’s probably something rather different.")
    print ("Behind the piles of paper you find another box that looks like the one you found in the living room. You open it to reveal another orb. You feel both relieved and at the same time hopeless as it may not work either.")
    print ("You jump down from the counter.")
    kitchenterror = False
    while kitchenterror == False:
        print ("Option 1: Back to the hallway")
        playerchoice = input("Option 2: Look further\n")
        if playerchoice.isdigit():
            playerchoice = int(playerchoice)
        if playerchoice == 1:
            print ("You go to leave the kitchen and realise that the door is shut for some reason. Thinking you must have closed it without realising, you go to open it… it’s locked!")
            print ("""“Strange” you think to yourself, but what do you expect in this this place after all. Feeling frustrated, you calm yourself down and try and look for another way out.\n""")
            kitchenterror = False
        elif playerchoice == 2:
            print ("Looking around the room you see a large box on the table. You have a look inside and see its full of some strange looking cups and what look like rolled up mats.")
            print ("""Looking deeper in the box you find a large sharp object with a strange pattern on it, something to do with rituals you assume.""")
            print ("You don't find anything useful in the box.\n")
            print
            print ("You leave the box and see a drawer in the corner of the room to the far left, opposite of the door. You open the drawer and see a key tucked away in the corner, you pick it up.")
            print ("You try the key on the door… It works! You leave the room and close the door behind you.")
            print ("you look to your left and see another door. This one’s different however... it looks to be made out of metal rather than a normal wooden door.\n")
            kitchenterror = True

    return playerchoice

def orbs():
    orbuse = False
    while orbuse == False:
        print ("Option 1:Use the new orb on exit")
        playerchoice = input("Option 2: Go to the door\n")
        if playerchoice.isdigit():
            playerchoice = int(playerchoice)
        if playerchoice == 1:
            print ("More focused on leaving the house you decide to try the orb on the door. You make your way to the door and try the orb.")
            print ("You try it and… again nothing. Frustrated, you come to the conclusion that you will now have to try the other door.\n")
            orbuse = False
        elif playerchoice == 2:
            print ("\n")
            print ("Curiosity getting the better of you, you decide to go to the new found door.")
            print ("When you reach the door you see a padlock on it. You lift it up then drop it... it swings and bangs loudly on the door.")
            print ("You hear some kind of scream coming from the other side! You put your ear on the door to try and listen you hear it getting louder and louder!")
            print ("You then start to hear a thumping sound accompanying the murmurs!\n")
            print ("All of a sudden, there is a loud bang at the door! You fall back holding your ear.")
            print
            print ("Once you gather your bearings and can hear again, the room is filled with loud bangs coming from the door.")
            print ("You sit there, staring at it for what seems like forever.")
            print ("Then it just stops out of nowhere... You calm down and try to pick yourself up.")
            print ("You pull yourself up, using an object that is to your right, not realising that is not fixed into the ground.")
            print ("You pull it down as you stumble to your feet.\n")
            print ("You see a shiny ball that rolled out of the object. You pick it up… another orb, you hope that this one will work!")
            print ("You run straight for the door, excited that this may be your ticket out of here!\n")
            print ("You place the orb into the hole on the keypad and touch the shapes. You see another row of shapes materialise above and then disappear.")
            print ("You realise you need to memorise the combination.\n")
            orbuse = True
    return playerchoice

def start_puzzle():
    puzzle_start = False
    while puzzle_start == False:
        playerchoice = input("Option 1: Start Puzzle\n")
        if playerchoice.isdigit():
            playerchoice = int(playerchoice)
        if playerchoice == 1:
            puzzle_start = True
        else:
            puzzle_start = False
    return playerchoice

# gets difficulty
def define_difficulty(difficulty):
    difficulty_file = open("difficulty.txt", "w")
    difficulty_file.write(difficulty)
    difficulty_file.close()

# gets game type - main game or mini game
def define_game_type(game_type):
    game_type_file = open("game_type.txt", "w")
    game_type_file.write(game_type)
    game_type_file.close()

# gets players previous progress
def get_progress():
    progress_file = open("progress.txt", "r")
    progress = progress_file.read()
    progress_file.close()
    return progress

#updates player's current progress
def update_progress(mini_game):
    progress_file = open("progress.txt", "w")   
    progress_file.write(mini_game)
    progress_file.close()

def check_current_progress():
    current_progress_file = open("current_progress.txt", "r")
    current_progress = current_progress_file.read()
    current_progress_file.close()
    return current_progress

def update_current_progress(mini_game):
    current_progress_file = open("current_progress.txt", "w")   
    current_progress_file.write(mini_game)
    current_progress_file.close()   
        
#Main Game
define_difficulty("medium")
define_game_type("main game")
previous_progress = get_progress()
highest_number = 100
answer_puzzle = random.randint(1,highest_number)
intro()
firstroom(answer_puzzle)
previous_progress = minigame_a(answer_puzzle,previous_progress)
corridor()
third_door()
desk(previous_progress)
previous_progress = get_progress()
leave()
corridor_part2()
second_door()
corridor_part3()
first_door()
door_one()
hallway_part2()
doortwo()
orbs()
start_puzzle()
update_current_progress("none")
print ("\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n")
os.system('test_your_memory.py')
current_progress = check_current_progress()
if current_progress == "memory game complete":
    os.system('escape.py')
