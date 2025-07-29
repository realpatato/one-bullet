''' MAIN FILE - HANDLES GAME LOOP AND CONNECTS EVERYTHING '''
''' IMPORTS '''
#needed for all visual functionality
import pygame
#needed for player object
import player_manager as pm
#needed for wall objects
import wall as w

''' PYGAME SETUP '''
#starts the module
pygame.init()

#variables for screen size
screen_width = 1200
screen_height = 600
#creates the screen
screen = pygame.display.set_mode((screen_width, screen_height))
#sets the screen caption
pygame.display.set_caption("One Bullet")

''' GAME OBJECT SETUPS '''
#loads in the sprite for the Player
player_sprite = pygame.image.load("main-stuff/arrow.png")
#creates the player with the sprite
player = pm.Player(player_sprite, screen)

wall_sprite = pygame.image.load("main-stuff/sprites/120x120PLACEHOLDER.png")
#creates walls
wall_tiles = [w.Wall_Tile(wall_sprite, screen, (0, 0)), w.Wall_Tile(wall_sprite, screen, (0, 120))]
'''
for r in range(3):
    for c in range(3):
        wall_tile = w.Wall_Tile(wall_sprite, screen, (r*40, c*40))
        wall_tiles.append(wall_tile)
'''
        
''' GAME LOOP SET UP '''
#clock for frame rate management
clock = pygame.time.Clock()
#variable to control loop
keep_playing = True

''' GAME LOOP '''
while keep_playing:
    #start with getting the mouse position
    mouse_pos = pygame.mouse.get_pos()
    #rotate the player before continuing too
    player.player_rotate(mouse_pos)

    #check for events
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            player.spawn_bullet()

        #check if the player has quit
        if event.type == pygame.QUIT:
            #set control variable to false
            keep_playing = False

    screen.fill((0, 0, 0))

    if player._bullet != None:
        player._bullet.bullet_movement(wall_tiles)
        player._bullet.draw_bullet()

    player.draw_self()

    for wall in wall_tiles:
        wall.draw_self()

    #update the screen
    pygame.display.update()

    #ticks the clock
    clock.tick(60)

''' ENDING THE PROGRAM '''
#quits the window
pygame.quit()
#ends the program
quit()