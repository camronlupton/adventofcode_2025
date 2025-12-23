from aoc_2025_09_input import testInput, solutionInput
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
inputList = dynamicInput('submit').split('\n')
def getInputCords(list):
    newList = []
    for row in list:
        temp = row.split(',')
        newList.append([int(temp[0]),int(temp[1])])
    return newList
inputTiles = getInputCords(inputList)
nullTile = '•'
greenTile = 'G'
redTile = 'R'


def getGridSize(reds):
    maxCol = 0 # tile[0]
    maxRow = 0 # tile[1]
    minCol = 9999999999999
    minRow = 9999999999999
    for tile in reds:
        if tile[0] > maxCol: maxCol = tile[0] 
        if tile[1] > maxRow: maxRow = tile[1] 
        if tile[0] < minCol: minCol = tile[0]
        if tile[1] < minRow: minRow = tile[1] 
    #print([minCol, minRow], [maxCol,maxRow])
    return [minCol, minRow], [maxCol,maxRow]

def displayGrid(reds):
    minCoords, gridSize = getGridSize(reds) # Example: [11, 11]
    
    # Calculate dimensions
    rows = gridSize[1] + 2
    cols = gridSize[0] + 2

    #print(f"Grid Dimensions: {cols} x {rows}") # Check this output!
    grid = [[nullTile] * cols for _ in range(rows)]

    for row in grid:
        print(' '.join(row))
        

    r=0
    for tile in reds:
        #print(tile)
        grid[tile[1]][tile[0]]=redTile

    for row in grid:
        print(' '.join(row))

    prevTile = reds[-1]

    for tile in reds:
        if tile[0] != prevTile[0]: 
            stableRow = tile[1]
            start = min(tile[0], prevTile[0])
            end = max(tile[0], prevTile[0])
            
            for col in range(start + 1, end):
                grid[stableRow][col] = greenTile

        elif tile[1] != prevTile[1]: 
            stableCol = tile[0]
            start = min(tile[1], prevTile[1])
            end = max(tile[1], prevTile[1])
            
            for row in range(start + 1, end):
                grid[row][stableCol] = greenTile
        
        prevTile = tile


    print('draw:')
    for row in grid:
        print(' '.join(row))
    

    

    


#def solvePartOne(reds):
    areas = []
    for redA in reds:
        for redB in reds:
            cols= [redA[0],redB[0]]
            rows= [redA[1],redB[1]]
            
            colDelta = max(cols)-min(cols)+1
            rowDelta = max(rows)-min(rows)+1
            area = colDelta * rowDelta
            areas.append(area)

    return max(areas)


        

print(getGridSize(inputTiles))
#print(solvePartOne(inputTiles))
#displayGrid(inputTiles)

print("finished")
end_time = time.time()
print(f"--- {end_time - start_time:.4f} seconds ---") 



