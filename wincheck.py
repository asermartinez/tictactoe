def check(game, winner):
    """TODO: Docstring for check.
    :returns: TODO

    """
    # Check the board for winning combinations
    # Columns
    for col in range(3):
        if game[0][col] == 'X' and game[1][col] == 'X' and game[2][col] == 'X':
            winner = 'X'
        if game[0][col] == 'O' and game[1][col] == 'O' and game[2][col] == 'O':
            winner = 'O'

    # Rows
    for row in range(3):
        if game[row][0] == 'X' and game[row][1] == 'X' and game[row][2] == 'X':
            winner = 'X'
        if game[row][0] == 'O' and game[row][1] == 'O' and game[row][2] == 'O':
            winner = 'O'

    # Diagonal Starting Left
    for row in range(3):
        if game[0][0] == 'X' and game[1][1] == 'X' and game[2][2] == 'X':
            winner = 'X'
        if game[0][0] == 'O' and game[1][1] == 'O' and game[2][2] == 'O':
            winner = 'O'

    # Diagonal Starting Right
    if game[2][0] == 'X' and game[1][1] == 'X' and game[0][2] == 'X':
        winner = 'X'
    if game[2][0] == 'O' and game[1][1] == 'O' and game[0][2] == 'O':
        winner = 'O'

    return winner
