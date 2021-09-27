import numpy as np

class Tile:
    def __init__(self, bool '''bool''', tile_type #int, tile_orientation #int ):
        Tile._static = bool
        Tile.type = tile_type
        Tile.orientation = tile_orientation
    def rotate(self):
        Tile.orientation = (Tile.orientation +1)%4

class Object:
    object_list=["book", "emerald", "gold", "key ring", "map", "owl", "ring", "sword"]
    def __init__(self, object_type=0 '''int in {0,..,7}'''):
        Object.object=object_list[object_type]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    T = Tile(True, 0, 0)
    print_hi('PyCharm')

