# Created By: Ferdous Sediqi
# created in : June. 2022

# import game
import ugame 
# import stage
import stage 

# function for main scene of the game
def game_scene():
    
    # import the background image
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")

    image_bank_sprite = stage.Bank.from_bmp16("space_aliens.bmp")


    # set background image
    background = stage.Grid(image_bank_background, 10, 8)
    ship = stage.Sprite(image_bank_sprite, 5, 75, 66)

    # create stage for the background
    game = stage.Stage(ugame.display, 60)
    # set layers for all sprites
    game.layers = [ship] + [background]
    game.render_block()

    # looping the scene
    while True:
        pass
        game.render_sprites([ship])
        game.tick()

if __name__ == "__main__":
    game_scene()
