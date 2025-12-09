from aoc_2025_07_input import testInput, solutionInput
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
inputList = modeInput.split('\n')

def replaceNthsChar(string, ns, new_char):
    if len(ns) == 0:
        return string

    n = max(ns)
    #print(f"replace {n}: {string[n]}")


    if n == 0: #front
        newString = new_char + string[n+1:]
    elif n == len(string)-1: #back
        newString = string[0:n] + new_char
    elif 0 < n < len(string)-1: #middle
        newString = string[0:n] + new_char + string[n+1:]


    ns.remove(n)
    return replaceNthsChar(newString, ns, new_char)

def findChars(string, target):
    i = 0
    indicies = []
    for char in string:
        if char is target:
            indicies.append(i)
        i += 1
    return indicies


def solvePartOne(list):
    timelines = 1
    splits = 0
    startIndicies = findChars(list[0], 'S')
    newList = []
    print(f"start: {startIndicies}")
    rowNum = 0
    for row in list:
        before = row 
        after = ''
        if rowNum == 0:
            after = row
            print(after)
        elif rowNum == 1:
            after = replaceNthsChar(row, startIndicies,'|')
            print(after)
        elif rowNum > 1:
            previousBeams = findChars(newList[rowNum-1],'|')
            rowsSplitters = findChars(row, '^')
            
            newBeams = []
            for beam in previousBeams:
                if beam in rowsSplitters:
                    newBeams.append(beam-1) 
                    newBeams.append(beam+1)
                    timelines += 2
                if beam not in rowsSplitters:
                    newBeams.append(beam)
            after = replaceNthsChar(before, newBeams, '|')

            print(after)
        newList.append(after)
        rowNum += 1

    print(f"{splits} splits")
    print(f"{timelines} timelines")

def solvePartTwo(inputList):
    length = len(inputList[0])
    timelines = [0] * length
    

    startingS = inputList[0].find('S')
    if startingS != -1:
        timelines[startingS] = 1 

    
    for rowNum in range(1, len(inputList)):
        row = inputList[rowNum]
        next_counts = [0] * length 
        for c in range(length):
            if timelines[c] > 0:
                count = timelines[c]
                
                if row[c] in ('.', 'S'):
                    next_counts[c] += count
                    
                elif row[c] == '^':
                    # beams thats are running out of frame
                    if c > 0:
                        next_counts[c - 1] += count  #going left
                    if c < length - 1:
                        next_counts[c + 1] += count  #going right
        timelines = next_counts
    total_timelines = sum(timelines)
    
    print(f"Total timelines: {total_timelines}")
    return total_timelines

#RUN CODES
# 
#print(f"---> {replaceNthsChar('asdfghjkl;kjhgfdsaASDFGHJK', [1,3,6,4,8], '|')}")
# 
# 
solvePartTwo(inputList)





print("finished")
end_time = time.time()
print(f"--- {end_time - start_time:.4f} seconds ---") 



