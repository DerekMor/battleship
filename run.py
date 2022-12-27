import random
import time


class Board:
    """
    Creates instances of a playing grid and calls methods
     to generate ships on the grid
    """
    def __init__(self, player, name, size):
        self.player = player
        self.name = name
        self.size = size

    def generate_game_board(self, size, ships):
        """
        Code that generates the game board
        """
        game_board = []
        for i in range(size):
            inner_list = []
            for j in range(size):
                if self.name == "Computer":
                    inner_list.append("?")
                else:
                    inner_list.append("-")
            game_board.append(inner_list)
        return game_board


def generate_ship_locations(ships, size):
    """
    Randomly allocates ships to positions on grid
    """
    ship_list = []
    while len(ship_list) < ships:
        a = random.randint(0, (size -1))
        b = random.randint(0, (size -1))
        ship = [a, b]
       
        if len(ship_list) == 0:
            ship_list.append(ship)
            continue
        has_match = False
        for i in ship_list:
            if i == ship:
                has_match = True
                break
        if has_match is False:
            ship_list.append(ship)   

    return ship_list

         
def check_grid_size():
    """
    Asks the user what size grid they would like to play on
    """
    while True:
        try:
            grid_size = int(input("What size square grid would you like to use? (between 5 and 10)\n"))
        except ValueError:
            print("Please enter only a number")
            continue

        if grid_size < 5 or grid_size > 10:
            print("please enter a number between 5 and 10")
            continue
        else:
            break

    return grid_size


def check_num_ships():
    """
    Asks user to specify the number of ships they would like to use
    """
    while True:
        try:
            ships = int(input("How many ships would you like to use? (between 2 and 10)\n"))
        except ValueError:
            print("Please enter only a number")
            continue

        if ships < 2 or ships > 10:
            print("please enter a number between 2 and 10")
            continue
        else:
            break

    return ships


def display_boards(name, player, comp):
    """
    Displays game boards to console
    """
    print(f"\n{name}'s board\n")
    for i in range(len(player)):
        for j in range(len(player[i])):
            print(player[i][j], end= " ")
        print("")

    print("\nComputers board\n")
    for i in range(len(comp)):
        for j in range(len(comp[i])):
            print(comp[i][j], end= " ")
        print("")
    print("\n")

# def update_boards(name, board, guess):
#    """
#    Updates the game board using a guess
#    """


def place_player_ships(board, list):
    """
    Places the players ships visable on the board
    """
    for i in range(len(list)):
        board[list[i][0]][list[i][1]] = "@"

    return board


def get_player_guess(size, board):
    """
    Asks player for coordinates, validates input, checks if it has been previously guessed
    """
    while True:
        try:
            c1 = int(input("Please enter your first coordinate. The top left corner is position 0, 0:\n"))
        except ValueError:
            print("Please enter only a number")
            continue

        if c1 < 0 or c1 > (size -1):
            print(f"please enter a number between 0 and {size -1}")
            continue

        try:
            c2 = int(input("Please enter your second coordinate:\n"))
        except ValueError:
            print("Please enter only a number")
            continue

        if c2 < 0 or c2 > (size -1):
            print(f"please enter a number between 0 and {size -1}")
            continue
        
        print(f"You have entered {c1}, {c2}")
        time.sleep(1.5)
        guess = [c1, c2]
        if board[c1][c2] != "?":
            print("Coordinates have already been guessed, please try again")
            continue
        else:
            break
    return guess


def check_player_hit(guess, board, ships):
    """
    checks for hit or miss on board
    """
    hit = False
    for i in range(len(ships)):
        if ships[i] == guess:
            hit = True
            board[guess[0]][guess[1]] = "*"
            break
        else:
            board[guess[0]][guess[1]] = "X"
    if hit:
        print("HIT")
        time.sleep(1.5)
    else:
        print("Miss")
        time.sleep(1.5)
    return board


def check_win(board, ships, name):
    """
    Checks the hits on the board to check for winning conditions
    """
    hits = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "*":
                hits += 1
    if hits == ships:
        print(f"{name} has won!")
        time.sleep(1.5)
        return True
    else:
        return False


def get_comp_guess(size, board):
    """
    Generates a computer guess and makes sure it is not a duplicate guess
    """
    while True:
        a = random.randint(0, (size -1))
        b = random.randint(0, (size -1))
        if board[a][b] == "-":
            print(f"Computer has guessed {a}, {b}")
            time.sleep(1.5)
            print("Computer missed!")
            time.sleep(1.5)
            board[a][b] = "X"
            break
        elif board[a][b] == "@":
            print(f"Computer has guessed {a}, {b}")
            time.sleep(1.5)
            print("Computer has hit!")
            time.sleep(1.5)
            board[a][b] = "*"
            break
        else:
            continue
    
    return board


def main():
    """
    Main method that starts the game and calls all other methods
    """
    # Starting questions
    print("Welcome to Battleship!\n")
    name = input("Please enter your name:\n")
    grid = check_grid_size()
    ships = check_num_ships()
    # Initialise game boards
    player = Board(1, name, grid)
    comp = Board(2, "Computer", grid)
    player_board = player.generate_game_board(grid, ships)
    comp_board = comp.generate_game_board(grid, ships)
    player_ships = generate_ship_locations(ships, grid)
    computer_ships = generate_ship_locations(ships, grid)
    player_board = place_player_ships(player_board, player_ships)
    # start game
    has_winner = False
    while has_winner is False:
        display_boards(name, player_board, comp_board)
        player_guess = get_player_guess(grid, comp_board)
        comp_board = check_player_hit(player_guess, comp_board, computer_ships)
        player_win = check_win(comp_board, ships, player.name)

        if player_win:
            break

        player_board = get_comp_guess(grid, player_board)

        comp_win = check_win(player_board, ships, comp.name)

        if comp_win:
            break

    print("Thanks for playing!")
    time.sleep(1.5)
    play_again = input("Enter 'Y' to play again or anything else to end game\n")
    if play_again == "Y":
        main()

    # generate comp guess
    # if hit check for win
    # when won diplay message
    # play again?


main()
