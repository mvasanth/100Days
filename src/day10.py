"""
Implementatin of Day 9 of Advent of Code 2021.
More details of the challenge can be found here:
https://adventofcode.com/2021/day/10
"""

from typing import Final

SYNTAX: Final = "/workspaces/advent2021/src/inputs/day10.txt"

def getRawSyntax(file):
    """
    Given a file where each line represents syntax chunks in a submarine navigation subsystem,
    returns a list of strings where each line is a separate string.
    """
    try:
        inFile = open(file, 'r')
    except OSError:
        print("Could not open file")
        raise FileNotFoundError

    rawSyntax = inFile.readlines()

    # strip the trailing newline at the end of each line
    rawSyntax = [line.strip() for line in rawSyntax]

    inFile.close()

    return rawSyntax

def getIllegalCharDictAndMatchStrings(rawSyntax):
    """
    Processes each line of the syntax file and returns a tuple. 

    The first element of the tuple is a dictionary, where the keys are the characters that caused
    the line to be corrupted, and the values are the occurrences of these characters in the syntax lines.

    The second element of the tuple is a list of strings. Where each string is a sequence of characters
    that need to be appended to all the valid but incomplete strings in the given raw syntax.
    """
    illegalCharDict = {}
    matchStrings = []

    for syntaxLine in rawSyntax:
        char = processLine(syntaxLine)

        if len(char) == 1:
            # we have found an illegal character
            if char not in illegalCharDict:
                illegalCharDict[char] = 1
            else:
                illegalCharDict[char] += 1
        else:
            matchStrings.append(char)
    
    # reverse the string, as we need to close the last open brace first
    matchStrings = [string[::-1] for string in matchStrings]
    return (illegalCharDict, matchStrings)

class UnidentifiedCharException(Exception):
    """
    Raised when the syntax line contains a charater that is not one of the following:
    (, [, {, <, >, }, ], ).
    """
    pass

def processLine(syntaxLine):

    closingChars = { ')' : '(',
                        ']' : '[',
                        '}' : '{',
                        '>' : '<' }
    openingChars = { '(' : ')',
                        '[' : ']',
                        '{' : '}',
                        '<' : '>' }
    matchChars = []

    try:
        '''
        - Scan the string from left to right.
        - If the char is an opening char, add it to a temporary list.
        - If it is a closing char, check the last char that was added to the list.
            - If the last char is a match for the current char,
                - the syntax is still valid, remove the last char and continue scanning
            - If the last char is not a match for the current char,
                - the string is corrupted, return the illegal character
        '''
        for char in syntaxLine:
            if char in openingChars:
                matchChars.append(char)
            else:
                if closingChars[char] == matchChars[-1]:
                    matchChars.pop()
                else:
                    return char

    except UnidentifiedCharException:
        raise UnidentifiedCharException

    return matchChars          

class SyntaxErrorHandling():
    def __init__(self, illegalCharDict):
        self.illegalCharDict = illegalCharDict
        self.charPointsTable = { ')': 3,
                                 ']': 57,
                                 '}': 1197,
                                 '>': 25137 }
    
    def getTotalSyntaxErrorScore(self):
        totalSyntaxErrors = 0

        for char in self.illegalCharDict:
            totalSyntaxErrors +=  self.illegalCharDict[char] * self.charPointsTable[char]
        
        return totalSyntaxErrors

def getCompletionStrings(matchStrings):
    completionStrs = []

    for matchString in matchStrings:
        completionStr = getCompletionString(matchString)
        completionStrs.append(completionStr)

    return completionStrs

def getCompletionString(matchChars):
    """
    Given a string containing opening characters (, [, { or <, returns a string of equal length
    containing the matches for each of these characters in the same order.
    
    For example, if the input string is [<{{(, the output string returned will be ]>}}).
    """
    completionStr = ""

    for char in matchChars:

        if char == '(':
            completionStr += ')'
        elif char == '[':
            completionStr += ']'
        elif char == '{':
            completionStr += '}'
        elif char == '<':
            completionStr += '>'
        
    return completionStr

def getScoresList(completionStrs):
    """
    Given a list of strings, returns a list of integers where each integer corresponds to the
    score of the individual string.
    """
    scores = []

    for str in completionStrs:
        score = getCompletionStrScore(str)
        scores.append(score)
    
    return scores

def getCompletionStrScore(completionStr):
    """
    Given a string, return the score of that string based on the score dictionary defined below.
    """
    score = 0
    scoreDict = { ')': 1,
                  ']': 2,
                  '}': 3,
                  '>': 4}

    for char in completionStr:
        score = (score * 5) + scoreDict[char]
    
    return score

def getMiddleScore(scores):
    """
    Given a list of scores, sorts the list and returns the middle score.
    """
    scores.sort()

    middle = len(scores) // 2

    return scores[middle]

def main():
    rawSyntax = getRawSyntax(SYNTAX)
    (illegalCharDict, matchStrings) = getIllegalCharDictAndMatchStrings(rawSyntax)

    # Part 1
    syntaxErrorHandling = SyntaxErrorHandling(illegalCharDict)
    totalErrors = syntaxErrorHandling.getTotalSyntaxErrorScore()
    print("Total Syntax Errors are {}".format(totalErrors))

    # Part 2
    completionStrs = getCompletionStrings(matchStrings)
    scores = getScoresList(completionStrs)
    middleScore = getMiddleScore(scores)
    print("Middle Score = {}".format(middleScore))

if __name__ == "__main__":
    main()