import core
import pyglet
from pyglet.window import key
from core import GameElement
import sys

#### DO NOT TOUCH ####
GAME_BOARD = None
DEBUG = False
KEYBOARD = None
PLAYER = None
######################

GAME_WIDTH = 7
GAME_HEIGHT = 7

#### Put class definitions here ####
class Rock(GameElement):
    IMAGE = "Rock"
    SOLID = True

class Character(GameElement):
    IMAGE = "Cat"
    def __init__(self):
        GameElement.__init__(self)
        self.inventory = []

    def next_pos(self, direction):
        if direction == "up":
            return (self.x, self.y-1)
        elif direction == "down":
            return (self.x, self.y+1)
        elif direction == "left":
            return (self.x-1, self.y)
        elif direction == "right":
            return (self.x+1, self.y)
        return None

class Gem(GameElement):
    SOLID = False

    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("You just acquired a gem!  You have %d items!" % (len(player.inventory)))

class BlueGem(Gem):
    IMAGE = "BlueGem"

class GreenGem(Gem):
    IMAGE = "GreenGem"

class OrangeGem(Gem):
    IMAGE = "OrangeGem"

 
####   End class definitions    ####



def initialize():
    """Put game initialization code here"""
    
    rock_positions = [
        (2,1),
        (1,2),
        (3,2),
        (2,3),
        ]

    rocks = []

    for pos in rock_positions:
        rock = Rock()
        GAME_BOARD.register(rock)
        GAME_BOARD.set_el(pos[0], pos[1], rock)
        rocks.append(rock)

    rocks[-1].SOLID = False

    for rock in rocks:
        print rock

    global PLAYER
    PLAYER = Character()
    GAME_BOARD.register(PLAYER)
    GAME_BOARD.set_el(2,2, PLAYER)
    print PLAYER

    GAME_BOARD.draw_msg("This game is wicked awesome.")

    blue_gem = BlueGem()
    GAME_BOARD.register(blue_gem)
    GAME_BOARD.set_el(3, 1, blue_gem)

    green_gem = GreenGem()
    GAME_BOARD.register(green_gem)
    GAME_BOARD.set_el(0, 4, green_gem)

    orange_gem = OrangeGem()
    GAME_BOARD.register(orange_gem)
    GAME_BOARD.set_el(2, 4, orange_gem)

def keyboard_handler():  
    direction = None

    if KEYBOARD[key.UP]:
        GAME_BOARD.draw_msg("You pressed up")
        direction = "up"
    elif KEYBOARD[key.LEFT]:
        GAME_BOARD.draw_msg("You pressed left")
        direction = "left"
    elif KEYBOARD[key.RIGHT]:
        GAME_BOARD.draw_msg("You pressed right")
        direction = "right"
    elif KEYBOARD[key.DOWN]:
        GAME_BOARD.draw_msg("You pressed down")
        direction = "down"
       
    if direction:
        next_location = PLAYER.next_pos(direction)
        next_x = next_location[0]
        next_y = next_location[1]

        if next_x >= GAME_WIDTH  or next_x <= -1:
            next_x = PLAYER.x

        if next_y >= GAME_HEIGHT or next_y <= -1:
            next_y = PLAYER.y
        

        existing_el = GAME_BOARD.get_el(next_x, next_y)

        if existing_el:
            existing_el.interact(PLAYER)

        if existing_el is None or not existing_el.SOLID:
            GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
            GAME_BOARD.set_el(next_x, next_y, PLAYER)

