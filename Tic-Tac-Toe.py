import os
from Player import Player
from Grid import Grid
from Menu import Menu


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class Game:
    def __init__(self):
        self.players = [Player(), Player()]
        self.board = Grid()
        self.menu = Menu()
        self.current_player_ind = 0

    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == "1":
            self.setup_players()
            self.play_game()
        else:
            self.end_game()

    def setup_players(self):
        for number, pl in enumerate(self.players, start=1):
            clear_screen()
            print(f"Player {number}, enter your details:")
            pl.choose_name()
            pl.choose_symbol()
            if number == 2:
                self.valid_symbol()
        clear_screen()

    def valid_symbol(self):
        while self.players[1].symbol == self.players[0].symbol:
            print(f"{self.players[1].name}, Please enter the correct symbol")
            self.players[1].symbol = self.players[1].choose_symbol()

    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win() or self.check_draw():
                if self.check_win():
                    self.players[self.current_player_ind - 1].score += 1
                    clear_screen()
                    self.board.showing_grid()
                    self.display_winner()
                    self.display_score()
                else:
                    clear_screen()
                    self.board.showing_grid()
                    print("Draw!")
                    self.display_score()
                choice = self.menu.endgame_menu()
                if choice == "1":
                    self.restart_game()
                else:
                    self.end_game()
                break

    def play_turn(self):
        while True:
            self.display_score()
            self.board.showing_grid()
            position = int(
                input(f"{self.players[self.current_player_ind].name}, enter a valid position on the board: "))
            if self.board.valid_move(position):
                break
            else:
                clear_screen()
                print(f"{self.players[self.current_player_ind].name}, enter a value between 1 and 9")
        self.board.update_board(self.players[self.current_player_ind].symbol, position)
        self.board.showing_grid()
        clear_screen()
        if self.current_player_ind == 0:
            self.current_player_ind = 1
        else:
            clear_screen()
            self.current_player_ind = 0

    def check_win(self):
        for i in range(7):
            if i % 3 == 0:
                if self.board.board[i] == self.board.board[i + 1] == self.board.board[i + 2]:
                    return True
            if i == 0:
                if self.board.board[i] == self.board.board[i + 4] == self.board.board[i + 8]:
                    return True
            if i == 2:
                if self.board.board[i] == self.board.board[i + 2] == self.board.board[i + 4]:
                    return True
            if i < 3:
                if self.board.board[i] == self.board.board[i + 3] == self.board.board[i + 6]:
                    return True

    def check_draw(self):
        for i in range(9):
            if not self.board.board[i].isalpha():
                return False
        return True

    def restart_game(self):
        clear_screen()
        self.board.reset_board()
        self.play_game()

    def display_score(self):
        print(f"{self.players[0].name}: {self.players[0].score}, {self.players[1].name}: {self.players[1].score}")

    def display_winner(self):
        print(f"{self.players[self.current_player_ind - 1].name} wins!")

    def end_game(self):
        clear_screen()
        self.display_score()
        print("Thank you for playing my Tic-Tac-Toe!")


game = Game()
game.start_game()
