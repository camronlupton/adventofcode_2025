from aoc_2025_06_input import testInput, solutionInput
import time
import math
start_time = time.time()
print("started")

##utility
def dynamicInput(mode):
    if mode == 'test':
        return testInput
    if mode == 'submit':
        return solutionInput   
#determin run mode (test/submit)
modeInput = dynamicInput('test')

def solvePartTwo(list):
    result = None
    rowResults = []
    for row in list:
        numList = row[0:-1]
        operator = row[-1]
        longestDigit = len(str(max(numList)))
        #print(f"nums:{numList}, op:{operator}")
        #print(f"len: {longestDigit}")
        digit =  -1
        newEquation = []
        while digit > ((-1) * (longestDigit+1)):
            buildingNum = ''
            #print(f"digit: {digit}")
            for num in numList:
                if len(str(num)) >= digit*(-1):
                    #print(f"d{digit}: '{str(num)[(digit)]}' of '{str(num)}'")
                    buildingNum = str(buildingNum) + str(num)[(digit)]

                else:
                    continue
            digit -= 1
            newEquation.append(int(buildingNum))
        if operator == '+':
            val = sum(newEquation)
        elif operator == '*':
            val = math.prod(newEquation)
        print(f"original{numList}")
        print(f"{operator} on {newEquation} == {val}")
        print("")
        rowResults.append(val)
    print(rowResults)




print("finished")
end_time = time.time()
print(f"--- {end_time - start_time:.4f} seconds ---") 



