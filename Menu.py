class Menu:
    def display_main_menu(self):
        print("Welcome to my Tic-Tac-Toe game\n"
              "1.Start game\n"
              "2.Quit game")
        while True:
            choice = input("Enter your choice(1 or 2): ")
            if choice == "1" or choice == "2":
                break
            print("Invalid choice. Only 1 or 2")
        return choice

    def endgame_menu(self):
        print("Thank you for playing <3\n"
              "1.Play again\n"
              "2.Quit game")
        while True:
            choice = input("Enter your choice(1 or 2): ")
            if choice == '1' or choice == '2':
                break
            print("Invalid choice. Only 1 or 2")
        return choice
