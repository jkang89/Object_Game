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

GAME_WIDTH = 16
GAME_HEIGHT = 12

#### Put class definitions here ####
class Rock(GameElement):
    IMAGE = "Rock"
    SOLID = True

class Trees(GameElement):
    IMAGE = "ShortTree"
    SOLID = True

class Walls(GameElement):
    IMAGE = "Wall"
    SOLID = True

class Chests(GameElement):
    IMAGE = "Chest"
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

class NPC(GameElement):
    # if defeated != True: #Make defeated 
    #     SOLID = True
    # else:
    #     SOLID = False
    SOLID = True

class Blue_NPC(NPC):
    IMAGE = "Princess"

class Green_NPC(NPC):
    IMAGE = "Boy"

class Orange_NPC(NPC):
    IMAGE = "Horns"

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

    blue_gem_positions = [
        (0,3),
        (0,6),
        (0,11),
        (3,0),
        (8,0),
        (8,2),
        (9,8),
        (12,0),
        (15,1),
        (15,3)
        ]

    blue_gems = []

    for pos in blue_gem_positions:
        blue_gem = BlueGem()
        GAME_BOARD.register(blue_gem)
        GAME_BOARD.set_el(pos[0], pos[1], blue_gem)
        blue_gems.append(blue_gem)


    green_gem_positions = [
        (4,8),
        (6,2),
        (8,11),
        (9,3),
        (13,1)
        ]

    green_gems = []

    for pos in green_gem_positions:
        green_gem = GreenGem()
        GAME_BOARD.register(green_gem)
        GAME_BOARD.set_el(pos[0], pos[1], green_gem)
        green_gems.append(green_gem)


    orange_gem_positions = [
        (1,5),
        (5,5),
        (11,5),
        (12,8)
        ]

    orange_gems = []

    for pos in orange_gem_positions:
        orange_gem = OrangeGem()
        GAME_BOARD.register(orange_gem)
        GAME_BOARD.set_el(pos[0], pos[1], orange_gem)
        orange_gems.append(orange_gem)
    
    rock_positions = [
        (0,4),
        (1,3),
        (1,11),
        (2,0),
        (3,9),
        (3,7),
        (5,9),
        (5,7),
        (5,6),
        (6,3),
        (7,3),
        (8,7),
        (11,4),
        (12,9),
        (13,4),
        (15,6),
        (15,8)
        ]

    rocks = []

    for pos in rock_positions:
        rock = Rock()
        GAME_BOARD.register(rock)
        GAME_BOARD.set_el(pos[0], pos[1], rock)
        rocks.append(rock)

    tree_positions = [
        (0,5),
        (1,10),
        (1,6),
        (1,4),
        (4,0),
        (4,5),
        (6,5),
        (7,2),
        (11,2),
        (11,7),
        (11,9),
        (13,8),
        (14,10),
        (14,4),
        (15,5)
        ]

    trees = []

    for pos in tree_positions:
        tree = Trees()
        GAME_BOARD.register(tree)
        GAME_BOARD.set_el(pos[0], pos[1], tree)
        trees.append(tree)

    wall_positions = [
        (2,1),
        (5,2),
        (7,1),
        (7,10),
        (7,11),
        (8,3),
        (9,1),
        (9,4),
        (9,10),
        (9,11),
        (10,2),
        (10,3),
        (10,4),
        (11,0),
        (11,3),
        (11,6),
        (11,8),
        (12,1)
        ]

    walls = [] 

    for pos in wall_positions:
        wall = Walls()
        GAME_BOARD.register(wall)
        GAME_BOARD.set_el(pos[0], pos[1], wall)
        walls.append(wall)

    chest_positions = [
        (2,4),
        (3,8),
        (3,11),
        (4,3),
        (4,7),
        (5,0),
        (5,8),
        (5,11),
        (7,7),
        (7,9),
        (8,4),
        (8,6),
        (9,7),
        (11,1),
        (11,10),
        (11,11),
        (14,1),
        (14,6),
        (15,0)
        ]

    chests = []

    for pos in chest_positions:
        chest = Chests()
        GAME_BOARD.register(chest)
        GAME_BOARD.set_el(pos[0], pos[1], chest)
        chests.append(chest)

    Blue_NPC_positions = [
        (0,2),
        (0,7),
        (0,10),
        (3,1)
        ]

    Blue_NPCs = []

    for pos in Blue_NPC_positions:
        blue_npc = Blue_NPC()
        GAME_BOARD.register(blue_npc)
        GAME_BOARD.set_el(pos[0], pos[1], blue_npc)
        Blue_NPCs.append(blue_npc)

    Green_NPC_positions = [
        (4,9),
        (6,1),
        (8,10),
        (9,2),
        (13,2)
        ]

    Green_NPCs = []

    for pos in Green_NPC_positions:
        green_npc = Green_NPC()
        GAME_BOARD.register(green_npc)
        GAME_BOARD.set_el(pos[0], pos[1], green_npc)
        Green_NPCs.append(green_npc)

    Orange_NPC_positions = [
        (2,5),
        (5,4),
        (10,5),
        (12,5),
        (12,7)
        ]

    Orange_NPCs = []

    for pos in Orange_NPC_positions:
        orange_npc = Orange_NPC()
        GAME_BOARD.register(orange_npc)
        GAME_BOARD.set_el(pos[0], pos[1], orange_npc)
        Orange_NPCs.append(orange_npc)

    global PLAYER
    PLAYER = Character()
    GAME_BOARD.register(PLAYER)
    GAME_BOARD.set_el(0,0, PLAYER)
    print PLAYER

    GAME_BOARD.draw_msg("This game is wicked awesome.")
    
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

