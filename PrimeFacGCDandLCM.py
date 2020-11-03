def modOneToAnotherZero(FirstNumber, SecondNumber):
    """Returns True if there is no remainder after FirstNumber divides the SecondNumber"""
    if FirstNumber % SecondNumber == 0:
        return True
    else:
        return False
        
def isPrimeNumber(numberInQuestion):
    """Returns True if input number is Prime and False if it is Composite"""
    if numberInQuestion == 1:
        return False
    if numberInQuestion in [2,3,5,7]:
        return True
    for i in [2,3,4,5,6,7,8,9]:
        if modOneToAnotherZero(numberInQuestion, i) == False:
            continue
        else:
            return False
    return True

def nextPrimeNumber(CurrentInteger):
    """Calculates and Returns the next integer above the input integer"""
    CurrentInteger += 1
    while True:
        if isPrimeNumber(CurrentInteger) == True:
            return CurrentInteger
        CurrentInteger += 1

def primeFactorisationCW(inputNumber):
    """Calculates and Returns the Prime Factorisation list for a given number"""
    PrimeFactorizationDict = {}
    factorNumber = 2 #The current prime number that is being compared
    if inputNumber <= 1.0:
        return "Please restart and enter an integer greater than 1."
    while inputNumber > 1.0:
        if inputNumber % factorNumber == 0:
            inputNumber /= factorNumber
            if factorNumber in PrimeFactorizationDict:
                PrimeFactorizationDict[factorNumber] += 1
            else:
                PrimeFactorizationDict[factorNumber] = 1
        else:
            factorNumber = nextPrimeNumber(factorNumber)
    return PrimeFactorizationDict

def allFactorDictMaker(dictionary1,dictionary2,lcmORgcd):
    templateDictionary = {}
    for key in dictionary1:
        if key not in templateDictionary:
            templateDictionary[key] = 0
    for key in dictionary2:
        if key not in templateDictionary:
            templateDictionary[key] = 0

    for key in templateDictionary:
        if key not in dictionary1:
            dictionary1[key] = 0
        if key not in dictionary2:
            dictionary2[key] = 0

    for key in dictionary1:
        if lcmORgcd == 'lcm':
            templateDictionary[key] = max(dictionary1[key],dictionary2[key])
        if lcmORgcd == 'gcd':
            templateDictionary[key] = min(dictionary1[key],dictionary2[key])

    return templateDictionary

def calculateNumber(factorizationDictionary):
    totalOutputNumber = 1
    for key in factorizationDictionary:
        totalOutputNumber *= (key**factorizationDictionary[key])
    return "{:,}".format(totalOutputNumber)

def FactorizationString(factorizationDictionary):
    templist = []
    outputString = ''
    for key in factorizationDictionary:
        templist.append(key) 
    templist.sort()
    for i in templist:
        outputString += '('+"{:,}".format(i)+'^'+"{:,}".format(factorizationDictionary[i])+')·'
    outputString = outputString[:-1]#removes the last dot
    return outputString

def main():
    print()
    print("What would you like to calculate?")
    print("1) Prime Factorization of a number")
    print("2) Greatest Common Divisor (gcd)")
    print("3) Least Common Multiple (lcm)")
    calculationChoice = int(input("Enter a number followed by enter: "))

    if calculationChoice == 1:
        print()
        factoringNumberOne = int(input("What is the number you would like to find the Prime Factorization on: "))
        outputDict = primeFactorisationCW(factoringNumberOne)
        print()
        print("The Prime Factorization of","{:,}".format(factoringNumberOne),"is:")
        print(FactorizationString(outputDict),'=',calculateNumber(outputDict))

    elif calculationChoice == 2 or calculationChoice == 3:
        print()
        factoringNumberOne = int(input("What is the first number: "))
        factoringNumberTwo = int(input("What is the second number: "))

    if calculationChoice == 2:
        print()
        print("The Greatest Common Divisor (gcd) of","{:,}".format(factoringNumberOne),'and',"{:,}".format(factoringNumberTwo),'is:')
        print(calculateNumber(allFactorDictMaker(primeFactorisationCW(factoringNumberOne),primeFactorisationCW(factoringNumberTwo),'gcd')))
    if calculationChoice == 3:
        print()
        print("Least Common Multiple (lcm) of","{:,}".format(factoringNumberOne),'and',"{:,}".format(factoringNumberTwo),'is:')
        print(calculateNumber(allFactorDictMaker(primeFactorisationCW(factoringNumberOne),primeFactorisationCW(factoringNumberTwo),'lcm')))

if __name__ == "__main__":
    main()
