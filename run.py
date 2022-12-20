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


def main():
    """
    Main method that starts the game and calls all other methods
    """
    print("Welcome to Battleship!\n")
    name = input("Please enter your name:\n")
    grid = check_grid_size()
    ships = check_num_ships()
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
