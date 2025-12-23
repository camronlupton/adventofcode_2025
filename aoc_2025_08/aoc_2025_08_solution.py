from aoc_2025_08_input import testInput, solutionInput
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
def getCords(list):
    print("Getting Cords...")
    result = []
    boxNum = 0
    for box in list:
        #print(box)
        cords = box.split(',')
        dict = {}
        dict['id'] = boxNum
        dict['x'] = int(cords[0])
        dict['y'] = int(cords[1])
        dict['z'] = int(cords[2])
        result.append(dict)
        boxNum += 1
    return result
junctionBoxes = getCords(inputList)

def findDistance(a, b):
    print("Finding Distance...")
    id, x,y,z = ('id','x','y','z')
    xDelta = a[x] - b[x]
    yDelta = a[y] - b[y]
    zDelta = a[z] - b[z]
    #print(f"deltas: {xDelta}, {yDelta}, {zDelta}")
    distance = math.sqrt((xDelta**2) + (yDelta**2) + (zDelta**2))
    #print(distance)
    return distance



##find distance between all box pairings
def solvePartOne(boxes, pairs):
    id, x,y,z = ('id','x','y','z')
    boxDistanceMemo = {}
    for aBox in boxes:
        for bBox in boxes: 
            if aBox[id] != bBox[id]:
                boxDistanceMemo[aBox[id],bBox[id]] = findDistance(aBox,bBox)
    sortedMemo = {k: v for k, v in sorted(boxDistanceMemo.items(), key= lambda v: v[1])}

    ##remove duplicates (1,2) & (2,1)
    simplifiedMemo = {}
    for memo in sortedMemo: ##remove duplicates (1,2) & (2,1)
        #print(memo, boxDistanceMemo[memo],  boxes[memo[0]],boxes[memo[1]])
        if memo[0] < memo[1]:
            simplifiedMemo[memo] = sortedMemo[memo]


    connectionsMade = []
    for memo in simplifiedMemo:
        if len(connectionsMade) < pairs:
            #print(memo, simplifiedMemo[memo],  boxes[memo[0]],boxes[memo[1]])
            connectionsMade.append(memo)
    
    clusters = []
    remainingConnections = connectionsMade.copy()
    inCluster = []
    addToCluster = []
    conNum = 0

    for connection in connectionsMade[0:pairs]:
        if connection in remainingConnections:
            newCluster= checkForConenctions([connection],remainingConnections)
            clusters.append(newCluster)
            for item in newCluster:
                remainingConnections.remove(item)
    clusterSizes = []

    clusterNum = 0
    clusterBoxes = []
    for cluster in clusters:
        clusterBoxes.append([])
        for item in cluster:
            if item[0] not in clusterBoxes[clusterNum]: clusterBoxes[clusterNum].append(item[0])
            if item[1] not in clusterBoxes[clusterNum]: clusterBoxes[clusterNum].append(item[1])
        clusterNum += 1

    sortedClusters = sorted(clusterBoxes, key=len, reverse=True)
    print(sortedClusters)
    result = []
    for cluster in sortedClusters:
        if len(result) < 3: result.append(len(cluster))

    print(result)
    print(math.prod(result))


def checkForConenctions(chain, list):
    chainPoints = []
    for link in chain:
        if link[0] not in chainPoints: chainPoints.append(link[0])
        if link[1] not in chainPoints: chainPoints.append(link[1])
    chainAdds = 0
    for connection in list:
        pairFound = False
        if connection in chain:
            continue
        else:
            if connection[0] in chainPoints: pairFound = True
            if connection[1] in chainPoints: pairFound = True
            if pairFound == True:
                chainAdds += 1
                chain.append(connection)
                lastCluster = connection
                if connection[0] not in chainPoints: chainPoints.append(connection[0])
                if connection[1] not in chainPoints: chainPoints.append(connection[1])

    print(f"Adds: {chainAdds}")
    if chainAdds > 0: return checkForConenctions(chain,list)
    if chainAdds == 0: return chain

