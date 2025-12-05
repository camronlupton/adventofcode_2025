from aoc_2025_04_input import testInput, solutionInput
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
    rows = input.split('\n')
    for row in rows:
        strList = [row[i:i+1] for i in range(0, len(row), 1)]
        result.append(strList)
    return result
inputList = inputToList(modeInput)

#x= horizontal
#y= vertical
#frame= xy

def solvePartOne(frame):
    moveable = 0
    frameSize = (len(frame[0]),len(frame))
    #print(f"frame: {frameSize}")
    curRow = 0
    for row in frame:
        curCol = 0
        for cell in row:
            if cell == "@":
                sides = sidesToCheck((curCol,curRow),frameSize)
                sidesBlocked = checkSides(frame, (curCol,curRow), sides) 
                if sidesBlocked < 4:
                    frame[curRow][curCol]='x'
                    moveable += 1
            curCol += 1
        curRow += 1
    return moveable, frame


def sidesToCheck(cellLoc, frameSize):
    sides = []
    cellRow = cellLoc[1]+1
    cellCol = cellLoc[0]+1
    if cellCol > 1: sides.append('l')
    if cellCol < frameSize[-1]: sides.append('r')
    if cellRow > 1: sides.append('u')
    if cellRow < frameSize[-1]: sides.append('d')
    return sides

def checkSides(frame, cellLoc, sides):
    blockedSpaces = []
    #cardinal directions
    if "l" in sides and frame[cellLoc[1]][cellLoc[0]-1] != ".": blockedSpaces.append("l")
    if "r" in sides and frame[cellLoc[1]][cellLoc[0]+1] != ".": blockedSpaces.append("r")
    if "u" in sides and frame[cellLoc[1]-1][cellLoc[0]] != ".": blockedSpaces.append("u")
    if "d" in sides and frame[cellLoc[1]+1][cellLoc[0]] != ".": blockedSpaces.append("d")
    #diagnol directions
    if "l" in sides and 'u' in sides and frame[cellLoc[1]-1][cellLoc[0]-1] != ".": blockedSpaces.append("lu")
    if "r" in sides and 'u' in sides and frame[cellLoc[1]-1][cellLoc[0]+1] != ".": blockedSpaces.append("ru")
    if "l" in sides and 'd' in sides and frame[cellLoc[1]+1][cellLoc[0]-1] != ".": blockedSpaces.append("ld")
    if "r" in sides and 'd' in sides and frame[cellLoc[1]+1][cellLoc[0]+1] != ".": blockedSpaces.append("rd")
    return len(blockedSpaces)


def resetFrame(list):
    rowNum = 0
    for row in list:
        colNum = 0
        for cell in row:
            if cell == 'x': list[rowNum][colNum] = '.'
            colNum += 1
        rowNum += 1
    return list

def solvePartTwo(frame):
    rollsMoved = []
    round = 1
    run = True
    while run:
        rollsThisRound, rawFrame = solvePartOne(frame)
        frame = resetFrame(rawFrame)
        rollsMoved.append(rollsThisRound)
        if rollsThisRound == 0: run = False
    print(rollsMoved)
    print(sum(rollsMoved))

solvePartTwo(inputList)
#testCell((7,0),inputList)

end_time = time.time()
print(f"--- {end_time - start_time:.4f} seconds ---") 