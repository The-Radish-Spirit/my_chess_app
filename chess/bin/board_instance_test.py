#create an instance of our board
game_board = board_64()

#test board contents
def content_test():
    for i in range(0,8):
        for j in range(0,8):
            print(game_board.board_array[i][j].coordinates)

content_test()
