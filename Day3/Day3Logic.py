from enum import Enum

class Square(Enum):
    Open = 1
    Tree = 2

def whatOpenSquareIsThis(square):
    if (square == '.'):
        return Square.Open
    elif (square == '#'):
        return Square.Tree

def moveLaterally(startingPosition, lineLength, lateralMovement):
    if (lateralMovement == 0):
        return startingPosition

    currentPosition = startingPosition
    movement = lateralMovement
    while movement > 0:
        if (currentPosition == lineLength):
            currentPosition = 1
        else:
            currentPosition += 1
        movement -= 1

    return currentPosition

def whatIsAtPosition(position, line):
    return whatOpenSquareIsThis(line[position - 1]) # we're 1-based indexing lines

# You can't move any more down when you are at the bottom
def moveDown(startingHeight, totalHeight, movement):
    finalHeight = totalHeight - movement
    if (finalHeight < 1):
        finalHeight = 1

    return finalHeight

def readSlopeFromFile(filename):
    with open(filename) as file:
        return [line.rstrip() for line in file.readlines()]

def main():
    print("hello")

    slope = readSlopeFromFile('Day3Input.txt')
    startingHeight = len(slope)
    startingLateralPosition = 1
    lineLength = len(slope[0])
    print ("Slope height is " + (str(startingHeight)))
    print ("Length of a line before wrapping is " + (str(lineLength)))

    currentHeight = startingHeight
    currentLateralPosition = startingLateralPosition
    while currentHeight > 1:
        currentLateralPosition = moveLaterally(currentLateralPosition, lineLength, 3)
        currentHeight -= 1


if __name__ == "__main__":
    main()