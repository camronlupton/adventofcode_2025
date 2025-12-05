from aoc_2025_05_input import testInput, solutionInput
import time, math
start_time = time.time()
print("started")

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
    return input.split('\n')

inputList = inputToList(modeInput)



def seperateInventory(input):
    freshRanges = [] #list of all unique Ids that are fresh
    availableIds = [] #list of all unique Ids that are available
    for line in input:
        if "-" in line: 
            ramList = []
            ram = line.split("-")
            for num in ram:
                ramList.append(int(num))
            freshRanges.append(ramList)
        elif line == "": print("gap found")
        else: availableIds.append(int(line))
    return freshRanges, availableIds


def solvePartOne(input):
    fresh, available = seperateInventory(inputList)
    print(f"fresh ranges: {fresh}")
    print(f"available: {available}")
    notSpoiled = []
    for item in available:
        for range in fresh:
            if range[0] <= item <= range[1]:
                notSpoiled.append(item)
                break
    return len(notSpoiled)

def overlappingRanges(rangeOne, rangeTwo):
    action = None
    if max(rangeOne[0], rangeTwo[0]) <= min(rangeOne[1], rangeTwo[1]) + 1:
        action = 'merge'

    if action == 'merge':
        fullRange = [rangeOne[0],rangeOne[1],rangeTwo[0],rangeTwo[1]]
        return action, [min(fullRange), max(fullRange)]
    return None, [0,0]

def simplifyRanges(list_to_modify):
    x = 0
    while x < len(list_to_modify):
        y = 0
        while y < len(list_to_modify):
            if y != x:
                action, newRange = overlappingRanges(list_to_modify[x], list_to_modify[y])
                if action == 'merge':
                    idx_max = max(x, y)
                    idx_min = min(x, y)
                    
                    list_to_modify.pop(idx_max)
                    list_to_modify.pop(idx_min)
                    list_to_modify.append(newRange)
                    simplifyRanges(list_to_modify)
                    
            y += 1
        x +=1

    return list_to_modify

def solvePartTwo(input):
    fresh, available = seperateInventory(input) 
    print(f"fresh ranges: {fresh}")
    rangeSizes = []


    fresh = simplifyRanges(fresh)
    for range in fresh:
        rangeSizes.append(range[1] - range[0] + 1)
        
    print(f"Merged fresh ranges: {fresh}")
    return sum(rangeSizes)

#print(solvePartOne(inputList))
print(solvePartTwo(inputList))
print("finished")
end_time = time.time()
print(f"--- {end_time - start_time:.4f} seconds ---") 




