import random


def minesweeper_game(n, m):
    grid = [[0 for row in range(n)] for column in range(n)]
    for i in range(m):
        xCoord = random.randint(0, n - 1)
        yCoord = random.randint(0, n - 1)
        grid[yCoord][xCoord] = 'X'
        # center right/left
        if (xCoord >= 0 and xCoord <= n - 2) and (yCoord >= 0 and yCoord <= n - 1):
            if grid[yCoord][xCoord + 1] != 'X':
                grid[yCoord][xCoord + 1] += 1

        if (xCoord >= 1 and xCoord <= n - 1) and (yCoord >= 0 and yCoord <= n - 1):
            if grid[yCoord][xCoord - 1] != 'X':
                grid[yCoord][xCoord - 1] += 1

        # top left/right/center
        if (xCoord >= 1 and xCoord <= n - 1) and (yCoord >= 1 and yCoord <= n - 1):
            if grid[yCoord - 1][xCoord - 1] != 'X':
                grid[yCoord - 1][xCoord - 1] += 1

        if (xCoord >= 0 and xCoord <= n - 2) and (yCoord >= 1 and yCoord <= n - 1):
            if grid[yCoord - 1][xCoord + 1] != 'X':
                grid[yCoord - 1][xCoord + 1] += 1

        if (xCoord >= 0 and xCoord <= n - 1) and (yCoord >= 1 and yCoord <= n - 1):
            if grid[yCoord - 1][xCoord] != 'X':
                grid[yCoord - 1][xCoord] += 1

        # bottom right/left/center
        if (xCoord >= 0 and xCoord <= n - 2) and (yCoord >= 0 and yCoord <= n - 2):
            if grid[yCoord + 1][xCoord + 1] != 'X':
                grid[yCoord + 1][xCoord + 1] += 1

        if (xCoord >= 1 and xCoord <= n - 1) and (yCoord >= 0 and yCoord <= n - 2):
            if grid[yCoord + 1][xCoord - 1] != 'X':
                grid[yCoord + 1][xCoord - 1] += 1

        if (xCoord >= 0 and xCoord <= n - 1) and (yCoord >= 0 and yCoord <= n - 2):
            if grid[yCoord + 1][xCoord] != 'X':
                grid[yCoord + 1][xCoord] += 1
    return grid

# create grid


def createMap(n):
    grid = [['.' for row in range(n)] for column in range(n)]
    return grid

# spacing out the game map


def styleMap(map):
    for row in map:
        print("\t".join(str(coord) for coord in row))
        print("")

# detecting if the game is filled out


def gameWon(map):
    for row in map:
        for coord in row:
            if coord == '.':
                return False
    return True

# play a new game


def continueGame(score):
    print("Score: ", score)
    isContinue = input("Play again? (y/n): ")
    if isContinue == 'n':
        return False
    return True

# start game


def startGame():
    gameStat = True
    while gameStat:
        # n = grid num; m = mine num
        n = 5
        m = 3
        minesweeper_map = minesweeper_game(n, m)
        playerMove = createMap(n)
        score = 0
        while True:
            if gameWon(playerMove) == False:
                print("Enter Column and Row to start: ")
                try:
                    xCoord = int(input("Column (1 to 5): "))
                    yCoord = int(input("Row (1 to 5): "))

                    if ((xCoord > 5 or xCoord < 1) or (yCoord > 5 or yCoord < 1)):
                        print("Column and/or Row is out of bound, please try again.")
                        continue

                    xCoord = int(xCoord) - 1
                    yCoord = int(yCoord) - 1

                    if (minesweeper_map[yCoord][xCoord] == 'X'):
                        print("Not Solved, you lost! Try again!")
                        styleMap(minesweeper_map)
                        gameStat = continueGame(score)
                        break

                    else:
                        playerMove[yCoord][xCoord] = minesweeper_map[yCoord][xCoord]
                        styleMap(playerMove)
                        score += 1

                except:
                    print("Input is not a number")
                    continue

            else:
                styleMap(playerMove)
                print("Solved! You won!")
                gameStat = continueGame(score)
                break

# code to find one solution to the puzzle


def solveGame():
    n = 5
    m = 3
    xCoord = 0
    yCoord = 0
    minesweeper_map = minesweeper_game(n, m)
    playerMove = createMap(n)

    while gameWon(playerMove) == False and yCoord < n:
        print("y:", yCoord)
        while xCoord < n:
            print("x:", xCoord)
            if (minesweeper_map[yCoord][xCoord] != 'X'):
                playerMove[yCoord][xCoord] = minesweeper_map[yCoord][xCoord]
            xCoord += 1
        yCoord += 1
        xCoord = 0

    styleMap(playerMove)
    print("Solved!")


if __name__ == "__main__":
    # startGame()
    solveGame()
