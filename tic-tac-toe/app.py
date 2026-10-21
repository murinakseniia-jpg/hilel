import random
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def check_winner(board):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), 
        (0, 3, 6), (1, 4, 7), (2, 5, 8), 
        (0, 4, 8), (2, 4, 6)
        ]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] != "":
            return board[a]
    if "" not in board:
        return "draw" 


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/computer-move", methods=["POST"])
def computer_move():
    board = request.json["board"]
    winner  = check_winner(board)
    if winner:
        return jsonify({"board": board, "winner": winner})
    empy_cells = [i for i in range(9) if board[i] == ""]
    if empy_cells:
        computer_choice = random.choice(empy_cells)
        board[computer_choice] = "O"
    winner = check_winner(board)
    return jsonify({"board": board, "winner": winner})

if __name__ == "__main__":
    app.run(debug=True)

# http://127.0.0.1:5000