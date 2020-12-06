import math

def sumOfTwoNumbers(first, second):
    return first + second

def sumOfTwoNumbersEquals(first, second, sum):
    return (first + second) == sum

def productOfFactors(factors):
    return math.prod(factors)

def inputFileAsListofIntegers(filename):
    with open(filename) as file:
        lines = file.readlines()
        return [int(line) for line in lines]

def whichTwoIntegersInAListSumToDesiredValue(integers, desiredSum):
    # Cannot sum with less than two integers
    if len(integers) < 2:
        return []

    # Don't want to sum elements with themselves
    firstInteger = integers.pop()

    for secondInteger in integers:
        if sumOfTwoNumbersEquals(firstInteger, secondInteger, desiredSum):
           return [firstInteger, secondInteger]

    return whichTwoIntegersInAListSumToDesiredValue(integers, desiredSum)

def whichThreeIntegersInAListSumToDesiredValue(integers, desiredSum):
    # Cannot sum with less than two integers
    if len(integers) < 3:
        return []

    # Don't want to sum elements with themselves
    firstInteger = integers.pop()
    for secondInteger in integers:
        if sumOfTwoNumbersEquals(firstInteger, secondInteger, desiredSum):
           return [firstInteger, secondInteger]

    return whichThreeIntegersInAListSumToDesiredValue(integers, desiredSum)



def main():

    # Exercise 1
    listOfIntegers = inputFileAsListofIntegers('Day1Input.txt')
    twoNumbers = whichTwoIntegersInAListSumToDesiredValue(listOfIntegers, 2020)
    answerForExerciseOne = productOfFactors(twoNumbers)
    print("Answer for exercise 1 is " + str(answerForExerciseOne))

    #Exercise 2
    threeNumbers = whichThreeIntegersInAListSumToDesiredValue(listOfIntegers, 2020)
    answerForExerciseTwo = productOfFactors(threeNumbers)
    print("Answer for exercise 2 is " + str(answerForExerciseTwo))

if __name__ == "__main__":
    main()