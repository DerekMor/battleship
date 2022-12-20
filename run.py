def check_grid_size(name):
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


def main():
    """
    Main method that starts the game and calls all other methods
    """
    print("Welcome to Battleship!\n")
    name = input("Please enter your name:\n")
    check_grid_size(name)
    # number of ships
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
