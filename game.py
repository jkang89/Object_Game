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
CONVERSATION_PARTNER = None
######################

GAME_WIDTH = 10
GAME_HEIGHT = 9

#### Put class definitions here ####
class Rock(GameElement):
    IMAGE = "Rock"
    SOLID = True

class ShortTrees(GameElement):
    IMAGE = "ShortTree"
    SOLID = True

class TallTrees(GameElement):
    IMAGE = "TallTree"
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
    SOLID = True

    def interact(self, player):
        global CONVERSATION_PARTNER
        CONVERSATION_PARTNER = self

        self.current_line = 0


class Princess_NPC(NPC):
    IMAGE = "Princess"
    LINES = ["Hello, welcome to our barren land. (Press SPACE to advance conversation.)",
             "Please answer this simple question to pass.",
             "Don't just button-mash. If you don't select the right answer, you'll have to start the conversation over.",
             "If you were running a race, and you pass the person in 2nd place, what place would you be in?",
             "a) First place    b) Second place     c) Third place      d) The best place"
             ]
    answer = "b"

class Boy_NPC(NPC):
    IMAGE = "Boy"
    LINES = ["'ello, luv.  Noice weather, we're havin'.",
            "You mind doin me a favuh, luv and answer me question?",
            "Tell me quickly, luv. What was da first 'uman organ ter be transferred from a cadaver ter a live 'uman?",
            "Is it: a) the heart        b) the liver        c) the kidney       d) the eyeball?"
            ]
    answer = "c"

class Girl_NPC(NPC):
    IMAGE = "Girl"
    LINES = ["I expected someone... smarter, but I suppose you'll have to do.",
            "All right then, answer me this.",
            "What is the definition of the term, anathema?",
            "Please choose wisely, and don't waste my time.",
            "Is the answer: a) a cursed, detested person     b) a medical procedure    c) an expression of ill will     d) readiness to believe"
            ]
    answer = "a"

class Christian_NPC(NPC):
    IMAGE = "Christian"
    LINES = ["Hey, brotimes.",
             "You made it this far. That's cool. (I guess.)",
             "Sooooooo, you get to guess my middle name today.",
             "If you don't get it, you fail at life.",
             "*Sweeps back hair.*",
             "What is my middle name?",
             "(Don't fuck this up.)",
             "Is it: a) Gross Garbage   b) Dr. Fishopolis   c) Zeppelin   d) None of the above"
            ]

    answer = "d"

class Horns_NPC(NPC):
    IMAGE = "Horns"
    LINES = ["Greetings, plebian.",
             "Congratulations making it thus far, but I'm afraid this is the end of your journey.",
             "*Diabolical laughter*",
             "Riddle me this: A farmer is trying to cross a river with a bag of corn, a hen, and a fox.  Did you write this down?",
             "The farmer's boat is only big enough to take himself and one other item per trip.",
             "The hen cannot be left alone with the corn or she will eat it.",
             "Likewise, the fox cannot be left alone with the hen, or the hen will be eaten.",
             "How many times does the farmer go from one back to the other?",
             "a) 3 moves      b) 5 moves       c) 7 moves      d) 10 moves"
            ]
    answer = "c"

class Gem(GameElement):
    SOLID = False

    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("You just acquired a gem!  You have %d items!" % (len(player.inventory)))

class BlueGem(Gem):
    IMAGE = "BlueGem"

class DoorClosed(GameElement):
    IMAGE = "DoorClosed"
    SOLID = True

 
####   End class definitions    ####



