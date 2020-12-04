import os
import unittest

from Day1 import sumOfTwoNumbers
from Day1 import sumOfTwoNumbersEquals
from Day1 import inputFileAsListofIntegers
from Day1 import doAnyTwoIntegersInAListSumToDesiredValue

class SummingNumbers(unittest.TestCase):
    def testSumOfTwoNumbersIsCorrect(self):
        self.assertEqual(sumOfTwoNumbers(1, 3), 4)

    def testSumOfTwoNumbersIsIncorrect(self):
        self.assertNotEqual(sumOfTwoNumbers(5, 3), 6)

    def testSumOfTwoNumbersEqualsASum(self):
        self.assertTrue(sumOfTwoNumbersEquals(1, 3, 4))

class ReadingInput(unittest.TestCase):
    TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'TestDay1Input.txt')

    def testFileHasCorrectNumberOfLines(self):
        self.assertEqual(len(inputFileAsListofIntegers(ReadingInput.TESTDATA_FILENAME)), 3)

    def testFileHasCorrectLineContent(self):
        lines = inputFileAsListofIntegers(ReadingInput.TESTDATA_FILENAME)
        self.assertEqual(lines[0], 1)
        self.assertEqual(lines[1], 2)
        self.assertEqual(lines[2], 3)

    def testCanFindDesiredSumOfTwoIntegers(self):
        self.assertTrue(doAnyTwoIntegersInAListSumToDesiredValue([1, 2, 3], 5))

    def testCanFailToFindDesiredSumOfTwoIntegers(self):
        self.assertTrue(doAnyTwoIntegersInAListSumToDesiredValue([1, 2, 3], 2))



if __name__ == '__main__':
    unittest.main()
