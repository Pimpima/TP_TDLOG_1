#Pierre-Marie CIRON & Joy-Rose DUNOYER
import numpy as np

object_list=["none","book", "emerald", "gold", "key ring", "map", "owl", "ring", "sword"]
class Object:
    '''It gives the object type as a character chain'''

    def __init__(self, object_type:int=0):
        '''Set the attribute object as the noun of the object and return "none" if it has no object'''
        Object.object = object_list[object_type]


class Tile:
    '''Tile class : corresponds to a piece of the game with several exits
    (2,3 or 4) that can rotate or move if it is not static'''
    def __init__(self, tile_bool:bool = False, tile_type:int = 0,tile_orientation:int = 0, has_object:Object=Object(0)):
        '''The tile is initialized by being static or dynamic (bool), by choosing a type of tile
        (there are 3 different types) and a rotation of the tile ; we have chosen a reference side of each tile.'''
        Tile.static = tile_bool
        Tile.type = tile_type
        Tile.orientation = tile_orientation
        Tile.object_in = has_object
        if not Tile.static:
            Tile.object_in = Object(0)
    def rotate(self):
        '''This function rotates the tile of 90° clockwise'''
        if not Tile.static:
            Tile.orientation = (Tile.orientation +1)%4




class Board:
    def __init__(self):
        Board.tile_position = []
        for lign in range(7):
            for col in range(7):
                t = Tile(False)
                Board.tile_position += [t]
        random_objects = np.random.permutation([1,2,3,4,5,6,7,8])

        #initialization of the static tiles with objects put randomly
        Board.tile_position[0]=Tile(True,2,1,Object(0))
        Board.tile_position[2] = Tile(True, 3, 2, Object(random_objects[0]))
        Board.tile_position[4] = Tile(True, 3, 2, Object(random_objects[1]))
        Board.tile_position[6]=Tile(True,2,2,Object(0))
        Board.tile_position[14] = Tile(True, 3, 1, Object(random_objects[2]))
        Board.tile_position[16]=Tile(True,4,0,Object(0))
        Board.tile_position[18]=Tile(True,4,0,Object(0))
        Board.tile_position[20] = Tile(True, 3, 3, Object(random_objects[3]))
        Board.tile_position[28] = Tile(True, 3, 1, Object(random_objects[4]))
        Board.tile_position[30] = Tile(True, 4, 0, Object(0))
        Board.tile_position[32] = Tile(True, 4, 0, Object(0))
        Board.tile_position[34] = Tile(True, 3, 3, Object(random_objects[5]))
        Board.tile_position[42] = Tile(True, 2, 0, Object(0))
        Board.tile_position[44] = Tile(True, 3, 0, Object(random_objects[6]))
        Board.tile_position[46] = Tile(True, 3, 0, Object(random_objects[7]))
        Board.tile_position[48] = Tile(True, 2, 3, Object(0))

        #we choose the position of the empty case
        pos=np.random.randint(49)
        while Board.tile_position[pos].static:
            pos =np.random.randint(49)
        Board.empty_position = pos #the position of the empty place should not be on a static tile

        #list of the dynamic tiles to put on the board randomly
        dynamic_tiles = [Tile(False,0,random(4),Object(0)) for k in range (12)]
        dynamic_tiles += [Tile(False, 1, random(4), Object(0)) for k in range(16)]
        dynamic_tiles += [Tile(False, 2, random(4), Object(0)) for k in range(6)]

        dynamic_tiles = np.random.permutation(dynamic_tiles)

        compt=0
        for k in range(49):
            if not Board.tile_position[k].static and k != Board.empty_position:
                Board.tile_position[k] = dynamic_tiles[compt]
                compt +=1





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    T = Tile(True, 0, 0)
    B=Board()



