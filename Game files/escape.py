# Chris Burrell
# Running game

import random
import time
import tkinter
from tkinter import *

def show_instructions():
    plot_visible = True
    instructions_visible = True
    canvas.itemconfig(end_plot, state = 'normal')     
    while plot_visible == True:
        canvas.bind("<Button-1>", playermovement)
        if canvas.coords(end_plot)[0] < 500:
            plot_visible = False
            canvas.itemconfig(end_plot, state = 'hidden')
            window.update()
    canvas.itemconfig(instructions, state = 'normal') 
    while instructions_visible == True:
        canvas.bind("<Button-1>", playermovement)
        if canvas.coords(instructions)[0] < 500:
            instructions_visible = False
            canvas.itemconfig(instructions, state = 'hidden')
            window.update()        

# moves the retry screen one pixel up or down, dependant on if yes or no is clicked
def getorigin(event_coords):
    x = event_coords.x
    y = event_coords.y
    if (x >= 280 and x <= 407) and (y >= 425 and y <= 465):
        canvas.move(retry_screen,0,-1)         
    elif (x >= 560 and x <= 660) and (y >= 425 and y <= 465):
        canvas.move(retry_screen,0,1)

# animates players run and jump
def animate_player(animated_time,first_run):
    if canvas.coords(Player)[3] < ground_level:
        canvas.itemconfig(player_skin_1, state = 'hidden')        
        canvas.itemconfig(player_skin_2, state = 'hidden')
    elif animated_time >= player_switch_time:
        if first_run == True:
            canvas.itemconfig(player_skin_1, state = 'hidden')        
            canvas.itemconfig(player_skin_2, state = 'normal')
            canvas.itemconfig(player_jumping, state = 'hidden')
            first_run = False
        else:    
            canvas.itemconfig(player_skin_1, state = 'normal')        
            canvas.itemconfig(player_skin_2, state = 'hidden')
            canvas.itemconfig(player_jumping, state = 'hidden')  
            first_run = True
        animated_time = 0
    else:
        animated_time += 1
    return animated_time, first_run

# move ground
def move_ground():
    if canvas.coords(ground)[0] <= 0.1:
        canvas.move(ground, 1000 , 0)
    else:
        canvas.move(ground, obstaclemovement , 0)

# draw obstacle
def draw_obstacle(obs_count):
    if obstacles[obs_count] == unshuffled_obstacles [0]:
        canvas.create_image((unshuffled_obstacles[0][0]+unshuffled_obstacles[0][2])/2, (unshuffled_obstacles[0][1]+unshuffled_obstacles[0][3])/2, image = obstacle_1_base)
    elif obstacles[obs_count] == unshuffled_obstacles [1]:       
        canvas.create_image((unshuffled_obstacles[1][0]+unshuffled_obstacles[1][2])/2, (unshuffled_obstacles[1][1]+unshuffled_obstacles[1][3])/2, image = obstacle_2_base)
    elif obstacles[obs_count] == unshuffled_obstacles [2]:
        canvas.create_image((unshuffled_obstacles[2][0]+unshuffled_obstacles[2][2])/2, (unshuffled_obstacles[2][1]+unshuffled_obstacles[2][3])/2, image = obstacle_3_base)



# initiates a player jump on a mouse click (also clicks through main screens)
def playermovement(event):
    if canvas.coords(end_plot)[0] == 500.0:
        canvas.move(end_plot, -1 , 0)
    elif canvas.coords(instructions)[0] == 500.0:
        canvas.move(instructions, -1 , 0)
    elif canvas.coords(Player)[3] == ground_level:
        canvas.move(Player,0,-1)
        canvas.move(player_skin_1,0,-1)
        canvas.move(player_skin_2,0,-1)
        canvas.move(player_jumping,0,-1)
        canvas.itemconfig(player_jumping, state = 'normal')

