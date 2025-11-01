class TicTacToe:
    def __init__(self):
        print("Welcome to the Tic Tac Toe game!")
        self.board = [" "] * 9
        self.player = "X"
        self.winner = None
        self.score = {"X": 0, "O": 0}

    def display_board(self):
        print(f"\n{self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("_" * 9)
        print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("_" * 9)
        print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}")
        print()

    def player_move(self):
        try:
            move = int(input(f"Player {self.player}, enter your move (1-9): "))
            if 1 <= move <= 9 and self.board[move - 1] == " ":
                self.board[move - 1] = self.player
            elif 1 <= move <= 9:
                print("That spot is already taken, try again.")
                self.player_move()
            else:
                print("Invalid number, choose between 1 and 9.")
                self.player_move()
        except ValueError:
            print("Please enter a valid number.")
            self.player_move()

    def switch_player(self):
        self.player = "O" if self.player == "X" else "X"

    def check_winner(self):
        combos = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontal
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertical
            (0, 4, 8), (2, 4, 6)              # diagonal
        ]

        for a, b, c in combos:
            if self.board[a] == self.board[b] == self.board[c] != " ":
                self.winner = self.board[a]
                return True
        return False

    def check_tie(self):
        return " " not in self.board and self.winner is None

    def update_score(self):
        if self.winner:
            self.score[self.winner] += 1
            print(f"Player {self.winner} wins! Current score: {self.score}")

    def reset_board(self):
        self.board = [" "] * 9
        self.winner = None
        self.player = "X"

    def play_game(self):
        while True:
            self.display_board()
            self.player_move()

            if self.check_winner():
                self.display_board()
                self.update_score()
                break

            if self.check_tie():
                self.display_board()
                print("It's a tie!")
                break

            self.switch_player()

    def play_again(self):
        while True:
            self.play_game()
            again = input("Do you want to play again? (y/n): ").lower()
            if again == "y":
                self.reset_board()
            else:
                print("Thanks for playing! Final scores:")
                print(self.score)
                break


if __name__ == "__main__":
    game = TicTacToe()
    game.play_again()
