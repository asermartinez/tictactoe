import math


def empty_moves(game):
    """TODO: Docstring for moves.
    """
    moves = []
    for item in game:
        if item == 'X' or item == 'O':
            pass
        else:
            moves.append(item)
    return moves

def win_board(game, turn):
    """TODO: Docstring for win_board.
    """
    if ((game[0] == turn and game[1] ==  turn and game[2] == turn) or
       (game[3] == turn and game[4] ==  turn and game[5] == turn) or
       (game[6] == turn and game[7] ==  turn and game[8] == turn) or
       (game[0] == turn and game[3] ==  turn and game[6] == turn) or
       (game[1] == turn and game[4] ==  turn and game[7] == turn) or
       (game[2] == turn and game[5] ==  turn and game[8] == turn) or
       (game[0] == turn and game[4] ==  turn and game[8] == turn) or
       (game[2] == turn and game[4] ==  turn and game[6] == turn) ):
        return True
    else:
        return False
    # elif (len(empty_moves(game)) == 0):
    #     return False
    #
def minimax(game, turn, moves):
    """TODO: Docstring for minimax.
    """
    moves_left = empty_moves(game)

    new_game = game
    if turn == 'X':
        for i in moves_left:
            value = -math.inf
            new_game[i] = turn
            if len(empty_moves(game)) == 0:
                move = {i : 10}
                moves.append(move)
                return 0
            if win_board(new_game, turn):
                move = {i : 10}
                moves.append(move)
                return 10
            value = max(value, minimax(new_game, 'O', moves))
            move = {i : value}
            moves.append(move)
    elif turn == 'O':
        for i in moves_left:
            value = math.inf
            new_game[i] = turn
            if len(empty_moves(game)) == 0:
                move = {i : -10}
                moves.append(move)
                return 0
            if win_board(new_game, turn):
                move = {i : -10}
                moves.append(move)
                return -10
            value = min(value, minimax(new_game, 'X', moves))
            move = {i : value}
            moves.append(move)

    return value

# human_player = 'X'
# ai_player = 'O'
# turn = ai_player
# moves = []
# move = {}
# print('moves left:', empty_moves(game))
# minimax(game, turn)
# print(moves[0])
# for item in moves[0].keys():
#     best_move_index = item
# print(best_move_index)
