from flask import Flask, render_template, redirect, url_for, request, session
from flask_session import Session
from tempfile import mkdtemp
from wincheck import check
from ai import empty_moves, win_board, minimax
from copy import deepcopy

app = Flask(__name__)

app.config['SESSION_FILE_DIR'] = mkdtemp()
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    """ Render game board with GET request. Reset game board for a POST request."""

    if (request.method == 'POST'):
        session['board'] = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        session['moves'] = []
        session['turn'] = 'X'
        session['win'] = False
        session['winner'] = ''
        session['best_move'] = -1

    if 'board' not in session:
        session['board'] = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        session['turn'] = 'X'
        session['moves'] = []
        session['win'] = False
        session['winner'] = ''
        session['best_move'] = -1

    game = session['board']
    # winner = None

    win = session['win']

    counter = 0
    for square in game:
        print(square, ' ', end='')
        counter += 1
        if (counter % 3) == 0:
            print('\n')

    print('Winning board: ', win)
    return render_template('game.html', game=session['board'], turn=session['turn'], moves=session['moves'], win=session['win'], winner=session['winner'], best_move=session['best_move'])


@app.route("/play/<int:row>")
def play(row):
    """ Update the game board """

    game = session['board']
    game[row] = session['turn']

    session['board'] = game
    session['winner'] = session['turn']
    session['win'] = win_board(game, session['turn'])

    if (session['turn'] == 'X'):
        session['turn'] = 'O'
    else:
        session['turn'] = 'X'

    session['moves'].append(row)

    print('Moves list: ', session['moves'])
    print(game)
    print('play turn', session['turn'])
    print('Moves left:', empty_moves(game))
    return redirect(url_for('index'))


@app.route('/undo')
def undo():
    """ Undo the last move """

    game = session['board']
    moves = session['moves']

    if len(moves) > 0:
        last = moves[-1]
        game[last] = last
        if session['turn'] == 'X':
            session['turn'] = 'O'
        else:
            session['turn'] = 'X'

        del moves[-1]

    return redirect(url_for('index'))


@app.route('/ai')
def ai():
    """ Find best next move """
    turn = deepcopy(session['turn'])
    game = deepcopy(session['board'])

    moves = []

    print('Moves left:', empty_moves(game))

    minimax(game, turn, moves)

    print('Best moves: ', moves)

    if turn == 'X':
        best_moves_ordered = sorted(moves, key=lambda x: list(x.values()), reverse=True)
        if len(moves) >= 0:
            for item in best_moves_ordered[0].keys():
                session['best_move'] = item
    if turn == 'O':
        best_moves_ordered = sorted(moves, key=lambda x: list(x.values()))
        if len(moves) >= 0:
            for item in best_moves_ordered[0].keys():
                session['best_move'] = item


    print('Best moves ordered: ', best_moves_ordered)
    print('Best move BOX: ', session['best_move'])

    return redirect(url_for('index'))
