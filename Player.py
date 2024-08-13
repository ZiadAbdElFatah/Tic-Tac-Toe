class Player:

    def __init__(self, name="Player", symbol='x', score=0):
        self.name = name
        self.symbol = symbol
        self.score = score

    def choose_name(self):
        while True:
            self.name = input(f"Enter your name(letters only): ")
            if self.name.isalpha():
                break
            print("Invalid name.")
        return self.name

    def choose_symbol(self):
        while True:
            self.symbol = input(f"{self.name}, Enter your symbol(x or o only): ")
            if self.symbol == 'x' or self.symbol == 'o':
                self.symbol = self.symbol.upper()
                break
            print("Invalid symbol.")
        return self.symbol
