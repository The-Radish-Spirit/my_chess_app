#define a class for squares on the board
class board_square(object):
    def __init__(self, coordinate_x, coordinate_y):
        self.coordinates = (coordinate_x,coordinate_y)
        self.occupied = False
        self.occupant = None
#define a class for a 64 square board
class board_64(object):

    #define funtion to initialize 8x8 board square array
    def __init__(self):
        self.board_array = []
        self.board_dim_x = 8
        self.board_dim_y = 8
        for i in range(0,self.board_dim_x):
            col= []
            for j in range(0,self.board_dim_y):
                col.append(board_square(i,j))
            self.board_array.append(col)

"""
#create an instance of our board
game_board = board_64()

#test board contents
for i in range(0,8):
    for j in range(0,8):
        print(game_board.board_array[i][j].coordinates)
"""
