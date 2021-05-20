# Main Menu
# Chris Burrell
# 06/03/2018

import random
import time
import tkinter
from tkinter import *
import os

def adventure_game():
    window.withdraw()
    os.system('witch_way_out.py')
    window.deiconify()

def number_difficulty_screen():
    canvas.delete(ALL)
    background = canvas.create_image(canvas_width/2,canvas_height/2, image = background_shape)
    easy_button = Button(canvas, height = 95, width = 215, image = easy_photo, borderwidth = 0, highlightthickness = 0, command = easy_number)
    easy_window = canvas.create_window(500,150, window = easy_button)
    medium_button = Button(canvas, height = 95, width = 215, image = medium_photo, borderwidth = 0, highlightthickness = 0, command = medium_number)
    medium_window = canvas.create_window(500,250, window = medium_button)
    hard_button = Button(canvas, height = 95, width = 215, image = hard_photo, borderwidth = 0, highlightthickness = 0, command = hard_number)
    hard_window = canvas.create_window(500,350, window = hard_button)
    back_button = Button(canvas, height = 95, width = 215, image = back_photo, borderwidth = 0, highlightthickness = 0, command = mini_games)
    back_window = canvas.create_window(500,450, window = back_button)

def memory_difficulty_screen():
    canvas.delete(ALL)
    background = canvas.create_image(canvas_width/2,canvas_height/2, image = background_shape)
    easy_button = Button(canvas, height = 95, width = 215, image = easy_photo, borderwidth = 0, highlightthickness = 0, command = easy_memory)
    easy_window = canvas.create_window(500,150, window = easy_button)
    medium_button = Button(canvas, height = 95, width = 215, image = medium_photo, borderwidth = 0, highlightthickness = 0, command = medium_memory)
    medium_window = canvas.create_window(500,250, window = medium_button)
    hard_button = Button(canvas, height = 95, width = 215, image = hard_photo, borderwidth = 0, highlightthickness = 0, command = hard_memory)
    hard_window = canvas.create_window(500,350, window = hard_button)
    back_button = Button(canvas, height = 95, width = 215, image = back_photo, borderwidth = 0, highlightthickness = 0, command = mini_games)
    back_window = canvas.create_window(500,450, window = back_button)

def escape_difficulty_screen():
    canvas.delete(ALL)
    background = canvas.create_image(canvas_width/2,canvas_height/2, image = background_shape)
    easy_button = Button(canvas, height = 95, width = 215, image = easy_photo, borderwidth = 0, highlightthickness = 0, command = easy_escape)
    easy_window = canvas.create_window(500,150, window = easy_button)
    medium_button = Button(canvas, height = 95, width = 215, image = medium_photo, borderwidth = 0, highlightthickness = 0, command = medium_escape)
    medium_window = canvas.create_window(500,250, window = medium_button)
    hard_button = Button(canvas, height = 95, width = 215, image = hard_photo, borderwidth = 0, highlightthickness = 0, command = hard_escape)
    hard_window = canvas.create_window(500,350, window = hard_button)
    back_button = Button(canvas, height = 95, width = 215, image = back_photo, borderwidth = 0, highlightthickness = 0, command = mini_games)
    back_window = canvas.create_window(500,450, window = back_button)

def mini_games():
    game_progress = get_progress()
    define_game_type("mini game")
    canvas.delete(ALL)
    background = canvas.create_image(canvas_width/2,canvas_height/2, image = background_shape)
    # guess the number button
    if game_progress == "none":
        guess_number_button = Button(canvas, height = 133, width = 215, image = locked_game_photo, borderwidth = 0, highlightthickness = 0, command = locked_game)
        guess_number_window = canvas.create_window(375,175, window = guess_number_button)
    else:
        guess_number_button = Button(canvas, height = 133, width = 215, image = guess_number_photo, borderwidth = 0, highlightthickness = 0, command = number_difficulty_screen)
        guess_number_window = canvas.create_window(375,175, window = guess_number_button)
    # hangman button    
    if game_progress == "none" or game_progress == "number guess complete":
        hangman_button = Button(canvas, height = 133, width = 215, image = locked_game_photo, borderwidth = 0, highlightthickness = 0, command = locked_game)
        hangman_window = canvas.create_window(625,175, window = hangman_button)        
    else:
        hangman_button = Button(canvas, height = 133, width = 215, image = hangman_photo, borderwidth = 0, highlightthickness = 0, command = hangman)
        hangman_window = canvas.create_window(625,175, window = hangman_button)
    # memory game button
    if game_progress == "none" or game_progress == "number guess complete" or game_progress == "hangman complete":    
        memory_test_button = Button(canvas, height = 133, width = 215, image = locked_game_photo, borderwidth = 0, highlightthickness = 0, command = locked_game)
        memory_test_window = canvas.create_window(375,325, window = memory_test_button)
    else:
        memory_test_button = Button(canvas, height = 133, width = 215, image = memory_test_photo, borderwidth = 0, highlightthickness = 0, command = memory_difficulty_screen)
        memory_test_window = canvas.create_window(375,325, window = memory_test_button)
    # running game button
    if game_progress == "all":
        escape_button = Button(canvas, height = 133, width = 215, image = escape_photo, borderwidth = 0, highlightthickness = 0, command = escape_difficulty_screen)
        escape_window = canvas.create_window(625,325, window = escape_button)
    else:
        escape_button = Button(canvas, height = 133, width = 215, image = locked_game_photo, borderwidth = 0, highlightthickness = 0, command = locked_game)
        escape_window = canvas.create_window(625,325, window = escape_button)
