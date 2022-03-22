"""
Implementatin of Day 2 of Advent of Code 2021.
More details of the challenge can be found here:
https://adventofcode.com/2021/day/2
"""
from enum import Enum
from fileinput import close
import sys
COMMANDS_FILE = "/workspaces/advent2021/src/day2.txt"

class CommandType(Enum):
    forward = 1 # increases the horizontal position
    down = 2 # increases the depth
    up = 3 # decreases the depth

class Command:
    """
    Creates a command object with a particular type (forward, down or up),
    and the value the position or depth will be changed by.
    """
    def __init__(self, type, value):
        self.type = type
        self.value = value
    
    def getType(self):
        return self.type
    
    def getValue(self):
        return self.value

class UnknownCommandTypeError(Exception):
    """
    Raised when an unidentified command type is received.
    Valid command types are forward, down and up.
    """
    pass

def getCommandList(file):
    """
    Helper function that takes in a file that has a list of commands and converts them into a
    list of command objects that will then be used by the day2 class. 
    
    Input: File containing the list of commands.
    
    Output: Command list.
    """
    try:
        inFile = open(file, 'r')
    except OSError:
        print("Could not open file")
        raise FileNotFoundError

    lines = inFile.readlines()

    # strip the trailing newline at the end of each line
    lines = [line.strip() for line in lines]

    # separate the command type and the value
    lines = [line.split(" ") for line in lines]
    
    commands = []

    try:
        for line in lines:
            if line[0] == "forward":
                type = CommandType.forward
            elif line[0] == "down":
                type = CommandType.down
            elif line[0] == "up":
                type = CommandType.up
            else:
                raise UnknownCommandTypeError
            
            command = Command(type, int(line[1]))
            commands.append(command)
    except UnknownCommandTypeError:
        print("Received an unknown command type")
        raise UnknownCommandTypeError
    finally:
        inFile.close()    
    
    return commands

class day2:
    """
    Models the behaviour for Day 2 of the Advent Calender 2021.
    Maintains three parameters position, depth and aim that are used to steer the submarine,
    and exposes all the API's needed to modify them.
    """
    def __init__(self, position, depth, aim):
        self.position = position
        self.depth = depth
        self.aim = aim
    
    def getPosition(self):
        return self.position
    
    def getDepth(self):
        return self.depth
    
    def getAim(self):
        return self.aim
    
    def modifyPosition(self, position):
        self.position += position
    
    def modifyDepth(self, value):
        self.depth += (self.aim * value)
    
    def modifyAim(self, commandType, aim):
        if commandType == CommandType.down:
            self.aim += aim
        else:
            self.aim -= aim
    
    def getFinalResult(self):
        return (self.position * self.depth)
    
    def executeCommands(self, commandList):
        for command in commandList:
            if command.type == CommandType.forward:
                self.modifyPosition(command.value)
                self.modifyDepth(command.value)
            else:
                self.modifyAim(command.type, command.value)

def main():
    commands = getCommandList(COMMANDS_FILE)
    day = day2(0, 0, 0)
    day.executeCommands(commands)
    result = day.getFinalResult()
    print("Final Result is {}".format(result))

if __name__ == '__main__':
    main()