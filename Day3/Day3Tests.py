import unittest
from Day3Logic import Square
from Day3Logic import whatOpenSquareIsThis
from Day3Logic import moveLaterally
from Day3Logic import whatIsAtPosition
from Day3Logic import moveDown

class CanReadInput(unittest.TestCase):

    def testKnowWhatTreeSquareIs(self):
        self.assertEqual(whatOpenSquareIsThis('#'), Square.Tree)

    def testKnowWhatOpenSquareIs(self):
        self.assertEqual(whatOpenSquareIsThis('.'), Square.Open)

    def testMovingLeftWithoutWrappingGivesPosition(self):
        line = "....#.."
        startingPosition = 1
        movementRight = 4
        destinationPosition = moveLaterally(startingPosition, line, movementRight)
        self.assertEqual(5, destinationPosition)

    def testMovingLeftWithWrappingGivesPosition(self):
        line = "..#.."
        startingPosition = 1
        movementRight = 7
        destinationPosition = moveLaterally(startingPosition, len(line), movementRight)
        self.assertEqual(3, destinationPosition)

    def testKnowATreeIsWhereItIsExpected(self):
        line = "..#.."
        self.assertEqual(Square.Tree, whatIsAtPosition(3, line))

    def testMovingDownGivesPosition(self):
        slope = ["...", "#..", "..."]
        startingHeight = 3
        downwardMovement = 1
        self.assertEqual(2, moveDown(1, len(slope), downwardMovement))

    def testMovingDownPastBottomGivesPosition(self):
        slope = ["...", "#..", "..."]
        startingHeight = 3
        downwardMovement = 4
        self.assertEqual(1, moveDown(1, len(slope), downwardMovement))


if __name__ == '__main__':
    unittest.main()
