import unittest
import sys
sys.path.insert(1, '/workspaces/advent2021/src')
from day2 import day2, getCommandList
from day2 import Command
from day2 import CommandType

class testCommand(unittest.TestCase):

    def testCommandCreation(self):
        command = Command(CommandType.down, 2)
        self.assertIsNotNone(command)
    
    def testCommandGetType(self):
        command = Command(CommandType.down, 2)
        self.assertEqual(CommandType.down, command.getType())
    
    def testCommandGetValue(self):
        command = Command(CommandType.down, 2)
        self.assertEqual(2, command.getValue())

class testGetCommandList(self):

    def testGetCommandListFromFile():
        commands = getCommandList()
    
class testDay2(unittest.TestCase):

    def testExecuteCommands(self):
        commandF = Command(CommandType.forward, 5)
        commandD = Command(CommandType.down, 9)
        commandU = Command(CommandType.up, 6)
        commands = []
        commands.append(commandF)
        commands.append(commandD)
        commands.append(commandU)

        day = day2(0, 0)
        day.executeCommands(commands)
        self.assertEqual(5, day.getPosition())
        self.assertEqual(3, day.getDepth())

if __name__ == '__main__':
    unittest.main()