"""
Implementation of Day 1 of the Advent Calender 2021.
Details of Day 1 can be found here:
https://adventofcode.com/2021/day/1
"""

DEPTHS_FILE = "/workspaces/advent2021/src/inputs/day1.txt"
SLIDING_WINDOW_SIZE = 3

def getDepthList():
    """
    Input: A file containing the depths of the ocean floor. One depth on each line.
    
    Output: Returns a list of integer depths 
    """
    print("Loading depths from file day1_1.txt")
    inFile = open(DEPTHS_FILE, 'r')
    lines = inFile.readlines()

    # strip the trailing newline at the end of each line
    lines = [line.strip() for line in lines]

    # convert each line from string to int
    depthsList = [int(line) for line in lines]

    print("Loaded {} depths".format(len(depthsList)))
    return depthsList
    
def getDepthIncreaseCount(depthList):
    """
    Input: Takes in a list of depths (int) 
    
    Outout: Returns the count of the number of times there is an increase
            in depth in the given list
    """
    count = 0

    for i in range(len(depthList) - 1):
        if depthList[i] < depthList[i + 1]:
            count += 1
    
    return count

def getAggregateDepthList(depthList):
    """
    Input: Takes in a list of depths (int)
    
    Output: Returns a list of depths where each depth is the sum of depths in a sliding window
            of the original list of depths. 
    """
    aggregateDepths = []

    for i in range(len(depthList) - (SLIDING_WINDOW_SIZE - 1)):
        j = i + SLIDING_WINDOW_SIZE
        sum = 0

        # sum of depths for this sliding window
        for depth in depthList[i:j]:
            sum += depth
        
        aggregateDepths.append(sum)
    
    return aggregateDepths

def main():
    # setup
    depthList = getDepthList()

    # part 1
    depthIncreaseCount = getDepthIncreaseCount(depthList)
    print("Individual depth increase count is {}".format(depthIncreaseCount))

    # part 2
    depthsInSlidingWindow = getAggregateDepthList(depthList)
    slidingWindowDepthIncreaseCount = getDepthIncreaseCount(depthsInSlidingWindow)
    print("Depth Increase count in the sliding window is {}".format(slidingWindowDepthIncreaseCount))
    
if __name__ == '__main__':
    main()