import random


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
                inner_list.append("?")
            game_board.append(inner_list)
        return game_board


def generate_ship_locations(ships, size):
    """
    Randomly allocates ships to positions on grid
    """
    ship_list = []
    while len(ship_list) < ships:
        a = random.randint(0, size)
        b = random.randint(0, size)
        ship = [a, b]
        print(ship)
        
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
    # Start the game
    display_boards(name, player_board, comp_board)
    player_ships = generate_ship_locations(ships, grid)
    print(player_ships)
    # create grid
    # place ships
    # play game {
    # dislay game grid
    # pick a coordinate
    # check for him or miss and display message
    # if hit check for win
    # generate comp guess
    # if hit check for win
    # when won diplay message
    # play again?


main()
