DEPTHS_FILE = "/workspaces/advent2021/src/day1_1.txt"

def getDepthsList():
    """
    Returns a list of depths
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

class day1:
    def __init__(self, depthList):
        self.depthList = depthList
    
    def getDepthList(self):
        return self.depthList
    
    def getDepthIncreaseCount(self, depthList):
        count = 0

        for i in range(len(depthList) - 1):
            if depthList[i] < depthList[i + 1]:
                count += 1
        
        return count

    def getDepthListInSlidingWindow(self):
        depthsInSlidingWindow = []

        for i in range(len(self.depthList) - 2):
            j = i + 3
            sum = 0

            # sum of depths for this sliding window
            for depth in self.depthList[i:j]:
                sum += depth
            
            depthsInSlidingWindow.append(sum)
        
        return depthsInSlidingWindow

def main():
    depthList = getDepthsList()
    #depthList = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    day = day1(depthList)
    depthIncreaseCount = day.getDepthIncreaseCount(depthList)
    print("Individual depth increase count is {}".format(depthIncreaseCount))
    depthsInSlidingWindow = day.getDepthListInSlidingWindow()
    slidingWindowDepthIncreaseCount = day.getDepthIncreaseCount(depthsInSlidingWindow)
    print("Depth Increase count in the sliding window is {}".format(slidingWindowDepthIncreaseCount))
    
if __name__ == '__main__':
    main()