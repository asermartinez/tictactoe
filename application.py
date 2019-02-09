from flask import Flask, render_template, redirect, url_for, request, session
from flask_session import Session
from tempfile import mkdtemp

app = Flask(__name__)

app.config['SESSION_FILE_DIR'] = mkdtemp()
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    """ Render game board with GET request. Reset game board for a POST request."""

    if (request.method == 'POST'):
        session['board'] = [[None, None, None], [None, None, None], [None, None, None]]
        session['moves'] = []
        session['turn'] = 'X'

    if 'board' not in session:
        session['board'] = [[None, None, None], [None, None, None], [None, None, None]]
        session['turn'] = 'X'
        session['moves'] = []

    game = session['board']
    winner = None

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

    for row in session['board']:
        print(row)
    print(winner)
    return render_template('game.html', game=session['board'], turn=session['turn'], moves=session['moves'], winner=winner)


@app.route("/play/<int:row>/<int:col>")
def play(row, col):
    """ Update the game board """

    game = session['board']
    game[row][col] = session['turn']

    if (session['turn'] == 'X'):
        session['turn'] = 'O'
    else:
        session['turn'] = 'X'

    session['last_move'] = []
    session['last_move'].append(row)
    session['last_move'].append(col)

    session['moves'].append(session['last_move'])

    for item in session['moves']:
        print(item)

    print(game)
    return redirect(url_for('index'))


@app.route('/undo')
def undo():
    """ Undo the last move """

    game = session['board']
    moves = session['moves']

    if len(moves) > 0:
        last = moves[-1]
        game[last[0]][last[1]] = None
        del moves[-1]

    return redirect(url_for('index'))























