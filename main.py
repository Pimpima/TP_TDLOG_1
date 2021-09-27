# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Tile():
    def __init__(self, bool #bool, tile_type #int, tile_orientation #int):
        Tile._static = bool
        Tile.type = tile_type
        Tile.orientation = tile_orientation
    def rotate(self):
        Tile.orientation = (Tile.orientation +1)%4




# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    T = Tile(True, 0, 0)
    print_hi('PyCharm')
