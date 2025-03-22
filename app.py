from flask import Flask, render_template, request, redirect, url_for
import tictactoe as ttt

app = Flask(__name__)

# Initialize the game board
board = ttt.initial_state()
ai_turn = False

@app.route("/")
def index():
    """Render the main game page."""
    global board, ai_turn
    winner = ttt.winner(board)
    game_over = ttt.terminal(board)

    if not game_over and ai_turn:
        # AI's turn
        move = ttt.minimax(board)
        board = ttt.result(board, move)
        ai_turn = False
        return redirect(url_for("index"))

    return render_template("index.html", board=board, winner=winner, game_over=game_over)

@app.route("/move", methods=["POST"])
def move():
    """Handle player moves."""
    global board, ai_turn
    if not ttt.terminal(board):
        row = int(request.form["row"])
        col = int(request.form["col"])
        if (row, col) in ttt.actions(board):
            board = ttt.result(board, (row, col))
            ai_turn = True
    return redirect(url_for("index"))

@app.route("/reset")
def reset():
    """Reset the game."""
    global board, ai_turn
    board = ttt.initial_state()
    ai_turn = False
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
