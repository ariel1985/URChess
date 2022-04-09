"""
Will represent an auto/ai player



https://python-chess.readthedocs.io/en/latest/
"""

import chess

board = chess.Board()

print(board)


# generate board fen string
board2 = chess.Board('r1bqkb1r/pppp1Qpp/2n2n2/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4')
print(board2)

print(chess.STARTING_FEN)