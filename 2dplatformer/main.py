import pygame, sys
from settings import * 
from level import Level


# Pygame setup
pygame.init()

# create a variable that creates a window with a tuple as the dimensions 
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) 

# creates a variable that calls the .load function and uses a .png file as an argument 
# icon = pygame.image.load("emoji_man_rect.png")

# calls a function that assign the argument as a window icon, takes the icon variable as an argument 
# pygame.display.set_icon(icon)

# calls a function that assign a name to the window, takes a string as an argument 
pygame.display.set_caption("Emoji-Man in Rectland")

# creates an instance/object of the Clock class
clock = pygame.time.Clock()

# creates an instance of the Level class
level = Level()


while True:
    
    # event loop
    # checks for events(inputs) from the user every loop
    for event in pygame.event.get():

        # if the event.type is .QUIT(the X button) then run the indented code 
        if event.type == pygame.QUIT:
            
            # closes the window and shuts down the program
            pygame.quit()
            sys.exit()

    # calls the .fill method in the screen instance(class) that takes a tuple with three integers as an argument 
    screen.fill(BG_COLOR)

    # calls the .run method in the level instance(class) 
    level.run()

    # drawing logic
    # calls the .update function that updates the entire surface area  
    pygame.display.update()

    # calls the .tick method and gives it integer of 60 as an argument
    clock.tick(60)