# checks if player is currently jumping, falling or in the jump apex (hanging in mid air)
def playerjump(rising, declining, reached_apex, count_apex):
    # test if jump has been initiated
    if canvas.coords(Player)[3] == ground_level - 1.0:
        rising = True
    # move jumping player
    if rising == True:
        canvas.move(Player,0,-jump_speed)
        canvas.move(player_skin_1,0,-jump_speed)
        canvas.move(player_skin_2,0,-jump_speed)
        canvas.move(player_jumping,0,-jump_speed) 
        # test if player has reached jump apex
        if (canvas.coords(Player)[1]) <= jump_height:
            rising = False
            reached_apex = True
    # stop player from moving up if jump apex reached
    if reached_apex == True:
        count_apex += 1
        # test if player has been stationary in jump apex for amount of time equal to count_apex, if so initiates falling
        if count_apex == apex_duration:
            reached_apex = False
            declining = True
            count_apex = 0
    # moves player down if they are falling
    if declining == True:
        canvas.move(Player,0,jump_speed)
        canvas.move(player_skin_1,0,jump_speed)
        canvas.move(player_skin_2,0,jump_speed)
        canvas.move(player_jumping,0,jump_speed) 
        if (canvas.coords(Player)[3]) >= ground_level - 1.0:
            canvas.move(Player,0,ground_level - canvas.coords(Player)[3])
            canvas.move(player_skin_1,0,jump_speed)
            canvas.move(player_skin_2,0,jump_speed)
            canvas.move(player_jumping,0,jump_speed) 
            declining = False
    if (canvas.coords(Player)[3]) >= ground_level:
        canvas.coords(Player,50,player_height,50 + player_width,ground_level)
        canvas.coords(player_skin_1,(canvas.coords(Player)[0] + canvas.coords(Player)[2]) / 2, (canvas.coords(Player)[1] + canvas.coords(Player)[3]) / 2)
        canvas.coords(player_skin_2,(canvas.coords(Player)[0] + canvas.coords(Player)[2]) / 2, (canvas.coords(Player)[1] + canvas.coords(Player)[3]) / 2)
        canvas.coords(player_jumping,(canvas.coords(Player)[0] + canvas.coords(Player)[2]) / 2, (canvas.coords(Player)[1] + canvas.coords(Player)[3]) / 2)
    return rising, declining, reached_apex, count_apex

def detect_collission(obstacle, hasflash, lives, alive):
    obstacle = obstacle + mod_1
    # test if the incoming object is underneath Player
    if canvas.coords(obstacle)[0] <= canvas.coords(Player)[2] - collision_leniance and canvas.coords(obstacle)[2] >= canvas.coords(Player)[0] + collision_leniance:
        # test if the bottom of the player is lower than the top of the incoming object 
        if canvas.coords(Player)[3] - collision_leniance >= canvas.coords(obstacle)[1]:
            # test if player has invulnerability, where false, deducts one life and gives invulnerability
            if hasflash == False:
                if lives == 3:
                    canvas.itemconfig(life_box_1, fill = '',outline = '')
                if lives == 2:
                    canvas.itemconfig(life_box_2, fill = '',outline = '')
                if lives == 1:
                    canvas.itemconfig(life_box_3, fill = '',outline = '')
                if lives <= 0:
                    alive = False
                lives = lives - 1
                hasflash = True
    return hasflash, lives, alive

def animate_flash(hasflash, count_flash,first_run_visible):
    # if the player has invulnerability, this makes the player flash
    if hasflash == True:
        # animates flash when jumping
        if canvas.coords(Player)[3] < ground_level:
            count_flash = count_flash + 1
            if count_flash % flash_mod == 0:
                canvas.itemconfig(player_jumping, state = 'normal')
            elif count_flash % (flash_mod/2) == 0:
                canvas.itemconfig(player_jumping, state = 'hidden')
        # animates flash on first run skin
        elif first_run_visible == True:
            count_flash = count_flash + 1
            if count_flash % flash_mod == 0:
                canvas.itemconfig(player_skin_1, state = 'normal')
            elif count_flash % (flash_mod/2) == 0:
                canvas.itemconfig(player_skin_1, state = 'hidden')
        # animates flash on second run skin
        else:
            count_flash = count_flash + 1
            if count_flash % flash_mod == 0:
                canvas.itemconfig(player_skin_2, state = 'normal')
            elif count_flash % (flash_mod / 2) == 0:
                canvas.itemconfig(player_skin_2, state = 'hidden')
                
    return count_flash
        
