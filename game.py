import pygame as pyg
from pygame.locals import *


class PokemonClass:
    """
    Initialising the class with HP points, movement, speed, name, level and exp points attributed to a pokemon
    the speed attribute will decide how many pixels the sprite will move when a direction key is pressed
    """
    def __init__(self, hp: int, movement: str, speed: int, name: str, lvl: int, exp: int, win_size: tuple):
        self.hp = hp
        self.movement = movement
        self.speed = speed
        self.name = name
        self.lvl = lvl
        self.exp = exp
        self.win_size = win_size

        # initializing pygame
        pyg.init()
        self.screen = pyg.display.set_mode(win_size)  # setting window size
        pyg.display.set_caption("Classified project(or maybe not)")

    # The PokemonState func. will log the stats
    def PokemonState(self):
        print(
            "Your pokemon has ", self.hp,
            "HP" "\nYour pokemon has ", self.movement,
            "\nYour pokemon is called ", self.name,
            "\nYour pokemon is level ", self.lvl,
            "\nYour pokemon has ", self.exp, " exp",
        )

    """
    x, y are the starting position of the charcter
    width and height indicate sprite width and height
    """
    def run_game(self, width: int, height: int):
        x = (self.win_size[0]//2) - (width//2)  # center x position
        y = (self.win_size[1]//2) - (height//2)  # center y position
        screen = self.screen

        player = pyg.image.load("resources/sprite.png")  # loading sprite

        while True:
            pyg.time.delay(100)

            # defining controls
            # self.speed is how many pixels the sprite will move upon keypress
            keys = pyg.key.get_pressed()

            if keys[pyg.K_w] or keys[pyg.K_UP]:
                y -= self.speed
            elif keys[pyg.K_s] or keys[pyg.K_DOWN]:
                y += self.speed
            elif keys[pyg.K_d] or keys[pyg.K_RIGHT]:
                x += self.speed
            elif keys[pyg.K_a] or keys[pyg.K_LEFT]:
                x -= self.speed

            screen.fill(0)  # clearing screen
            screen.blit(player, (x, y))  # loads and displays the sprite at (x, y)
            pyg.display.flip()

            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    print("Terminating game...")
                    pyg.quit()


Pikachu = PokemonClass(100, "Thunderbolt", 5, "Pikachu", 10, 50, (500, 500))
Pikachu.PokemonState()
Pikachu.run_game(20, 20)
