import numpy as np


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Tile:
    '''Tile class : corresponds to a piece of the game with several exits
    (2,3 or 4) that can rotate or move if it is not static'''
    def __init__(self, tile_bool:bool = False, tile_type:int = 0,tile_orientation:int = 0):
        '''The tile is initialized by being static or dynamic (bool), by choosing a type of tile
        (there are 3 different types) and a rotation of the tile ; we have chosen a reference side of each tile.'''
        Tile._static = tile_bool
        Tile.type = tile_type
        Tile.orientation = tile_orientation
    def rotate(self):
        '''This function rotates the tile of 90° clockwise'''
        Tile.orientation = (Tile.orientation +1)%4



class Board:



class Object:
    object_list=["book", "emerald", "gold", "key ring", "map", "owl", "ring", "sword"]
    def __init__(self, object_type=0 '''int in {0,..,7}'''):
        Object.object=object_list[object_type]



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    T = Tile(True, 0, 0)


