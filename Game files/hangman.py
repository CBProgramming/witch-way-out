import random
import time

print ("\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n")
completed_hangman = False
print("WELCOME TO HANGMAN")
print("YOU HAVE GOT 8 ATTEMPTS TO GUESS THE WORD")    



letters = ""
validLetters = 'abcdefghijklmnopqrstuvwxyz'
prompt = ("\n1 = Name of Animals"
          "\n2 = Name of Video Games"
          "\n3 = Name of Fruits"
          "\n4 = Name of Movie"
          "\n5 = Name of Birds"
          "\n6 = Name of Flowers"
          "\n7 = Name of Country"
          "\n8 = Random word\n")


turns = 9
guessed = ' '
word = print("\nPlease enter your choice:")
valid_choice = False
while valid_choice == False:
    choice= input(prompt)
       
    if choice == "1":
        print("\nGuess the  name of the animal")
        word = random.choice(["tiger", "lion", "deer", "bear", "dog", "cat", "pig", "horse", "goat", "sheep", "squirrel", "gorilla", "monkey", "camel", "giraffe", "hippo", "rhino", "zebra", "panda", "frog",
                              "crocodile", "whale", "alligator","dolphin", "octopus", "jellyfish", "mouse", "fox", "buffalo", "cow", "rat", "rabbit" ])
        valid_choice = True
    elif choice == "2":
        print("\nGuess the name of the video game")
        word = random.choice(["pacman", "super mario", "clash of clans", "donkey kong", "tomb raider", "street fighter", "candy crush", "call of duty", "street of rage", "pong", "god of war", "mortal kombat",
                              "grand theft auto", "resident evil","guitar hero", "dragon age", "the witcher", "tetris", "fallout", "mass effect", "space invaders", "sim city", "rock band", "duck hunt","silent hill",
                              "paperboy", "journey", "pokemon"])
        valid_choice = True
    elif choice == "3":
        print("\nGuess the name of the fruit")
        word = random.choice(["apple", "orange", "mango", "guava", "pear", "apricot", "banana", "avocado", "blackberry",  "peach","blueberry", "grape", "coconut", "pomegranate", "kiwi", "lemon", "watermelon",
                              "plum", "raisins","pineapple", "strawberry" ])
        valid_choice = True
    elif choice == "4":
        print("\nGuess the name of the movie")
        word = random.choice(["home alone", "die hard", "lucy", "titanic", "the wizard of oz", "terminator", "the lion king", "the godfather", "the jesus film",
                              "jurassic park", "raidors of the lost ark","harry potter", "the shawshank redemption", "schindlers list", "the dark knight", "fight club", "pulp fiction", "forrest gump",
                              "transformers", "back to future", "citizen kane", "psycho", "city of god", "the matrix", "braveheart", "gladiator", "the avengers", "the ten commandments", "scarface" ])
        valid_choice = True

    elif choice == "5":
        print("\nGuess the name of the bird")
        word = random.choice([ "crow", "pigeon", "peacock", "eagle","vulture", "chicken", "duck", "turkey", "swan", "ostrich", "woodpeacock", "dove", "magpie", "flamingo", "penguin", "sparrow", "toucan", 
                               "parrot", "humingbird", "owl" ])
        valid_choice = True                    
                             
    elif choice == "6":
        print("\nGuess the name of the flower")
        word = random.choice([ "rose", "lily", "daffodils","lotus", "cactus", "daisy", "tulip", "rhododendron", "aloe vera", "orchids", "sunflower", "pansy", "hibiscus", "dahlia", "lavender", "lilac",
                              "marigold", "snowdrops" ])
        valid_choice = True

    elif choice == "7":
        print("\nGuess the name of the country")
        word = random.choice(["afghanistan","australia", "argentina", "bahrain", "bangladesh", "belgium", "bhutan", "brazil", "bulgaria", "canada", "china", "colombia", "congo", "cyprus", "denmark", "egypt", 
                              "finland", "france", "germany", "greece", "hong kong", "hungary", "iceland", "india", "ireland", "island", "iraq", "iran", "israel", "italy", "japan", "kenya", "korea", "kuwait",
                              "latvia", "libya", "malaysia", "maldives", "mexico", "nepal", "netherlands", "new zealand", "nigeria", "norway", "oman", "pakistan", "peru", "philippines", "poland", "portugal",
                              "qatar", "saudi arabia", "spain", "sri lanka", "sweden", "switzerland", "syria", "thailand", "united kingdom", "ukraine", "vietnam", "zimbabwe" ])
        valid_choice = True
    

    elif choice == "8":
        print("\nGuess the random word")
        word = random.choice(["tiger", "lion", "deer", "bear", "dog", "cat", "pig", "horse", "goat", "sheep", "squirrel", "gorilla", "monkey", "camel", "giraffe", "hippo", "rhino", "zebra", "panda", "frog",
                              "crocodile", "whale", "alligator","dolphins", "octopus", "jellyfish", "mouse", "fox", "buffalo", "cow", "rat", "rabbit","pacman", "super mario", "clash of clans", "donkey kong",
                              "tomb raider", "street fighter", "candy crush", "call of duty", "street of rage", "pong", "god of war", "mortal kombat","grand theft auto", "resident evil","guitar hero", "dragon age",
                              "the witcher", "tetris","fallout", "mass effect", "space invaders", "sim city", "rock band", "duck hunt", "silent hill", "paperboy", "journey", "pokemon","apple", "orange", "mango",
                              "guava", "pear", "apricot", "banana", "avocado", "blackberry","blueberry", "grape", "coconut", "pomegranate", "kiwi", "lemon", "watermelon","plum", "raisins","pineapple", "strawberry",
                              "home alone", "die hard", "lucy", "titanic", "the wizard of oz", "terminator", "the lion king", "the godfather", "the jesus film",
                              "jurassic park", "raidors of the lost ark","harry potter", "the shawshank redemption", "schindlers list", "the dark knight", "fight club", "pulp fiction", "forrest gump", "transformers",
                              "back to future", "citizen kane", "psycho", "city of god", "the matrix", "braveheart", "gladiator", "the avengers", "the ten commandments", "scarface","crow", "pigeon", "peacock", "eagle",
                              "vulture", "chicken", "duck", "turkey", "swan", "ostrich", "woodpeacock", "dove", "magpie", "flamingo", "penguin", "sparrow", "toucan","parrot", "humingbird", "owl", "rose", "lily",
                              "daffodils", "lotus", "cactus", "daisy", "tulip", "rhododendron", "aloe vera", "orchids", "sunflower", "pansy", "hibiscus", "dahlia", "lavender", "lilac", "marigold", "snowdrops", "afghanistan",
                              "australia", "argentina", "bahrain", "bangladesh", "belgium", "bhutan", "brazil", "bulgaria", "canada", "china", "colombia", "congo", "cyprus", "denmark", "egypt","finland", "france",
                              "germany", "greece", "hong kong", "hungary", "iceland", "india", "ireland", "island", "iraq", "iran", "israel", "italy", "japan", "kenya", "korea", "kuwait","latvia", "libya","malaysia",
                              "maldives", "mexico", "nepal", "netherlands", "new zealand", "nigeria", "norway", "oman", "pakistan", "peru", "philippines", "poland", "portugal","qatar", "saudi arabia", "spain", "sri lanka",
                              "sweden", "switzerland", "syria", "thailand", "united kingdom", "ukraine", "vietnam", "zimbabwe" ])

        valid_choice = True

    else:
        print("\nInvalid input.  Please enter a number from the list above.")




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
        completed_hangman = True
        hangman = False
    else:
        print ("\nGUESS THE WORD:", msg)
    
    if completed_hangman != True:
        guess = input()


    
    
    actual_letter = False
    if guess == "":
        if completed_hangman != True:
            print("\nNot a valid letter")
    elif guess in validLetters:
        actual_letter = True
        guessed = guessed + guess
        if guess not in letters:
            if len(letters) < 1:
                letters = letters + guess
            else:
                letters = letters + "," + guess
    else:
        if completed_hangman != True:
            print("\nNot a valid letter")
    
       


    if guess not in word:
        turns = turns - 1
        if actual_letter == True:
            print(guess, "is not in the word")
        if turns == 8:
            print("                                       |---¬")
            print("                                       |   O")
            print("                                       |    ")
            print("                                       |    ")
            print("                                      /_\   ")
            if letters != "":       
                print("You have already guessed", letters) 
            
        elif turns == 7:
            print("                                       |---¬")
            print("                                       |   O")
            print("                                       |   |")
            print("                                       |    ")
            print("                                      /_\   ")
            if letters != "":       
                print("You have already guessed", letters) 
           
        elif turns == 6:
            print("                                       |---¬")
            print("                                       |   O")
            print("                                       |   |")
            print("                                       |  / ")
            print("                                      /_\   ")
            if letters != "":       
                print("You have already guessed", letters)  
            
        elif turns == 5:
            print("                                       |---¬")
            print("                                       |   O")
            print("                                       |   |")
            print("                                       |  / \ ")
            print("                                      /_\   ")
            if letters != "":       
                print("You have already guessed", letters)  
            
        elif turns == 4:
            print("                                       |---¬")
            print("                                       |   O")
            print("                                       |   |")
            print("                                       | _/ \ ")
            print("                                      /_\   ")
            if letters != "":       
                print("You have already guessed", letters) 
            
        elif turns == 3:
            print("                                       |---¬")
            print("                                       |   O")
            print("                                       |   |")
            print("                                       | _/ \_ ")
            print("                                      /_\   ")
            if letters != "":       
                print("You have already guessed", letters)  
            
        elif turns == 2:
            print("                                       |---¬")
            print("                                       |   O")
            print("                                       |  -|")
            print("                                       | _/ \_ ")
            print("                                      /_\   ")
            if letters != "":       
                print("You have already guessed", letters)  
              
        elif turns == 1:
            print("                                       |---¬")
            print("                                       |   O")
            print("                                       |  -|- ")
            print("                                       | _/ \_ ")
            print("                                      /_\   ")               

            print("\nYou have failed to guess the word:",word)
            print("\nBetter luck next time!")
            letters = ""
            break

time.sleep(3)
