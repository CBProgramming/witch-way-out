    # Chris Burrell
    # Memory game


import random
import time
import tkinter
from tkinter import *

def do_nothing(mouse_coords):
     ()

# identify clicked button
def get_mouse_coords(mouse_coords):
    valid_x = True
    valid_y = True
    x = mouse_coords.x
    y = mouse_coords.y
    if y > 100 and y <300:
        location = 199.00
    elif y > 300 and y < 500:
        location = 399.00
    else:
        valid_y = False
    if (x > 100 and x < 300) and (y > 100 and y < 300):
        button = (cat)
    elif (x > 300 and x < 500) and (y > 100 and y < 300):
        button = (hat)     
    elif (x > 500 and x < 700) and (y > 100 and y < 300):
        button = (broom)
    elif (x > 700 and x < 900) and (y > 100 and y < 300):
        button = (moon)
    elif (x > 100 and x < 300) and (y > 300 and y < 500):
        button = (pentagram)
    elif (x > 300 and x < 500) and (y > 300 and y < 500):
        button = (skull)
    elif (x > 500 and x < 700) and (y > 300 and y < 500):
        button = (coffin)
    elif (x > 700 and x < 900) and (y > 300 and y < 500):
        button = (bat)
    else:
        valid_x = False
    if valid_x == True and valid_y == True:
        hide_clicked_button(button, location)
        window.update()
        time.sleep(button_time)

def hide_clicked_button(button_clicked,pixel_location_check):
     if canvas.coords(button_clicked)[1] != pixel_location_check:
        canvas.itemconfig(button_clicked, state = 'hidden')
        canvas.move(button_clicked, 0 , -1)

# generate an entirely new solution each time
def create_new_solution(current_len,solution):
    solution = []
    random.shuffle(default_shapes)
    for shape in range(current_len):
        solution.append(default_shapes[random.randint(0, len(default_shapes)-1)])
    return solution

#briefly display solution to user
def display_solution(solution, shapes_deleted, answer_display_time):
    # display solution of four or less
    hide_buttons()
    canvas.itemconfig(memorise, state = 'normal')
    window.update()
    time.sleep(message_time)
    canvas.itemconfig(memorise, state = 'hidden')
    if len(solution) % 2 != 0 and len(solution) < 5:
        start_width = (canvas_width / 2) - (((len(solution) - 1) / 2) * (shape_width + gap_width))
        start_height = canvas_height / 2
    elif len(solution) % 2 != 0 and len(solution) >= 5:
        start_width = 150
        start_height = (canvas_height / 2) - ((gap_width + shape_width) /2)       
    elif len(solution) % 2 == 0 and len(solution) < 5:
        start_width = 150
        start_height = canvas_height / 2
    else:
        start_width = 150
        start_height = canvas_height / 4        
    for shape in range(len(solution)):
        if solution[shape] == 'cat':
            canvas.create_image(start_width,start_height, image = cat_shape)
        elif solution[shape] == 'hat':
            canvas.create_image(start_width,start_height, image = hat_shape)
        elif solution[shape] == 'broom':
            canvas.create_image(start_width,start_height, image = broom_shape)
        elif solution[shape] == 'moon':
            canvas.create_image(start_width,start_height, image = moon_shape)
        elif solution[shape] == 'pentagram':
            canvas.create_image(start_width,start_height, image = pentagram_shape)
        elif solution[shape] == 'skull':
            canvas.create_image(start_width,start_height, image = skull_shape)
        elif solution[shape] == 'coffin':
            canvas.create_image(start_width,start_height, image = coffin_shape)
        elif solution[shape] == 'bat':
            canvas.create_image(start_width,start_height, image = bat_shape)
        start_width += shape_width + gap_width
        if shape == 3:
            start_height += (shape_width + gap_width)
            if len(solution) % 2 != 0:
                start_width = (canvas_width / 2) - (((len(solution) - 5) / 2) * (shape_width + gap_width))
            elif len(solution) % 2 == 0:
                start_width = (canvas_width / 2) - (((len(solution) - 5) / 2) * (shape_width + (gap_width / 2)))
    window.update()
    time.sleep(answer_display_time)
    for shape in range(0,len(solution)):
        canvas.delete(shape + object_reference_modifier + shapes_deleted)
    shapes_deleted = shapes_deleted + len(solution)  
    window.update()
    return shapes_deleted, answer_display_time

def hide_buttons():
    canvas.itemconfig(cat, state = 'hidden')
    canvas.itemconfig(hat, state = 'hidden')
    canvas.itemconfig(broom, state = 'hidden')
    canvas.itemconfig(moon, state = 'hidden')
    canvas.itemconfig(pentagram, state = 'hidden')
    canvas.itemconfig(skull, state = 'hidden')
    canvas.itemconfig(coffin, state = 'hidden')
    canvas.itemconfig(bat, state = 'hidden')

