import unittest

from Day2Logic import PasswordRule
from Day2Logic import LineOfInput
from Day2Logic import doesPasswordPassValidation

class ParsingRules(unittest.TestCase):

    def testCanParseLowerBound(self):
        ruleAsString = "4-5 m"
        rule = PasswordRule(ruleAsString)
        self.assertEqual(4, rule.atLeast)

    def testCanParseUpperBound(self):
        ruleAsString = "4-5 m"
        rule = PasswordRule(ruleAsString)
        self.assertEqual(5, rule.atMost)


    def testCanParseCompulsoryCharacter(self):
        ruleAsString = "4-5 m"
        rule = PasswordRule(ruleAsString)
        self.assertEqual('m', rule.compulsoryCharacter)

class CanParseALineOfInput(unittest.TestCase):

    def testCanParseALineOfInput(self):
        line = "5-6 j: jjjjjj"
        lineOfInput = LineOfInput(line)
        self.assertEqual("5-6 j", lineOfInput.ruleString)
        self.assertEqual("jjjjjj", lineOfInput.passwordToCheck)

class PasswordIsValidated(unittest.TestCase):

    def testValidPasswordPasses(self):
        lineOfInputAsString = "4-5 m: aassmsmsmsmsm"
        lineOfInput = LineOfInput(lineOfInputAsString)

        self.assertTrue(doesPasswordPassValidation(lineOfInput))

    def testInvalidPasswordFails(self):
        lineOfInputAsString = "4-5 m: aassmm"
        lineOfInput = LineOfInput(lineOfInputAsString)

        self.assertFalse(doesPasswordPassValidation(lineOfInput))



if __name__ == '__main__':
    unittest.main()
