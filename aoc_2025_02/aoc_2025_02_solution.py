from aoc_2025_02_input import testInput, solutionInput
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
    return input.split(',')
inputList = inputToList(modeInput)

##print(f"--->{inputList}")

#What makes an ID invalid?
#   duplicated characters (ie. 55- 6464- 123123-...)


def solvePartOne(list):
    invalidIds = []
    for range in list:
        rangeStart = int(range.split("-")[0])
        rangeEnd = int(range.split("-")[1])
        currentId = rangeStart

        while currentId <= rangeEnd:
            length = len(str(currentId))
            #only even length IDs can be invalid
            if length % 2 == 0:
                ## print(f"–––>: {str(currentId)[0:int(length/2)]}-{str(currentId)[int(length/2):]}")    
                if str(currentId)[0:int(length/2)] == str(currentId)[int(length/2):]:
                    invalidIds.append(currentId)
            currentId += 1

    return sum(invalidIds)


def allEqual(list):
    base = list[0]
    for item in list:
        if item != base:
            return False
    return True


def solvePartTwo(list):
    invalidIds = []
    for vRange in list:
        rangeStart = int(vRange.split("-")[0])
        rangeEnd = int(vRange.split("-")[1])
        currentId = rangeStart

        while currentId <= rangeEnd:
            length = len(str(currentId))
            splitBy = math.floor(length/2)
            while splitBy >= 1:
                #'length' is devisable by 'splitBy' amount
                if length % splitBy == 0:
                    checkList = [str(currentId)[i:i+splitBy] for i in range(0, length, splitBy)]
                    #print(f"–––> {currentId}/{splitBy}: {checkList}")
                    if allEqual(checkList):
                        #print(f"invalid: {currentId}")
                        invalidIds.append(currentId)
                        break

                splitBy -= 1

            currentId += 1

    return sum(invalidIds)



print(solvePartTwo(inputList))

end_time = time.time()
print(f"--- {end_time - start_time:.4f} seconds ---") 


