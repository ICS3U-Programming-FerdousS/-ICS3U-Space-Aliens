# Created By: Ferdous Sediqi
# Created on: June 2022

# import game
import ugame 
# import stage
import stage 

# import constant file
import constants

# function for main scene of the game
def game_scene():
    
    # import the background image
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")

    image_bank_sprite = stage.Bank.from_bmp16("space_aliens.bmp")


    # set background image
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    ship = stage.Sprite(image_bank_sprite, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))

    # create stage for the background
    game = stage.Stage(ugame.display, constants.FPS)
    # set layers for all sprites
    game.layers = [ship] + [background]
    game.render_block()

    # looping the scene
    while True:
        # get user response from pressing buttons and change the x and y axis
        keys = ugame.buttons.get_pressed()
        if keys & ugame.K_X:
            pass
        if keys & ugame.K_O:
            pass
        if keys & ugame.K_START:
            pass
        if keys & ugame.K_SELECT:
            pass
        if keys & ugame.K_RIGHT:
        # if statment to not let ship got out of screen
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + 1, ship.y)
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
        if keys & ugame.K_LEFT:
        # if statment to not let ship got out of screen
            if ship.x >= 0:
                ship.move(ship.x - 1, ship.y)
            else:
                ship.move(0, ship.y)
        if keys & ugame.K_UP:
            pass
        if keys & ugame.K_DOWN:
            pass
        # render gqme
        game.render_sprites([ship])
        game.tick()

if __name__ == "__main__":
    game_scene()