def initialize():
    """Put game initialization code here"""

    blue_gem_positions = [
        (3,0),
        (6,0),
        (1,2),
        (5,2),
        (4,4),
        (7,4),
        (2,6),
        (6,6),
        (3,8),
        (5,8)
        ]

    blue_gems = []

    for pos in blue_gem_positions:
        blue_gem = BlueGem()
        GAME_BOARD.register(blue_gem)
        GAME_BOARD.set_el(pos[0], pos[1], blue_gem)
        blue_gems.append(blue_gem)

    rock_positions = [
        (0,1),
        (1,1),
        (2,1),
        (3,1),
        (4,1),
        (5,1),
        (6,1),
        (7,1),
        (8,1)
        ]

    rocks = []

    for pos in rock_positions:
        rock = Rock()
        GAME_BOARD.register(rock)
        GAME_BOARD.set_el(pos[0], pos[1], rock)
        rocks.append(rock)

    shorttree_positions = [
        (1,3),
        (2,3),
        (3,3),
        (4,3),
        (5,3),
        (6,3),
        (7,3),
        (8,3),
        (9,3)
        ]

    shorttrees = []

    for pos in shorttree_positions:
        shorttree = ShortTrees()
        GAME_BOARD.register(shorttree)
        GAME_BOARD.set_el(pos[0], pos[1], shorttree)
        shorttrees.append(shorttree)

    wall_positions = [
        (0,5),
        (1,5),
        (2,5),
        (3,5),
        (4,5),
        (5,5),
        (6,5),
        (7,5),
        (8,5)
        ]

    walls = [] 

    for pos in wall_positions:
        wall = Walls()
        GAME_BOARD.register(wall)
        GAME_BOARD.set_el(pos[0], pos[1], wall)
        walls.append(wall)

    talltree_positions = [
        (1,7),
        (2,7),
        (3,7),
        (4,7),
        (5,7),
        (6,7),
        (7,7),
        (8,7),
        (9,7)
        ]

    talltrees = []

    for pos in talltree_positions:
        talltree = TallTrees()
        GAME_BOARD.register(talltree)
        GAME_BOARD.set_el(pos[0], pos[1], talltree)
        talltrees.append(talltree)

    princess_npc = Princess_NPC()
    GAME_BOARD.register(princess_npc)
    GAME_BOARD.set_el(9,1, princess_npc)

    christian_npc = Christian_NPC()
    GAME_BOARD.register(christian_npc)
    GAME_BOARD.set_el(0,7, christian_npc)

    girl_npc = Girl_NPC()
    GAME_BOARD.register(girl_npc)
    GAME_BOARD.set_el(0,3, girl_npc)

    boy_npc = Boy_NPC()
    GAME_BOARD.register(boy_npc)
    GAME_BOARD.set_el(9,5, boy_npc)

    horns_npc = Horns_NPC()
    GAME_BOARD.register(horns_npc)
    GAME_BOARD.set_el(8,8, horns_npc)

    doorclosed = DoorClosed()
    GAME_BOARD.register(doorclosed)
    GAME_BOARD.set_el(9,8, doorclosed)

    global PLAYER
    PLAYER = Character()
    GAME_BOARD.register(PLAYER)
    GAME_BOARD.set_el(0,0, PLAYER)
    print PLAYER


def engage_in_conversation():
    global CONVERSATION_PARTNER
    p = CONVERSATION_PARTNER
    line = p.LINES[p.current_line]
    GAME_BOARD.draw_msg(line)

    answer = None

    if KEYBOARD[key.SPACE]:
        p.current_line += 1
        if p.current_line >= len(p.LINES):
            p.current_line = len(p.LINES) - 1       
    elif KEYBOARD[key.A]:
        answer = "a"
        CONVERSATION_PARTNER = None
    elif KEYBOARD[key.B]:
        answer = "b"
        CONVERSATION_PARTNER = None
    elif KEYBOARD[key.C]:
        answer = "c"
        CONVERSATION_PARTNER = None
    elif KEYBOARD[key.D]:
        answer = "d"
        CONVERSATION_PARTNER = None

    if answer == p.answer:
        GAME_BOARD.del_el(p.x, p.y)


def keyboard_handler():  
    if CONVERSATION_PARTNER != None:
        engage_in_conversation()
        return

    direction = None

    if KEYBOARD[key.UP]:
        direction = "up"
    elif KEYBOARD[key.LEFT]:
        direction = "left"
    elif KEYBOARD[key.RIGHT]:
        direction = "right"
    elif KEYBOARD[key.DOWN]:
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

