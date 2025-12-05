from aoc_2025_03_input import testInput, solutionInput
import time, math
start_time = time.time()

##utility
def dynamicInput(mode):
    if mode == 'test':
        return testInput
    if mode == 'submit':
        return solutionInput   
#determin run mode (test/submit)
modeInput = dynamicInput('submit')
def inputToList(input):
    result = []
    banks = input.split('\n')
    for bank in banks:
        strList = [bank[i:i+1] for i in range(0, len(bank), 1)]
        numList = [int(strList[i]) for i in range(0,len(strList),1)]
        result.append(numList)
    return result
inputList = inputToList(modeInput)


def findLargestOne(list, omitStart, omitEnd):
    currentHighestNum = 0
    currentIndex = 0
    indexFound = None
    list = list[omitStart:len(list)-omitEnd]
    for num in list:
        if num > currentHighestNum:
            currentHighestNum = num
            indexFound = currentIndex
        currentIndex += 1
    return currentHighestNum, indexFound

def solvePartOne(banks):
    bankVoltages = []
    for bank in inputList:
        ##first digit
        firstDigitNum, firstDigitIndex = findLargestOne(bank, 0, 1)
        ##second digit
        secondDigitNum, secondDigitIndex = findLargestOne(bank, firstDigitIndex+1, 0)
        bankVoltages.append(int(str(firstDigitNum)+str(secondDigitNum)))
    return sum(bankVoltages)

def findLargestTwo(list, omitStart, omitEnd):
    currentHighestNum = 0
    currentIndex = 0
    indexFound = None 
    list = list[omitStart:len(list)-omitEnd]
    for num in list:
        if num > currentHighestNum:
            currentHighestNum = num
            indexFound = currentIndex
        currentIndex += 1
    return currentHighestNum, indexFound+1

def solvePartTwo(banks, digits):
    bankVoltages = []
    for bank in inputList:
        builtNum = 0
        IndexBlocked = 0
        #find Max voltage of n(digits) batteries per bank
        for digit in range(0,digits,1):
            nextDigitNum, IndexBlockedDelta = findLargestTwo(bank, IndexBlocked, digits-digit-1)
            IndexBlocked += IndexBlockedDelta
            builtNum = int(str(builtNum)+str(nextDigitNum))
        #print(f"–––> {builtNum}")
        bankVoltages.append(builtNum)
    return sum(bankVoltages)

    




print(f"result: {solvePartTwo(inputList, 12)}")
#print(f"result: {solvePartOne(inputList)}")


end_time = time.time()
print(f"--- {end_time - start_time:.4f} seconds ---") 