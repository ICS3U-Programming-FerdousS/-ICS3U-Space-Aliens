# Created By: Ferdous Sediqi
# Created on: June 2022

# import game
import ugame 
# import stage
import stage 

# import constant file
import constants

def menu_scene():
  # add background image
  image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
  # array for text
  text = []
  # set style the text 
  text1 = stage.Text(width = 29, height = 12, font = None, palette = constants.NEW_PALETTE, buffer = None)
  text1.move(20, 10)
  text1.text("MT Game Studios")
  text.append(text1)
  # set the text style 
  text2 = []
  text2 = stage.Text(width = 29, height = 12, font = None, palette = constants.NEW_PALETTE, buffer = None)
  text2.move(40, 110)
  text2.text("PRESS START BUTTON")
  text.append(text2)
  
  # sets background to image 0 and image bank
  background = stage.Grid(image_bank_mt_background, 10, 8)  
  # creating stage background
  game = stage.Stage(ugame.display, constants.FPS)
  game.layers = [text] + [background]
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

    # set background image
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    ship = stage.Sprite(image_bank_sprite, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))
    alien = stage.Sprite(image_bank_sprite, 9, int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2), 16)

    # create stage for the background
    game = stage.Stage(ugame.display, constants.FPS)
    # set layers for all sprites
    game.layers = [ship] + [alien] + [background]
    game.render_block()

    # looping the scene
    while True:
        # get user response from pressing buttons and change the x and y axis
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_X != 0:
            # check the state of button a
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
                print("Pressed B")
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]   
        if keys & ugame.K_O != 0:
            pass
        if keys & ugame.K_START != 0:
            pass
        if keys & ugame.K_SELECT != 0:
            pass
        if keys & ugame.K_RIGHT != 0:
        # if statment to not let ship got out of screen
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + 1, ship.y)
                print("Right")
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
        if keys & ugame.K_LEFT != 0:
        # if statment to not let ship got out of screen
            if ship.x >= 0:
                ship.move((ship.x - constants.SPRITE_MOVEMENT_SPEED), ship.y)
                print("Left")
            else:
                ship.move(0, ship.y)
        if keys & ugame.K_UP != 0:
            pass
        if keys & ugame.K_DOWN != 0:
            pass
        # if button is pressed keep play the sound
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)
        # render gqme
        game.render_sprites([alien] + [ship])
        game.tick()

if __name__ == "__main__":
    menu_scene()
