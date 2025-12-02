from aoc_2025_01_input import testInput, solutionInput

##utility
def dynamicInput(mode):
    if mode == 'test':
        return testInput
    if mode == 'submit':
        return solutionInput   
#determin run mode (test/submit)
modeInput = dynamicInput('submit')
def inputToList(input):
    return input.split('\n')
inputList = inputToList(modeInput)






#part 1 solution
def solvePartOne(list):
    countZeroed = 0
    location = 50

    for item in list:
        direction = item[0]
        amount = int(item[1:])

        ##print(f"before turn:{location}")
        if direction == 'R':
            location += amount
        if direction == 'L':
            location -= amount


        ##print(f"before resets:{location}")
        while location < 0:
            location += 100
        while location > 99:
            location -= 100


        ##print(f"{direction}{amount}: {location}")
        if location == 0:
            countZeroed += 1

    print(f"solution: {countZeroed}")

#part 2 solution
def solvePartTwo(list):
    countZeroed = 0
    location = 50

    for item in list:
        direction = item[0]
        amount = int(item[1:])
        clicks = 0

        ##print(f"before turn:{location}")
        
        while amount > 0:
            if direction == 'R':
                if location == 99:
                    location = 0
                else:
                    location += 1

            if direction == 'L':
                if location == 0:
                    location = 99
                else:
                    location -= 1
            
            if location == 0:
                countZeroed +=1
            amount -= 1

    print(f"solution: {countZeroed}")


#run
solvePartTwo(inputList)