def show_buttons():
    canvas.itemconfig(cat, state = 'normal')
    canvas.itemconfig(hat, state = 'normal')
    canvas.itemconfig(broom, state = 'normal')
    canvas.itemconfig(moon, state = 'normal')
    canvas.itemconfig(pentagram, state = 'normal')
    canvas.itemconfig(skull, state = 'normal')
    canvas.itemconfig(coffin, state = 'normal')
    canvas.itemconfig(bat, state = 'normal')

#get users answer and deterime if correct
def get_answer(solution,entire_answer_guessed):
    button_click_allowed = False    
    player_answer = ["guess"] * len(solution)
    canvas.itemconfig(enter_code, state = 'normal')    
    window.update()
    time.sleep(message_time)
    canvas.itemconfig(enter_code, state = 'hidden')     
    show_buttons()
    window.update()
    current_guess = 0
    guessed_correctly = True
    entire_answer_guessed = False
    click_count = 0
    while guessed_correctly == True:
        if canvas.coords(cat)[1] == 199.00 or canvas.coords(hat)[1] == 199.00 or canvas.coords(broom)[1] == 199.00 or canvas.coords(moon)[1] == 199.00 or canvas.coords(pentagram)[1] == 399.0 or  canvas.coords(skull)[1] == 399.0 or  canvas.coords(coffin)[1] == 399.0 or  canvas.coords(bat)[1] == 399.0:
            canvas.bind("<Button-1>",do_nothing)
        elif canvas.coords(cat)[1] == 200.00 and canvas.coords(hat)[1] == 200.00 and canvas.coords(broom)[1] == 200.00 and canvas.coords(moon)[1] == 200.00 and canvas.coords(pentagram)[1] == 400.00 and  canvas.coords(skull)[1] == 400.00 and  canvas.coords(coffin)[1] == 400.00 and  canvas.coords(bat)[1] == 400.00:
            canvas.bind("<Button-1>",get_mouse_coords)
        player_answer = append_answer_list(player_answer, solution,current_guess)
        if player_answer[current_guess] == solution[current_guess]:
            if player_answer[len(solution)-1] != "guess":
                guessed_correctly = False
                entire_answer_guessed = True
                hide_buttons()
                canvas.itemconfig(correct, state = 'normal')
                window.update()
                time.sleep(message_time)
                canvas.itemconfig(correct, state = 'hidden')
            current_guess = current_guess + 1
            time.sleep(0)
        elif player_answer[current_guess] == "guess":
            ()
        else:
            hide_buttons()
            window.update()               
            canvas.itemconfig(incorrect_code, state = 'normal')
            window.update()
            time.sleep(message_time)
            canvas.itemconfig(incorrect_code, state = 'hidden')
            show_buttons()
            guessed_correctly = False
        window.update()
    button_click_allowed = False
    return entire_answer_guessed

#check the player's answer
def append_answer_list(players_answers,  solution, current_choice):
    if canvas.coords(cat)[1] == 199.0:
        players_answers.insert(current_choice,'cat')
        players_answers.pop(len(solution))
        canvas.move(cat, 0 , 1)
        time.sleep(button_time)
        canvas.itemconfig(cat, state = 'normal')
    elif canvas.coords(hat)[1] == 199.0:
        players_answers.insert(current_choice,'hat')
        players_answers.pop(len(solution))

        canvas.move(hat, 0 , 1)
        time.sleep(button_time)
        canvas.itemconfig(hat, state = 'normal')
    elif canvas.coords(broom)[1] == 199.0:
        players_answers.insert(current_choice,'broom')
        players_answers.pop(len(solution))
        canvas.move(broom, 0 , 1)
        time.sleep(button_time)
        canvas.itemconfig(broom, state = 'normal')
    elif canvas.coords(moon)[1] == 199.0:
        players_answers.insert(current_choice,'moon')
        players_answers.pop(len(solution))
        canvas.move(moon, 0 , 1)
        time.sleep(button_time)
        canvas.itemconfig(moon, state = 'normal')
    elif canvas.coords(pentagram)[1] == 399.0:
        players_answers.insert(current_choice,'pentagram')
        players_answers.pop(len(solution))
        canvas.move(pentagram, 0 , 1)
        time.sleep(button_time)
        canvas.itemconfig(pentagram, state = 'normal')
    elif canvas.coords(skull)[1] == 399.0:
        players_answers.insert(current_choice,'skull')
        players_answers.pop(len(solution))
        canvas.move(skull, 0 , 1)
        time.sleep(button_time)
        canvas.itemconfig(skull, state = 'normal')
    elif canvas.coords(coffin)[1] == 399.0:
        players_answers.insert(current_choice,'coffin')
        players_answers.pop(len(solution))
        canvas.move(coffin, 0 , 1)
        time.sleep(button_time)
        canvas.itemconfig(coffin, state = 'normal')
    elif canvas.coords(bat)[1] == 399.0:
        players_answers.insert(current_choice,'bat')
        players_answers.pop(len(solution))
        canvas.move(bat, 0 , 1)
        time.sleep(button_time)
        canvas.itemconfig(bat, state = 'normal')
    return players_answers