def solvePartTwo(boxes):
    id, x,y,z = ('id','x','y','z')
    print("Building MEmo")
    boxDistanceMemo = {}
    for aBox in boxes:
        for bBox in boxes: 
            if aBox[id] != bBox[id]:
                boxDistanceMemo[aBox[id],bBox[id]] = findDistance(aBox,bBox)
    print("sorting")
    sortedMemo = {k: v for k, v in sorted(boxDistanceMemo.items(), key= lambda v: v[1])}

    ##remove duplicates (1,2) & (2,1)
    print("simplifying")
    simplifiedMemo = {}
    for memo in sortedMemo: ##remove duplicates (1,2) & (2,1)
        #print(memo, boxDistanceMemo[memo],  boxes[memo[0]],boxes[memo[1]])
        if memo[0] < memo[1]:
            simplifiedMemo[memo] = sortedMemo[memo]


    connectionsMade = []
    for memo in simplifiedMemo:
            connectionsMade.append(memo)
    print("building clusters")
    clusters = []
    remainingConnections = connectionsMade.copy()
    inCluster = []
    addToCluster = []

    for connection in connectionsMade:
        print(len(clusters))
        if connection in remainingConnections:
            newCluster= checkForConenctions([connection],remainingConnections)
            clusters.append(newCluster)
            for item in newCluster:
                remainingConnections.remove(item)
                lastCluster = item
    clusterSizes = []
    clusterNum = 0
    clusterBoxes = []
    for cluster in clusters:
        clusterBoxes.append([])
        for item in cluster:
            if item[0] not in clusterBoxes[clusterNum]: clusterBoxes[clusterNum].append(item[0])
            if item[1] not in clusterBoxes[clusterNum]: clusterBoxes[clusterNum].append(item[1])

        clusterNum += 1

    sortedClusters, = sorted(clusterBoxes, key=len, reverse=True)
    #print(sortedClusters)


    print(f"--->{len(clusters)}")
    print(lastCluster)
    print(boxes[lastCluster[0]] ,"            ", boxes[lastCluster[1]])
    print(boxes[lastCluster[0]][x] * boxes[lastCluster[1]][x])

def solvePartTwoAttemptTwo(boxes):
    id, x,y,z = ('id','x','y','z')#for me to make index the dictionary easier/cleaner
    
    
    print("Building Memo")
    boxDistanceMemo = {}
    for aBox in boxes:
        for bBox in boxes: 
            if aBox[id] != bBox[id]:
                boxDistanceMemo[aBox[id],bBox[id]] = findDistance(aBox,bBox)
    
    print("sorting")
    sortedMemo = {k: v for k, v in sorted(boxDistanceMemo.items(), key= lambda v: v[1])}

    print("simplifying")
    connectionsMade = []
    for memo in sortedMemo:
        if memo[0] < memo[1]: # duplicate check
            connectionsMade.append(memo)

    
    print("building clusters")
    
    
    clusters = []
    for box in boxes:
        clusters.append([box['id']])

    
    for connection in connectionsMade:
        idA = connection[0]
        idB = connection[1]

        #Identify cluster of each id in connection
        clusterA_idx = -1
        clusterB_idx = -1

        for i in range(len(clusters)):
            if idA in clusters[i]:
                clusterA_idx = i
            if idB in clusters[i]:
                clusterB_idx = i
        
        
        if clusterA_idx != clusterB_idx: #if they are not clusterd together
            clusters[clusterA_idx].extend(clusters[clusterB_idx])#merge 1 clsuter
            clusters.pop(clusterB_idx) #prune off the other

            # Stop conditional all connections made into one cluster print idA and idB's x values
            if len(clusters) == 1:
                print(f"---> {len(clusters)} Cluster remaining")
                print(f"Last Connection: {connection}")
                
                xA = boxes[idA][x]
                xB = boxes[idB][x]
                print(f"X values: {xA} * {xB}")
                print(f"Answer: {xA * xB}")
                return 
    



    




    

        
        

solvePartTwoAttemptTwo(junctionBoxes)










print("finished")
end_time = time.time()
print(f"--- {end_time - start_time:.4f} seconds ---") 



