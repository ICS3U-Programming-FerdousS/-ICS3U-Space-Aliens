# Created By: Ferdous Sediqi
# Created on: June 2022

import ugame
import stage
import constants
import time
import random 

# function for splash scene
def splash_scene():
    # add background sound file for splash scene
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)
      
    # add background image
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
 
    # sets background to image 0 and image bank
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_Y, constants.SCREEN_Y)

    # blank white   
    background.tile(2, 2, 0)  
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(12, 2, 0)  

    background.tile(2, 3, 0)  
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  

    background.tile(2, 4, 0)  
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  
    background.tile(2, 5, 0)  
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(12, 5, 0)
    background.tile(12, 5, 0) 

    # creating stage background
    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = [background]

    # render background
    game.render_block()
    # repeat the game forever
    while True:

        # run splash scene on the screen for 2 second then go to menu scene
        time.sleep(2.0)
        menu_scene()

def menu_scene():
    
  # add background image
  image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

  # list for text1
  text = []

  # set style the text 
  text1 = stage.Text(width = 29, height = 12, font = None, palette = constants.NEW_PALETTE, buffer = None)
  text1.move(20, 10)
  text1.text("MT Game Studios")

  # append company name  to text list
  text.append(text1)

  # set the text style 
  text2 = stage.Text(width = 29, height = 12, font = None, palette = constants.NEW_PALETTE, buffer = None)
  text2.move(10, 110)
  text2.text("PRESS START BUTTON")

  # append Start instruction button to text list
  text.append(text2)
  
  # sets background to image 0 and image bank
  background = stage.Grid(image_bank_mt_background, constants.SCREEN_X, constants.SCREEN_Y)  

  # creating stage background
  game = stage.Stage(ugame.display, constants.FPS)
  game.layers = text + [background]

  # render background
  game.render_block()

  # repeat the game forever
  while True:
    keys = ugame.buttons.get_pressed()

    # push the start button to start the game
    if keys & ugame.K_START != 0:
      game_scene()

    #redaw sprites  
    game.tick()

# function for main scene of the game
def game_scene():    

    # global variable to keep track of score
    score = 0

    # list for text1
    text = []

    # set style the text 
    scoreText = stage.Text(width = 80, height = 40, font = None, palette = constants.NEW_PALETTE, buffer = None)
    scoreText.move(5, 5)
    scoreText.text(str(score))
    text.append(scoreText)

    # this function place brings aliens on the screen
    def show_alien():
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x < 0:
                aliens[alien_number].move(random.randint(0 + constants.SPRITE_SIZE, constants.SCREEN_X - constants.SPRITE_SIZE), constants.OFF_TOP_SCREEN)
                break
    # import the background image
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")

    image_bank_sprite = stage.Bank.from_bmp16("space_aliens.bmp")

    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # importing sound file 
    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    boom_sound = open("boom.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    # set background image
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(1, 3)
            background.tile(x_location, y_location, tile_picked)
    ship = stage.Sprite(image_bank_sprite, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))

    aliens = []
    for alien_number in range(constants.TOTAL_NUMBER_OF_ALIENS):
        a_single_alien = stage.Sprite(image_bank_sprite, 9, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        aliens.append(a_single_alien)
    show_alien()
    # declare list for lasers
    lasers = []

    for lasers_number in range(constants.TOTAL_NUMBER_OF_LASERS):
        a_single_laser = stage.Sprite(image_bank_sprite, 10, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
    lasers.append(a_single_laser)

    # create stage for the background
    game = stage.Stage(ugame.display, constants.FPS)

    # set layers for all sprites
    game.layers = text + lasers +  [ship] + aliens + [background]
    game.render_block()

    # looping the scene
    while True:
        # get user response from pressing buttons and change the x and y axis
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_O != 0:
            # check the state of button a
            # print ("A pressed")
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]   
        if keys & ugame.K_X != 0:
            # print ("B pressed")
            pass
        if keys & ugame.K_START != 0:
            pass
        if keys & ugame.K_SELECT != 0:
            pass
        if keys & ugame.K_RIGHT != 0:
        # if statment to not let ship got out of screen
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + 1, ship.y)
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
        if keys & ugame.K_LEFT != 0:
        # if statment to not let ship got out of screen
            if ship.x >= 0:
                ship.move((ship.x - constants.SPRITE_MOVEMENT_SPEED), ship.y)
            else:
                ship.move(0, ship.y)
        if keys & ugame.K_UP != 0:
            pass
        if keys & ugame.K_DOWN != 0:
            pass
        # if A button is pressed keep play the sound and change laser positions
        if a_button == constants.button_state["button_just_pressed"]:
            for lasers_number in range(len(lasers)):
                if lasers[lasers_number].x < 0:
                    lasers[lasers_number].move(ship.x, ship.y)
                sound.play(pew_sound)
                break
        # loop to see if still have the laser to fire
        for lasers_number in range(len(lasers)):
            if lasers[lasers_number].x > 0:     
                lasers[lasers_number].move(lasers[lasers_number].x, lasers[lasers_number].y - constants.LASER_SPEED)
                if lasers[lasers_number].y < constants.OFF_TOP_SCREEN:
                    lasers[lasers_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)

        # loop to bring alliens on the screen and remove them back by changing their x and y values
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                aliens[alien_number].move(aliens[alien_number].x, aliens[alien_number].y + constants.ALIEN_SPEED)
            if aliens[alien_number].y > constants.SCREEN_Y:
                aliens[alien_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                show_alien()

        # for loop to check if lasers touches alliens and then add score
        for lasers_number in range(len(lasers)):
            if lasers[lasers_number].x > 0:
                for alien_number in range(len(aliens)):
                    if aliens[alien_number].x > 0:
                        if stage.collide(lasers[lasers_number].x + 6, lasers[lasers_number].y + 2, lasers[lasers_number].x + 11, lasers[lasers_number].y + 12, aliens[alien_number].x + 1, aliens[alien_number].y, aliens[alien_number].x + 15, aliens[alien_number].y + 15):
                            aliens[alien_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            lasers[lasers_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            sound.stop()
                            sound.play(boom_sound)
                            show_alien()
                            show_alien()
                            score = score + 1
                            print(score)  
                                                       
        # render the game
        game.render_sprites(lasers +  [ship] + aliens)
        game.tick()

if __name__ == "__main__":
    splash_scene()
