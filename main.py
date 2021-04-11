""" 
Name: ICS20 - CPT 2021 Danielle Nguyen

Purpose: Bitcoin Mining Animation

Author: Danielle Nguyen

Created: 2021-03-28
"""
 
import pygame
 
# Define some colors - 
# BLACK for the image background
# GREY - text backbround
# WHITE - for text color
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
#GREEN    = (   0, 255,   0)
#RED      = ( 255,   0,   0)
GREY     = (81, 90, 90)
 
pygame.init()
  
# Set the width and height of the screen [width, height]
screen_width = 750
screen_height = 580
size = [screen_width, screen_height]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Danielle's Bitcoin Mining Simulator")
 
#Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize the conveyor belt location
box_x = 0
box_y = 400
box_x_velocity = 12
box_go = False

# Initialize the location of the coin on the conveyor
box_x2 = 0
box_y2 = 375
box_x2_velocity = 12
box2_go = False

# Initialize the coordinates of the Miner
miner_x = 200 
miner_y = 280 
miner_velocity = 5
jump = False
jumpcount = 10

# Location of treasure chest - fixed and not moving
treasure_x = 650
treasure_y = 310

# Initial coordinates of the Bitcoins to catch
coin_x = 200
coin_y = 120
coin_x_velocity = 5
coin_go = False

# --------- Dani Load images ---------
# images are from kenney.ln

# Background of the screen
background_image = pygame.image.load("background.png").convert()
background_image = pygame.transform.scale(background_image, (750, 500))

# Bitcoin image - transform scale to resize the image
bitcoin_image = pygame.image.load("bitcoin.png").convert()
bitcoin_image.set_colorkey(BLACK)
bitcoin_image = pygame.transform.scale(bitcoin_image, (50, 25))

# Miner image
miner_image = pygame.image.load("miner.png").convert()
miner_image.set_colorkey(BLACK)
miner_image = pygame.transform.scale(miner_image, (90, 80))

# conveyor image
wheel_image1=pygame.image.load("conveyor.png").convert()
wheel_image1.set_colorkey(BLACK)

# Treasure chest image to pretend to keep all the coins
treasure_image = pygame.image.load("chest.png").convert()
treasure_image.set_colorkey(BLACK)
treasure_image = pygame.transform.scale(treasure_image, (100, 100))

# ----------  Fonts and size to use -----------
font = pygame.font.SysFont('Calibri', 20, True, False)
# font2 = pygame.font.SysFont('Calibri', 15, True, False)


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
    # Declare the keys    
    keys = pygame.key.get_pressed() 

    # --- Game logic should go here
    # -------Start Danielle
    # ---  Background Image from <> ----
    screen.blit(background_image, [0, 0])
   
    # ------ Miner position ---------
    screen.blit(miner_image, [miner_x,miner_y])

      # ------ Coin position ---------
    screen.blit(bitcoin_image, [coin_x,coin_y])

    # --------- Treasure chest --------
    screen.blit(treasure_image, [treasure_x, treasure_y])

    # --- Miner walking left and right with the arrow keys ---
    if keys[pygame.K_LEFT ] and miner_x > miner_velocity:
      miner_x -= miner_velocity
    if keys[pygame.K_RIGHT] and miner_x < screen_width - 50 - miner_velocity:
      miner_x += miner_velocity
    
    # ----- Miner moving up and down arrow keys -----  
    if not (jump):
      if keys[pygame.K_UP] and miner_y > miner_velocity:
        miner_y -= miner_velocity
      if keys[pygame.K_DOWN] and miner_y < screen_height - 50 - miner_velocity:
        miner_y += miner_velocity
      
      # Press key space to jump
      if keys[pygame.K_SPACE]:
        jump = True

    # ------ Miner is jumping and jumpcount = 9 ------
    else:
      if jumpcount >= -10:
        n_1 = 1
        if jumpcount < 0:
          n_1 = -1
        miner_y -= (jumpcount ** 2) * 0.5 * n_1
        jumpcount -= 1
      # if not jumping set it to false and back to jumpcount 9  
      else: 
        jump = False
        jumpcount = 10
    
    # ----- Coins moving for the miner to catch ------ 
    coin_go = True
    if coin_x > screen_width or coin_x < 0:
      coin_x = 0
    if coin_go:
      coin_x += coin_x_velocity
    
    # ----- If condition when the miner hits the coin -----
    if (miner_x <= coin_x and coin_x <= miner_x+80) and (miner_y <= coin_y and coin_y <= miner_y+ 120):
      # set the coin x position to 0 if it hits the miner to start the coin again 
      coin_x = 0
      print("hit")

    # ---- loop the conveyor when it hits the wall -----
    box_go = True
    if box_x+675 > screen_width or box_x < 0:
      box_x =0
    if box_go:
      box_x += box_x_velocity

    # display the conveyor multiple times
    screen.blit(wheel_image1, [box_x, box_y])
    screen.blit(wheel_image1, [box_x+75, box_y])
    screen.blit(wheel_image1, [box_x+150, box_y])
    screen.blit(wheel_image1, [box_x+225, box_y])
    screen.blit(wheel_image1, [box_x+300, box_y])
    screen.blit(wheel_image1, [box_x+375, box_y])
    screen.blit(wheel_image1, [box_x+450, box_y])
    screen.blit(wheel_image1, [box_x+525, box_y])
    
    # -- loop the bitcoin on the conveyor when it hits the wall --
    box2_go = True
    if box_x2 > (screen_width - 120) or box_x2 < 0:
      box_x2 =0
      
    if box2_go:
      box_x2 += box_x2_velocity

    # Display the bitcoin on top of the conveyor
    screen.blit(bitcoin_image,[box_x2, box_y2])
    
    # Draw the box for the text message with Grey color
    pygame.draw.rect(screen, GREY,[0,435 , 750, 200],0)
    
    # Limit to 20 frames per second
    clock.tick(20)
    
    # ---- All the TEXT messages ---------
      
    text2 = font.render("Bitcoin Simulation. Catch as much coin as possible.", True, WHITE)
    screen.blit(text2, [10, 450])
    
    text8 = font.render("Press the LEFT Arrow key to walk to the left.", True, WHITE)
    screen.blit(text8, [10, 475])

    text7 = font.render("Press the RIGHT Arrow key to walk to the right.", True, WHITE)
    screen.blit(text7, [10, 500])

    text6 = font.render("Press the SPACE key to jump, or with RIGHT or LEFT key to side jump.", True, WHITE)
    screen.blit(text6, [10, 525])

    text9 = font.render("Press the UP key to move up and DOWN key to move down.", True, WHITE)
    screen.blit(text9, [10, 550])

        
    # ------- End Danielle

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
   
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