# updates save file if completing in main game for first time
def update_progress(mini_game):
    progress_file = open("progress.txt", "w")   
    progress_file.write(mini_game)
    progress_file.close()

#get difficulty
difficulty_file = open("difficulty.txt", "r")
difficulty = difficulty_file.read()
difficulty_file.close()

#get game type
game_type_file = open("game_type.txt", "r")
game_type = game_type_file.read()
game_type_file.close()

#get previous game progress if main game is being played currently
if game_type == "main game":
    progress_file = open("progress.txt", "r")
    progress = progress_file.read()
    progress_file.close()

#initialise variables
canvas_width = 1000
canvas_height = 600
shape_width = 200
gap_width = 50
default_shapes = ["cat", "hat", "broom", "moon", "pentagram", "skull", "coffin", "bat"]
if difficulty == "easy":
     smallest_length = 3
     longest_length = 5
     answer_time = 2.00
     answer_time_increment = 0.6
elif difficulty == "medium":
     smallest_length = 3
     longest_length = 6
     answer_time = 1.75
     answer_time_increment = 0.5
elif difficulty == "hard":     
     smallest_length = 3
     longest_length = 7
     answer_time = 1.2
     answer_time_increment = 0.15


solution_hide_modifier = 0
current_length = smallest_length
answer = []
button_time = 0.1

message_time = 1
wait_time = 1
object_reference_modifier = 15

#initialise window
window = Tk()
window.title("Memory game")
canvas = Canvas(window, width = canvas_width, height = canvas_height)
canvas.pack()
canvas.create_rectangle(0,0,canvas_width,canvas_height,fill = 'black')

#import shapes
cat_shape = PhotoImage(file = 'cat.png')
hat_shape = PhotoImage(file = 'hat.png')
broom_shape = PhotoImage(file = 'broom.png')
moon_shape = PhotoImage(file = 'moon.png')
pentagram_shape = PhotoImage(file = 'pentagram.png')
skull_shape = PhotoImage(file = 'skull.png')
coffin_shape = PhotoImage(file = 'coffin.png')
bat_shape = PhotoImage(file = 'bat.png')
incorrect_code_shape = PhotoImage(file = 'incorrect_code.png')
memorise_shape = PhotoImage(file = 'memorise.png')
enter_code_shape = PhotoImage(file = 'enter_code.png')
correct_shape = PhotoImage(file = 'correct.png')
cat = canvas.create_image(200,200, image = cat_shape)
hat = canvas.create_image(400,200, image = hat_shape)
broom = canvas.create_image(600,200, image = broom_shape)
moon = canvas.create_image(800,200, image = moon_shape)
pentagram = canvas.create_image(200,400, image = pentagram_shape)
skull = canvas.create_image(400,400, image = skull_shape)
coffin = canvas.create_image(600,400, image = coffin_shape)
bat = canvas.create_image(800,400, image = bat_shape)
incorrect_code = canvas.create_image(500,300, image = incorrect_code_shape)
memorise = canvas.create_image(500,300, image = memorise_shape)
enter_code = canvas.create_image(500,300, image = enter_code_shape)
correct = canvas.create_image(500,300, image = correct_shape)


hide_buttons()
canvas.itemconfig(incorrect_code, state = 'hidden')
canvas.itemconfig(memorise, state = 'hidden')
canvas.itemconfig(enter_code, state = 'hidden')
canvas.itemconfig(correct, state = 'hidden')
clicked_button = canvas.create_rectangle(0,1,2,3)

#shuffle shapes and generate solution
random.shuffle(default_shapes)
entire_answer_correct = False
#create first solution
answer = create_new_solution(current_length, answer)
# display solution

while entire_answer_correct == False:
    solution_hide_modifier, answer_time = display_solution(answer, solution_hide_modifier, answer_time)
    entire_answer_correct = get_answer(answer,entire_answer_correct)
while current_length < longest_length:
    entire_answer_correct = False
    current_length += 1    
    answer = create_new_solution(current_length, answer)    
    while entire_answer_correct == False:
        solution_hide_modifier, answer_time = display_solution(answer, solution_hide_modifier, answer_time)
        entire_answer_correct = get_answer(answer,entire_answer_correct)
    answer_time += answer_time_increment

if game_type == "main game":
    winner_display = PhotoImage(file = 'won_memory_plot.png')
    if progress == "hangman complete":
        progress = "memory complete"
        update_progress(progress)
    current_progress_file = open("current_progress.txt", "w")   
    current_progress_file.write("memory game complete")
    current_progress_file.close()       
else:
    winner_display = PhotoImage(file = 'winner.png') 
winner = canvas.create_image(500,300, image = winner_display)
window.update()
time.sleep(5)
canvas.delete(ALL)        
window.destroy()
window.mainloop()


