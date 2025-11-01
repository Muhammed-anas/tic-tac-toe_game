import React, { useState, useEffect } from 'react';
import './TicTacToe.css';

const TicTacToe = () => {
  const [board, setBoard] = useState(Array(9).fill(null));
  const [isXNext, setIsXNext] = useState(true);
  const [winner, setWinner] = useState(null);
  const [isDraw, setIsDraw] = useState(false);
  const [scores, setScores] = useState({ X: 0, O: 0, Draw: 0 });
  const [winningLine, setWinningLine] = useState([]);

  const checkWinner = (squares) => {
    const lines = [
      [0, 1, 2], [3, 4, 5], [6, 7, 8], // rows
      [0, 3, 6], [1, 4, 7], [2, 5, 8], // columns
      [0, 4, 8], [2, 4, 6]              // diagonals
    ];

    for (let i = 0; i < lines.length; i++) {
      const [a, b, c] = lines[i];
      if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
        setWinningLine([a, b, c]);
        return squares[a];
      }
    }
    return null;
  };

  const checkDraw = (squares) => {
    return squares.every(square => square !== null) && !checkWinner(squares);
  };

  const handleClick = (index) => {
    if (board[index] || winner || isDraw) {
      return;
    }

    const newBoard = board.slice();
    newBoard[index] = isXNext ? 'X' : 'O';
    setBoard(newBoard);
    setIsXNext(!isXNext);

    const gameWinner = checkWinner(newBoard);
    if (gameWinner) {
      setWinner(gameWinner);
      setScores(prev => ({
        ...prev,
        [gameWinner]: prev[gameWinner] + 1
      }));
    } else if (checkDraw(newBoard)) {
      setIsDraw(true);
      setScores(prev => ({
        ...prev,
        Draw: prev.Draw + 1
      }));
    }
  };

  const resetGame = () => {
    setBoard(Array(9).fill(null));
    setIsXNext(true);
    setWinner(null);
    setIsDraw(false);
    setWinningLine([]);
  };

  const resetScores = () => {
    setScores({ X: 0, O: 0, Draw: 0 });
    resetGame();
  };

  const renderSquare = (index) => {
    const isWinning = winningLine.includes(index);
    return (
      <button
        className={`square ${isWinning ? 'winning' : ''} ${board[index] ? `filled-${board[index].toLowerCase()}` : ''}`}
        onClick={() => handleClick(index)}
        disabled={!!winner || !!isDraw}
      >
        {board[index] && (
          <span className={`symbol ${board[index] === 'X' ? 'symbol-x' : 'symbol-o'}`}>
            {board[index]}
          </span>
        )}
      </button>
    );
  };

  const getStatus = () => {
    if (winner) {
      return `🎉 Player ${winner} Wins!`;
    }
    if (isDraw) {
      return `🤝 It's a Draw!`;
    }
    return `Player ${isXNext ? 'X' : 'O'}'s Turn`;
  };

  return (
    <div className="tic-tac-toe-container">
      <div className="game-header">
        <h1 className="game-title">Tic Tac Toe</h1>
        <p className="game-subtitle">Modern Edition</p>
      </div>

      <div className="scoreboard">
        <div className="score-item">
          <div className="score-label">Player X</div>
          <div className="score-value">{scores.X}</div>
        </div>
        <div className="score-item">
          <div className="score-label">Draws</div>
          <div className="score-value">{scores.Draw}</div>
        </div>
        <div className="score-item">
          <div className="score-label">Player O</div>
          <div className="score-value">{scores.O}</div>
        </div>
      </div>

      <div className="status-message">{getStatus()}</div>

      <div className="board">
        <div className="board-row">
          {renderSquare(0)}
          {renderSquare(1)}
          {renderSquare(2)}
        </div>
        <div className="board-row">
          {renderSquare(3)}
          {renderSquare(4)}
          {renderSquare(5)}
        </div>
        <div className="board-row">
          {renderSquare(6)}
          {renderSquare(7)}
          {renderSquare(8)}
        </div>
      </div>

      <div className="controls">
        <button className="btn btn-primary" onClick={resetGame}>
          New Game
        </button>
        <button className="btn btn-secondary" onClick={resetScores}>
          Reset Scores
        </button>
      </div>
    </div>
  );
};

export default TicTacToe;