# animates movement prior to second obstacle being created
def createsecondshape(sixhunreached, jumping, falling, flash, countdown, landed, top_reached, top_count,animated_duration,first_animation_visible):
    while sixhunreached == False:
        # moves obstacles
        canvas.move(obs + mod_1,obstaclemovement,0)
        canvas.move(obs + mod_1 + 1,obstaclemovement,0)
        # checks mouse click for jump
        canvas.bind("<Button-1>", playermovement)
        # performs jump, player and ground animations
        jumping, falling, top_reached, top_count = playerjump(jumping, falling, top_reached, top_count)
        animated_duration, first_animation_visible = animate_player(animated_duration,first_animation_visible)
        move_ground()
        window.update()
        time.sleep(sleeptime)
        # check if a new obstacle is required, if so, creates one and ends function
        if canvas.coords(obs + mod_1)[2] <= first_quarter_screen - random.randint(spawn_variation_1,spawn_variation_2):
            canvas.create_rectangle(obstacles[obs + 1][0],obstacles[obs + 1][1],obstacles[obs + 1][2],obstacles[obs + 1][3],fill = '',outline = '')
            draw_obstacle(obs+1)
            sixhunreached = True
    return jumping, falling, top_reached, top_count,animated_duration,first_animation_visible

# animates movement prior to third obstacle being created
def createthirdshape(fourhunreached, jumping, falling, flash, countdown, landed, top_reached, top_count,animated_duration,first_animation_visible):
    while fourhunreached == False:
        # moves obstacles        
        canvas.move(obs + mod_1,obstaclemovement,0)
        canvas.move(obs + mod_1+1,obstaclemovement,0)
        canvas.move(obs + mod_2,obstaclemovement,0)
        canvas.move(obs + mod_2+1,obstaclemovement,0)
        # checks mouse click for jump
        canvas.bind("<Button-1>", playermovement)
        jumping, falling, top_reached, top_count = playerjump(jumping, falling, top_reached, top_count)
        animated_duration, first_animation_visible = animate_player(animated_duration,first_animation_visible)
        move_ground()
        window.update()
        time.sleep(sleeptime)
        # check if a new obstacle is required, if so, creates one and ends function
        if canvas.coords(obs + mod_1)[2] <= half_screen - random.randint(spawn_variation_1,spawn_variation_2):
            canvas.create_rectangle(obstacles[obs + 2][0],obstacles[obs + 2][1],obstacles[obs + 2][2],obstacles[obs + 2][3],fill = '',outline = '')
            draw_obstacle(obs+2)            
            fourhunreached = True
    return jumping, falling, top_reached, top_count,animated_duration,first_animation_visible

# animates movement prior to fourth obstacle being created
def createfourthshape(twohunreached, jumping, falling, flash, countdown, landed, top_reached, top_count,animated_duration,first_animation_visible):
    while twohunreached == False:
        # moves obstacles
        canvas.move(obs + mod_1,obstaclemovement,0)
        canvas.move(obs + mod_1+1,obstaclemovement,0)        
        canvas.move(obs + mod_2,obstaclemovement,0)
        canvas.move(obs + mod_2+1,obstaclemovement,0)        
        canvas.move(obs + mod_3,obstaclemovement,0)
        canvas.move(obs + mod_3+1,obstaclemovement,0)
        # checks mouse click for jump
        canvas.bind("<Button-1>", playermovement)
        # performs jump, player and ground animations
        jumping, falling, top_reached, top_count = playerjump(jumping, falling, top_reached, top_count)
        animated_duration, first_animation_visible = animate_player(animated_duration,first_animation_visible)
        move_ground()
        window.update()
        time.sleep(sleeptime)
        # check if a new obstacle is required, if so, creates one and ends function
        if canvas.coords(obs + mod_1)[2] <= last_quarter_screen - random.randint(spawn_variation_1,spawn_variation_2):
            canvas.create_rectangle(obstacles[obs + 3][0],obstacles[obs + 3][1],obstacles[obs + 3][2],obstacles[obs + 3][3],fill = '',outline = '')
            draw_obstacle(obs+3)  
            twohunreached = True
    return jumping, falling, top_reached, top_count,animated_duration,first_animation_visible

