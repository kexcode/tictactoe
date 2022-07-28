from tictactoe import Cell, Board

print('Hi!')

board = Board()

board.state()


board.play_at_position(1)
board.play_at_position(2)
board.play_at_position(3)
board.play_at_position(5)
board.play_at_position(7)
current_move = int(input('Please select the position you want to play:  '))
board.play_at_position(current_move)
current_move = int(input('Please select the position you want to play:  '))
board.play_at_position(current_move)
current_move = int(input('Please select the position you want to play:  '))
board.play_at_position(current_move)