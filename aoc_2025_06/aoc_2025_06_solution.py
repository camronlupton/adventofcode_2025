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
modeInput = dynamicInput('submit')

    


def inputToList(input):
    length = len(input)

    #set Base list:
    c = 0
    operatorsFound = 0
    while c < length:
        if input[c] in ['+','*']:
            operatorsFound += 1
        c += 1
    result = [[] for _ in range(operatorsFound)]
    # split values into columns(equations) into lists in result
    n = 0
    c = 0
    v = 0
    curStr = ''
    while c < length:
        if input[c] in [' ','\n']:
            if curStr != '': #submit str
                result[v].append(curStr)
                curStr = ''
                v += 1
                #print(result)
            if input[c] == '\n':
                n += 1
                v = 0
        
        elif input[c] in ['1','2','3','4','5','6','7','8','9','0']:
            curStr = int(str(curStr) + input[c])
        elif input[c] in ['+','*']:
            curStr += input[c]
        c += 1
    return result
inputList = inputToList(modeInput)




def solvePartOne(list):
    rowResult = []

    for row in list:
        numList = row[0:-1]
        operator = row[-1]
        if operator == '+':
            val = sum(numList)
        elif operator == '*':
            val = math.prod(numList)
        rowResult.append(val)

        print(f"---> {operator} {numList} = {val}")
    return sum(rowResult)


#print(solvePartOne(inputList))




def solvePartTwo(string):
    list = string.split('\n')
    rowLength = len(list[0])
    rowCount = len(list)

    curRow = 0
    curChar = 0
    rawResult = []
    while curChar < rowLength:
        value = ''
        for row in list:
            value += row[curChar]
        rawResult.append(value.replace(' ',''))
        curChar += 1


    equations = [[]]
    curEquation = 0
    for item in rawResult:
        if item == '':
            equations.append([])
            curEquation += 1
            continue
        else:
            if '*' in item:
                equations[curEquation].append('*')
                item = item.replace('*','')
            if '+' in item:
                equations[curEquation].append('+')
                item = item.replace('+','')
            equations[curEquation].append(int(item))


    answerParts = []
    for equation in equations:
        nums = equation[1:]
        op = equation[0]
        if op == '+':
            val = sum(nums)
        elif op == '*':
            val = math.prod(nums)
        answerParts.append(val)
    return sum(answerParts)


print(solvePartTwo(modeInput))



print("finished")
end_time = time.time()
print(f"--- {end_time - start_time:.4f} seconds ---") 