# animates movement once four obstacles have been created
def movefourshapes(obs, jumping, falling, flash, countdown, landed, top_reached, top_count, lifebar, game_is_on, flash_counter, player_won,animated_duration,first_animation_visible, try_more):
    draw_count = 0
    # loop while not on the last four obstacles
    while obs != len(obstacles) - 4 and game_is_on == True:
        # moves obstacles
        canvas.move(draw_count + mod_1,obstaclemovement,0)
        canvas.move(draw_count + mod_1 + 1,obstaclemovement,0)        
        canvas.move(draw_count + mod_2,obstaclemovement,0)
        canvas.move(draw_count + mod_2 + 1,obstaclemovement,0)
        canvas.move(draw_count + mod_3,obstaclemovement,0)
        canvas.move(draw_count + mod_3 + 1,obstaclemovement,0)
        canvas.move(draw_count + mod_4,obstaclemovement,0)
        canvas.move(draw_count + mod_4 + 1,obstaclemovement,0)
        # checks mouse click for jump
        canvas.bind("<Button-1>", playermovement)
        # performs jump animation
        jumping, falling, top_reached, top_count = playerjump(jumping, falling, top_reached, top_count)
        # invulnerability reset calculations
        if flash == True:
            if countdown > 0:
                countdown = countdown - sleeptime
            else:
                flash = False
                countdown = flashduration
                if canvas.coords(Player)[3] < ground_level:
                    canvas.itemconfig(player_jumping, state = 'normal')
        else:
            # collision detection
            flash, lifebar, game_is_on = detect_collission(draw_count, flash, lifebar, game_is_on)
        # animate flash
        flash_counter = animate_flash(flash, flash_counter,first_animation_visible)
        if flash == False:
            flash_counter = 0
        # animate player then ground
        animated_duration, first_animation_visible = animate_player(animated_duration,first_animation_visible)
        move_ground()
        window.update()
        time.sleep(sleeptime)
        # check if a new obstacle is required, if so, creates one
        if canvas.coords(draw_count + mod_1)[2] <= 0 - random.randint(spawn_variation_1,spawn_variation_2):
            canvas.create_rectangle(obstacles[obs + 4][0],obstacles[obs + 4][1],obstacles[obs + 4][2],obstacles[obs + 4][3],fill = '',outline = '')
            draw_obstacle(obs+4)            
            obs = obs +1
            draw_count = draw_count + 2
    # animates movement for final four obstacles
    while obs >= len(obstacles) - 4 and game_is_on == True:
        # moves obstacles
        canvas.move(draw_count + mod_1,obstaclemovement,0)
        canvas.move(draw_count + mod_1 + 1,obstaclemovement,0)        
        canvas.move(draw_count + mod_2,obstaclemovement,0)
        canvas.move(draw_count + mod_2 + 1,obstaclemovement,0)
        canvas.move(draw_count + mod_3,obstaclemovement,0)
        canvas.move(draw_count + mod_3 + 1,obstaclemovement,0)
        canvas.move(draw_count + mod_4,obstaclemovement,0)
        canvas.move(draw_count + mod_4 + 1,obstaclemovement,0)
        # checks mouse click for jump
        canvas.bind("<Button-1>", playermovement)
        # performs jump animation
        jumping, falling, top_reached, top_count = playerjump(jumping, falling, top_reached, top_count)
        # invulnerability reset calculations
        if flash == True:
            if countdown > 0:
                countdown = countdown - sleeptime
            else:
                flash = False
                countdown = flashduration
                if canvas.coords(Player)[3] < ground_level:
                    canvas.itemconfig(player_jumping, state = 'normal')
        else:
            # collision detection
            if canvas.coords(draw_count + mod_3)[2] <= 0:
                flash, lifebar, game_is_on = detect_collission(draw_count + 6, flash, lifebar, game_is_on)
            elif canvas.coords(draw_count + mod_2)[2] <= 0:
                flash, lifebar, game_is_on = detect_collission(draw_count + 4, flash, lifebar, game_is_on)
            elif canvas.coords(draw_count + mod_1)[2] <= 0:
                flash, lifebar, game_is_on = detect_collission(draw_count + 2, flash, lifebar, game_is_on)
            else:
                flash, lifebar, game_is_on = detect_collission(draw_count + 0, flash, lifebar, game_is_on)
        # animate flash
        flash_counter = animate_flash(flash, flash_counter,first_animation_visible)
        if flash == False:
            flash_counter = 0
        # animate player then ground
        animated_duration, first_animation_visible = animate_player(animated_duration,first_animation_visible)
        move_ground()
        window.update()
        time.sleep(sleeptime)
        # test if end of level reached
        if canvas.coords(draw_count + mod_4)[2] <= 0:
            player_won = True
            try_more = False
            obs = 0
    return jumping, falling, flash, countdown, top_reached, top_count, lifebar, game_is_on, flash_counter, player_won,animated_duration,first_animation_visible, try_more

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

