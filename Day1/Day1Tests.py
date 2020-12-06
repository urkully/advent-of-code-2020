import os
import unittest

from Day1 import sumOfTwoNumbers
from Day1 import sumOfTwoNumbersEquals
from Day1 import inputFileAsListofIntegers
from Day1 import whichTwoIntegersInAListSumToDesiredValue
from Day1 import whichThreeIntegersInAListSumToDesiredValue
from Day1 import productOfFactors

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

class FindingSumsOfTwoInList(unittest.TestCase):
    def testCannotHaveLessThanTwoIntegers(self):
        self.assertCountEqual(whichTwoIntegersInAListSumToDesiredValue([1], 2), [])

    def testCanFindDesiredSumOfTwoIntegers(self):
        self.assertCountEqual(whichTwoIntegersInAListSumToDesiredValue([1, 2, 3], 5), [2, 3])

    def testCanFailToFindDesiredSumOfTwoIntegers(self):
        self.assertCountEqual(whichTwoIntegersInAListSumToDesiredValue([1, 2, 3], 7), [])

class FindingSumsOfThreeInList(unittest.TestCase):
    def testCannotHaveLessThanThreeIntegers(self):
        self.assertCountEqual(whichThreeIntegersInAListSumToDesiredValue([1, 2], 2), [])



class FindingProductOfFactors(unittest.TestCase):
    def testCorrectProductWithTwoFactors(self):
        self.assertEqual(productOfFactors([2, 3]), 6)

if __name__ == '__main__':
    unittest.main()
