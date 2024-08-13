class Grid:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]

    def showing_grid(self):
        for i in range(0, 9, 3):
            print("|".join(self.board[i:i + 3]))
            if i < 6:
                print(5 * '-')

    def update_board(self, symbol: str, position: int):
        while True:
            if self.valid_move(position):
                self.board[position - 1] = symbol
                return True
            else:
                return False

    def valid_move(self, position: int):
        if 9 >= position > 0 and not self.board[position - 1].isalpha():
            return True
        else:
            return False

    def reset_board(self):
        self.board = [str(i) for i in range(1, 10)]