try_again = True
# main game loop, try again becomes false if player wins or if they die and choose not to try again
while try_again == True:

    # Initialise variables - these should never be changed
    grounded = True
    sixhundredreached = False
    fourhundredreached = False
    twohundredreached = False
    obs = 0
    jumpingup = False
    fallingdown = False
    flashing = False
    apex_reached = False
    apex_count = 0
    flash_count = 0
    winner = False
    animated_first_run = True
    player_animated_for = 0
    game_on = True

    # obstacle modifiers - increment by 1 if an additional object is introduced before drawing obstacles
    mod_1 = 12
    mod_2 = 14
    mod_3 = 16
    mod_4 = 18

    # changeable variables which affect gameplay and visuals
    life = 3
    # Number of obstacles spawning is equal to 3 times the obstacle repeat value
    if difficulty == "easy":
            obstacle_repeat = 5
    elif difficulty == "medium":
            obstacle_repeat = 10
    elif difficulty == "hard":
            obstacle_repeat = 20
    flashduration = 1.2
    flash_countdown = flashduration
    flash_mod = 2
    sleeptime = 0.01
    obstaclemovement = -5
    ground_level = 500
    player_height = ground_level - 125
    player_width = 55
    apex_duration = 20
    jump_height = 195
    jump_speed = 15
    canvas_height = 600
    canvas_width = 1000
    first_quarter_screen = canvas_width / 4 * 3
    half_screen = canvas_width / 2
    last_quarter_screen = canvas_width / 4
    player_switch_time = 3
    collision_leniance = 5
    spawn_variation_1 = 25
    spawn_variation_2 = 50
    life_bar_x_axis = 10
    life_bar_y_axis = 10
    life_bar_size = 30
    life_bar_gap = 10

    #initialise window
    window = Tk()
    window.title("Runner")
    canvas = Canvas(window, width = canvas_width, height = canvas_height)
    canvas.pack()

    #create obstacles list
    unshuffled_obstacles = [[canvas_width - 45,ground_level - 100,canvas_width,ground_level],[canvas_width - 65,ground_level - 65,canvas_width,ground_level],[canvas_width - 35,ground_level - 80,canvas_width,ground_level]] * obstacle_repeat
    obstacles = [[canvas_width - 45,ground_level - 100,canvas_width,ground_level],[canvas_width - 65,ground_level - 65,canvas_width,ground_level],[canvas_width - 35,ground_level - 80,canvas_width,ground_level]] * obstacle_repeat
    random.shuffle(obstacles)

    #create initial game objects

    # create sky
    nightsky = PhotoImage(file = 'sky.png')
    sky = canvas.create_image(canvas_width / 2, canvas_height / 2, image = nightsky)

    #create player sprites
    Player = canvas.create_rectangle(50,player_height,50 + player_width,ground_level,fill = '',outline = '')
    player_skin_base_1 = PhotoImage(file = 'player_running_1.png')
    player_skin_base_2 = PhotoImage(file = 'player_running_2.png')
    player_skin_base_jump = PhotoImage(file = 'player_jumping.png')
    player_skin_1 = canvas.create_image((canvas.coords(Player)[0] + canvas.coords(Player)[2]) / 2, (canvas.coords(Player)[1] + canvas.coords(Player)[3]) / 2, image = player_skin_base_1)
    player_skin_2 = canvas.create_image((canvas.coords(Player)[0] + canvas.coords(Player)[2]) / 2, (canvas.coords(Player)[1] + canvas.coords(Player)[3]) / 2, image = player_skin_base_2)
    player_jumping = canvas.create_image((canvas.coords(Player)[0] + canvas.coords(Player)[2]) / 2, (canvas.coords(Player)[1] + canvas.coords(Player)[3]) / 2, image = player_skin_base_jump)
    canvas.itemconfig(player_skin_2, state = 'hidden')
    canvas.itemconfig(player_jumping, state = 'hidden')

    # create ground
    land = PhotoImage(file = 'ground.png')
    ground = canvas.create_image(canvas_width, ground_level + (canvas_height - ground_level) / 2, image = land)

    # initialise obstacle images
    obstacle_1_base = PhotoImage(file = 'obstacle_1.png')
    obstacle_2_base = PhotoImage(file = 'obstacle_2.png')
    obstacle_3_base = PhotoImage(file = 'obstacle_3.png')

    # creates life bars - determined by variables which can be modified above
    life_box_3 = canvas.create_rectangle(life_bar_x_axis,life_bar_y_axis,life_bar_x_axis + life_bar_size,life_bar_y_axis + life_bar_size, fill = "red")
    life_box_2 = canvas.create_rectangle(life_bar_x_axis + life_bar_size + life_bar_gap,life_bar_y_axis,(life_bar_x_axis + life_bar_size) * 2,life_bar_y_axis + life_bar_size, fill = "red")
    life_box_1 = canvas.create_rectangle(life_bar_x_axis + (life_bar_size + life_bar_gap) *2,life_bar_y_axis,(life_bar_x_axis + life_bar_size) * 3,life_bar_y_axis + life_bar_size, fill = "red")

    # creates initial game screens and runs function to display
    end_plot_display = PhotoImage(file = 'start.png')
    end_plot = canvas.create_image(500,300, image = end_plot_display)
    canvas.itemconfig(end_plot, state = 'hidden')
    instructions_display = PhotoImage(file = 'instructions.png')
    instructions = canvas.create_image(500,300, image = instructions_display)
    canvas.itemconfig(instructions, state = 'hidden')
    if game_type == "main game":
        plot_visible = True
    else:
        plot_visible = False
        canvas.move(end_plot, -1 , 0)
    instructions_visible = True
    canvas.itemconfig(end_plot, state = 'normal')
    window.update()
    while plot_visible == True:
        canvas.bind("<Button-1>", playermovement)
        if canvas.coords(end_plot)[0] < 500:
            canvas.itemconfig(instructions, state = 'normal')            
            canvas.itemconfig(end_plot, state = 'hidden')
            time.sleep(sleeptime)
            plot_visible = False
        window.update()          
        time.sleep(sleeptime)
    canvas.itemconfig(end_plot, state = 'hidden')
    canvas.itemconfig(instructions, state = 'normal')
    window.update()
    
    while instructions_visible == True:
        canvas.bind("<Button-1>", playermovement)
        if canvas.coords(instructions)[0] < 500:
            instructions_visible = False
            canvas.itemconfig(instructions, state = 'hidden')
        window.update()  
        time.sleep(sleeptime)

    # create first object
    canvas.create_rectangle(obstacles[0][0],obstacles[0][1],obstacles[0][2],obstacles[0][3],fill = '',outline = '')
    draw_obstacle(obs)

    # main animation functions
    jumpingup, fallingdown, apex_reached, apex_count,player_animated_for,animated_first_run = createsecondshape(sixhundredreached,jumpingup,fallingdown,flashing, flash_countdown, grounded, apex_reached, apex_count,player_animated_for,animated_first_run)
    jumpingup, fallingdown, apex_reached, apex_count,player_animated_for,animated_first_run = createthirdshape(fourhundredreached,jumpingup,fallingdown,flashing, flash_countdown, grounded, apex_reached, apex_count,player_animated_for,animated_first_run)
    jumpingup, fallingdown, apex_reached, apex_count,player_animated_for,animated_first_run = createfourthshape(twohundredreached,jumpingup,fallingdown,flashing, flash_countdown, grounded, apex_reached, apex_count,player_animated_for,animated_first_run)
    jumpingup, fallingdown, flashing, flash_countdown, apex_reached, apex_count, life, game_on, flash_count, winner,player_animated_for,animated_first_run, try_again = movefourshapes(obs,jumpingup,fallingdown, flashing, flash_countdown, grounded, apex_reached, apex_count,life, game_on, flash_count, winner,player_animated_for,animated_first_run, try_again)

    # test if player won
    if winner == True:
        if game_type == "main game":
            game_over = PhotoImage(file = 'won_escape_plot.png')
            if progress == "memory complete":
                progress = "all"
                update_progress(progress)
                
        else:    
            game_over = PhotoImage(file = 'winner.png')
    # if player lost, display try again screen
    else:
        game_over = PhotoImage(file = 'game_over.png')    
        try_again_screen = True
        while try_again_screen == True:
            retry_game = PhotoImage(file = 'try_again.png')
            retry_screen = canvas.create_image(500, 300, image = retry_game)
            window.update()
            canvas.bind("<Button-1>",getorigin)
            # test if player clicked yes
            if canvas.coords(retry_screen)[1] == 299.0:
                try_again_screen = False
                canvas.delete(ALL)        
                window.destroy()
            # test if player clicked no
            elif canvas.coords(retry_screen) [1] == 301.0:
                try_again_screen = False
                try_again = False
            
# display victory or game over screen
canvas.create_image(500, 300, image = game_over)
window.update()
time.sleep(5)
# exit game
canvas.delete(ALL)        
window.destroy()       
window.mainloop()   
