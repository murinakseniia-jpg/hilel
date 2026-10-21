const playButton = document.getElementById("play-tic-tac-toe");
const ticTacToeGame = document.getElementById("tic-tac-toe-game");
const ticTacToeIntro = document.getElementById("tic-tac-toe-intro");
const cells = document.querySelectorAll(".cell");
const restartButton = document.getElementById("restart-tic-tac-toe");

let gameOver = false;

playButton.addEventListener("click", function() {
    ticTacToeGame.hidden = false;
    ticTacToeIntro.hidden = true;
});

cells.forEach(function(cell) {
    cell.addEventListener("click", function() {
        if (cell.textContent !== "" || gameOver) return;
        cell.textContent = "X";
        const board = Array.from(cells, cell => cell.textContent);
        fetch("/computer-move", { 
            method: "POST", 
            headers: {"Content-Type": "application/json"}, 
            body: JSON.stringify({board: board}) })
        .then(response => response.json())
        .then(data => { data.board.forEach((value, i) => cells[i].textContent = value); return data; })
        .then(data => {const message = document.getElementById("game-message");
            if (data.winner === "X")
message.textContent = "You win!";
            else if (data.winner === "draw")
message.textContent = "It's a draw!"
            else if (data.winner === "O")
message.textContent = "Computer wins!"

            if (data.winner) gameOver = true;
         });
    });
});

restartButton.addEventListener("click", function() {
    cells.forEach(cell => cell.textContent = "");
    gameOver = false
    document.getElementById("game-message").textContent = "Your turn! Choose a square!"
});