import unittest
import sys
sys.path.insert(1, '/workspaces/advent2021/src')
from day2 import UnknownCommandTypeError, day2, getCommandList
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

class testGetCommandList(unittest.TestCase):

    def testGetCommandListValidFile(self):
        commands = getCommandList("/workspaces/advent2021/tests/day2test.txt")
        self.assertIsNotNone(commands)
        self.assertEqual(3, len(commands))
        self.assertEqual(CommandType.forward, commands[0].type)
        self.assertEqual(5, commands[0].value)
        self.assertEqual(CommandType.down, commands[1].type)
        self.assertEqual(7, commands[1].value)
        self.assertEqual(CommandType.up, commands[2].type)
        self.assertEqual(3, commands[2].value)
    
    def testGetCommandListInvalidFile(self):
        try:
            commands = getCommandList("/workspaces/advent2021/tests/day2tests.txt")
        except OSError:
            self.assertRaises(FileNotFoundError)
    
    def testGetCommandListInvalidCommand(self):
        try:
            commands = getCommandList("/workspaces/advent2021/tests/day2test_invalid.txt")
        except UnknownCommandTypeError:
            self.assertRaises(UnknownCommandTypeError)
            
class testDay2(unittest.TestCase):

    def testDay2Creation(self):
        day = day2(0, 0, 0)
        self.assertIsNotNone(day)
    
    def testDay2GetPosition(self):
        day = day2(3, 0, 0)
        self.assertEqual(3, day.getPosition())

    def testDay2GetDepth(self):
        day = day2(0, 7, 0)
        self.assertEqual(7, day.getDepth())

    def testDay2GetAim(self):
        day = day2(0, 0, 9)
        self.assertEqual(9, day.getAim())
        
    def testDay2ModifyPosition(self):
        day = day2(3, 0, 0)
        day.modifyPosition(5)
        self.assertEqual(8, day.getPosition())

    def testDay2ModifyAimDown(self):
        day = day2(0, 0, 7)
        day.modifyAim(CommandType.down, 4)
        self.assertEqual(11, day.getAim())

    def testDay2ModifyAimUp(self):
        day = day2(0, 0, 7)
        day.modifyAim(CommandType.up, 4)
        self.assertEqual(3, day.getAim())
    
    def testDay2ModifyDepth(self):
        day = day2(0, 5, 7)
        day.modifyDepth(3)
        self.assertEqual(26, day.getDepth())

    def testDay2FinalResult(self):
        command1 = Command(CommandType.forward, 5)
        command2 = Command(CommandType.down, 5)
        command3 = Command(CommandType.forward, 8)
        command4 = Command(CommandType.up, 3)
        command5 = Command(CommandType.down, 8)
        command6 = Command(CommandType.forward, 2)
        commands = []
        commands.append(command1)
        commands.append(command2)
        commands.append(command3)
        commands.append(command4)
        commands.append(command5)
        commands.append(command6)

        day = day2(0, 0, 0)
        day.executeCommands(commands)
        self.assertEqual(15, day.getPosition())
        self.assertEqual(60, day.getDepth())
        self.assertEqual(900, day.getFinalResult())

if __name__ == '__main__':
    unittest.main()