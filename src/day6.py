"""
Implementatin of Day 6 of Advent of Code 2021.
More details of the challenge can be found here:
https://adventofcode.com/2021/day/6
"""
from typing import Final

MAX_LANTERNFISH_TIMER: Final = 8
LANTERNFISH_TIMER_RESET: Final = 6
LANTERNFISH_TIMER_EXPIRED: Final = 0
TIMER_FILE = "/workspaces/advent2021/src/inputs/day6.txt"

def getLanternfishTimers(file):
    """
    Given a string with comma separated list of integers representing timer values, returns a list of integers
    where each integer corresponds to the timer value of a lanternfish.
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

def getFishCountList(timers):
    """
    Input: A list of integers representing the timer values of each lanternfish. 
    
    Output: An array of integers, where the index of the array is the timer value, and the value
            at the index is the number of fish that are at that timer value.
    """
    fishCount = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    for timer in timers:
        fishCount[timer] += 1
    
    return fishCount

def simulateDay(fishCount):
    """
    The following things happen on each day:
    - All fish have their timer value decremented by 1.
    - The fish that have a timer value of 0, reset its timer value to 6. 
    - In addition, they each create a new lanternfish and set its timer to 8.
    - The new lanternfish start their timer countdown from the next day.
    """
    updatedFishCount = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    numTimerExpiredFish = fishCount[LANTERNFISH_TIMER_EXPIRED]

    for i in range(MAX_LANTERNFISH_TIMER):
        updatedFishCount[i] = fishCount[i + 1]
    
    if numTimerExpiredFish > 0:
        updatedFishCount[LANTERNFISH_TIMER_RESET] += numTimerExpiredFish
        updatedFishCount[MAX_LANTERNFISH_TIMER] += numTimerExpiredFish
    
    return updatedFishCount

def simulateDays(fishCount, days):
    for _ in range(days):
        fishCount = simulateDay(fishCount)
    
    return fishCount

def main():
    timers = getLanternfishTimers(TIMER_FILE)
    
    # PART 1: How many fish after 80 days?
    fishCount = getFishCountList(timers)
    fishCount = simulateDays(fishCount, 80)
    print("Numer of lanternfish at the end of 80 days is {}".format(sum(fishCount)))

    # PART 2: How many fish after 256 days?
    fishCount = getFishCountList(timers)
    fishCount = simulateDays(fishCount, 256)
    print("Numer of lanternfish at the end of 256 days is {}".format(sum(fishCount)))

if __name__ == "__main__":
    main()