def sumOfTwoNumbers(first, second):
    return first + second

def sumOfTwoNumbersEquals(first, second, sum):
    return (first + second) == sum

def inputFileAsListofIntegers(filename):
    with open(filename) as file:
        lines = file.readlines()
        return [int(line) for line in lines]

def doAnyTwoIntegersInAListSumToDesiredValue(integers, desiredSum):
    for firstInteger in integers:
        for secondInteger in integers:
            if sumOfTwoNumbersEquals(firstInteger, secondInteger, desiredSum):
                print("**")
                print(firstInteger)
                print(secondInteger)
                return True

def main():
    with open('Day1Input.txt') as file:
        lines = file.readlines()
        for first in lines:
            for second in lines:
                for third in lines:
                    sum = (int(first) + int(second) + int(third))
                    if sum == 2020:
                        multiplied = (int(first) * int(second) * int(third))
                        print("multiplied is " + str(multiplied))

if __name__ == "__main__":
    main()