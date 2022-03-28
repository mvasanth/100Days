"""
Implementatin of Day 6 of Advent of Code 2021.
More details of the challenge can be found here:
https://adventofcode.com/2021/day/6
"""
from re import T
from typing import Final

NEW_LANTERNFISH_TIMER: Final = 8
LANTERNFISH_TIMER_RESET: Final = 6
LANTERNFISH_TIMER_EXPIRY: Final = 0
TIMER_FILE = "/workspaces/advent2021/src/day6.txt"

def getLanternfishTimers(file):
    """
    Given a comma separated list of integers representing timer values, returns a list of integers
    where each integer corresponds to the timer value of a lantern fish.
    """
    try:
        inFile = open(file, 'r')
    except OSError:
        print("Could not open file")
        raise FileNotFoundError

    timers = inFile.readline()

    inFile.close()

    timers = timers.split(",")

    timers = [int(timer) for timer in timers]

    return timers

class Lanternfish:
    def __init__(self, timer):
        self.timer = timer
        self.isNewTimer = False
    
    def getTimer(self):
        return self.timer
    
    def getIsNewTimer(self):
        return self.isNewTimer
    
    def resetTimer(self, newTimer):
        self.timer = newTimer
    
    def setIsNewTimer(self, timerState):
        self.isNewTimer = timerState
    
    def decrementTimer(self):
        self.timer -= 1

class LanternfishGrowth:
    """
    Models the growth of lanternfish over a certain number of days.
    Inputs are a list of lanternfish objects and an integer representing the number of days.
    """
    def __init__(self, lanternfish, days):
        self.lanternfishes = lanternfish
        self.days = days
    
    def handleTimerExpiry(self):
        pass

    def simulateLanternfishGrowth(self):
        """
        Given a list of lanternfish and the number of days, returns the growth (the number of fish) 
        of the fish at the end of the stipulated time period.
        """
        count = 0

        while (count != self.days):
            # List of indices to reset at the end of the day
            endOfDay = []

            for i, lanternfish in enumerate(self.lanternfishes):
                if lanternfish.getTimer() == LANTERNFISH_TIMER_EXPIRY:
                    # Reset the timer for this lanternfish
                    lanternfish.resetTimer(LANTERNFISH_TIMER_RESET)

                    # Start the timer for a new lanternfish
                    babyLanternfish = Lanternfish(NEW_LANTERNFISH_TIMER)
                    babyLanternfish.setIsNewTimer(True)
                    self.lanternfishes.append(babyLanternfish)

                elif lanternfish.getTimer() == NEW_LANTERNFISH_TIMER:
                    # Fish was just added to the list, timer starts running from the next day
                    if lanternfish.getIsNewTimer() == True:
                        endOfDay.append(i)
                    else:
                        lanternfish.decrementTimer()
                        
                else:
                    lanternfish.decrementTimer()

            # the day has passed, update timer state for all the new fish
            for lanternfish in self.lanternfishes:
                if lanternfish.getTimer() == NEW_LANTERNFISH_TIMER:
                    lanternfish.setIsNewTimer(False)

            count += 1

        return len(self.lanternfishes)

def getLanternfishes(timers):
    lanternfishes = []

    for timer in timers:
        lanternfish = Lanternfish(timer)
        lanternfishes.append(lanternfish)
    
    return lanternfishes

def main():
    timers = getLanternfishTimers(TIMER_FILE)
    lanternfishes = getLanternfishes(timers)
    growth = LanternfishGrowth(lanternfishes, 256)
    count = growth.simulateLanternfishGrowth()
    print("Numer of lanternfish at the end of 80 days is {}".format(count))

if __name__ == "__main__":
    main()