# main menu button
    main_menu_button = Button(canvas, height = 72, width = 328, image = main_menu_photo, borderwidth = 0, highlightthickness = 0, command = main_menu)
    main_menu_window = canvas.create_window(500,460, window = main_menu_button)

def locked_game():
    ()

def define_difficulty(difficulty):
    difficulty_file = open("difficulty.txt", "w")
    difficulty_file.write(difficulty)
    difficulty_file.close() 

def easy_number():
    define_difficulty("easy")
    launch_number_game()
    
def medium_number():
    define_difficulty("medium")
    launch_number_game()
    
def hard_number():
    define_difficulty("hard")
    launch_number_game()

def launch_number_game():
    window.withdraw()
    os.system('guess_the_number.py')
    window.deiconify()
    mini_games()

def hangman():
    window.withdraw()
    os.system('hangman.py')  
    window.deiconify()
    mini_games()
    
def easy_memory():
    define_difficulty("easy")
    launch_memory_game()

def medium_memory():
    define_difficulty("medium")
    launch_memory_game()

def hard_memory():
    define_difficulty("hard")
    launch_memory_game()

def launch_memory_game():
    window.withdraw()
    os.system('test_your_memory.py')
    window.deiconify()
    mini_games()

def easy_escape():
    define_difficulty("easy")
    launch_escape()

def medium_escape():
    define_difficulty("medium")
    launch_escape()

def hard_escape():
    define_difficulty("hard")
    launch_escape()

def launch_escape():
    window.withdraw()
    os.system('escape.py')
    window.deiconify()
    mini_games()

def quit_game():
    canvas.delete(ALL)        
    window.destroy()

def main_menu():
    canvas.delete(ALL)
    background = canvas.create_image(canvas_width/2,canvas_height/2, image = background_shape)    
    start_game_button = Button(canvas, height = 77, width = 410, image = start_game_photo, borderwidth = 0, highlightthickness = 0, command = adventure_game)
    start_game_window = canvas.create_window(500,200, window = start_game_button)
    mini_games_button = Button(canvas, height = 77, width = 410, image = mini_games_photo, borderwidth = 0, highlightthickness = 0, command = mini_games)
    mini_games_window = canvas.create_window(500,300, window = mini_games_button)
    quit_button = Button(canvas, height = 77, width = 410, image = quit_photo, borderwidth = 0, highlightthickness = 0,  command = quit_game)
    quit_window = canvas.create_window(500,400, window = quit_button)

def define_game_type(game_type):
    game_type_file = open("game_type.txt", "w")
    game_type_file.write(game_type)
    game_type_file.close()

def get_progress():
    progress_file = open("progress.txt", "r")
    progress = progress_file.read()
    progress_file.close()
    return progress

# string to clear the interpreter screen
clear_screen = "\n" * 50

# initialise variables
canvas_width = 1000
canvas_height = 600

# initialise window
window = Tk()
window.title("Main Menu")
canvas = Canvas(window, width = canvas_width, height = canvas_height)
canvas.pack()

# create background
background_shape = PhotoImage(file = 'background.png')
background = canvas.create_image(canvas_width/2,canvas_height/2, image = background_shape)

# import images
start_game_photo = PhotoImage(file = 'start_game.png')
mini_games_photo = PhotoImage(file = 'mini_games.png')
quit_photo = PhotoImage(file = 'quit.png')
guess_number_photo = PhotoImage(file = 'guess_the_number.png')
hangman_photo = PhotoImage(file = 'hangman.png')
memory_test_photo = PhotoImage(file = 'memory_test.png')
escape_photo = PhotoImage(file = 'escape.png')
main_menu_photo = PhotoImage(file = 'main_menu.png')
easy_photo = PhotoImage(file = 'easy.png')
medium_photo = PhotoImage(file = 'medium.png')
hard_photo = PhotoImage(file = 'hard.png')
back_photo = PhotoImage(file = 'back.png')
locked_game_photo = PhotoImage(file = 'locked_game.png')

#main
main_menu()
window.mainloop()



