import re

def doesPasswordPassValidation(lineOfInput):
    return PasswordRule(lineOfInput.ruleString).isPasswordValid(lineOfInput.passwordToCheck)

def doesPasswordPassNewValidation(lineOfInput):
    return NewPasswordRule(lineOfInput.ruleString).isPasswordValid(lineOfInput.passwordToCheck)


class LineOfInput:
    def parseLine(self, inputLine):
        match = re.search('^([0-9]*-[0-9]* [a-z]*): ([a-z]*$)', inputLine)
        self.ruleString = match.group(1)
        self.passwordToCheck = match.group(2)

    def __init__(self, inputLine):
        self.parseLine(inputLine)

class PasswordRule:
    def parseRuleFromString(self, ruleAsString):
        match = re.search('^([0-9]*)-([0-9]*) ([a-z]*)', ruleAsString)
        self.atLeast = int(match.group(1))
        self.atMost = int(match.group(2))
        self.compulsoryCharacter = match.group(3)

    def isPasswordValid(self, password):
        howManycompulsoryCharacters = password.count(self.compulsoryCharacter)
        return (howManycompulsoryCharacters >= self.atLeast and howManycompulsoryCharacters <= self.atMost)

    def __init__(self, ruleAsString):
        self.parseRuleFromString(ruleAsString)

class NewPasswordRule:
    def parseRuleFromString(self, ruleAsString):
        match = re.search('^([0-9]*)-([0-9]*) ([a-z]*)', ruleAsString)
        self.firstCompulsoryPosition = int(match.group(1))
        self.secondCompulsoryPosition = int(match.group(2))
        self.compulsoryCharacter = match.group(3)

    def isPasswordValid(self, password):
        howManycompulsoryCharacters = password.count(self.compulsoryCharacter)
        return ((password[self.firstCompulsoryPosition - 1] == self.compulsoryCharacter) ^ (password[self.secondCompulsoryPosition - 1] == self.compulsoryCharacter))

    def __init__(self, ruleAsString):
        self.parseRuleFromString(ruleAsString)


def main():

    # Exercise 1
    correctPasswords = 0
    with open('Day2Input.py') as file:
        lines = file.readlines()
        for line in lines:
            lineOfInput = LineOfInput(line)
            if (doesPasswordPassValidation(lineOfInput)):
                correctPasswords += 1
    print("There are " + str(correctPasswords) + " correct passwords")

    #Exercise 2
    correctPasswords = 0
    with open('Day2Input.py') as file:
        lines = file.readlines()
        for line in lines:
            lineOfInput = LineOfInput(line)
            if (doesPasswordPassNewValidation(lineOfInput)):
                correctPasswords += 1
    print("There are " + str(correctPasswords) + " correct passwords with new validation")


if __name__ == "__main__":
    main()