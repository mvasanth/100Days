"""
Implementatin of Day 14 of Advent of Code 2021.
More details of the challenge can be found here:
https://adventofcode.com/2021/day/14
"""
from typing import Final

def getTemplateAndRules(file):
    """
    Given an input file, returns the polymer template (string) and a list of lines, where each line
    is a string representing a polymer insertion rule.
    """
    try:
        inFile = open(file, 'r')
    except OSError:
        print("Could not open file")
        raise FileNotFoundError

    lines = inFile.readlines()

    # strip the trailing newline at the end of each line
    lines = [line.strip() for line in lines]

    inFile.close()

    template = lines[0]
    rules = lines[2:]
    return (template, rules)

def getRuleDict(rules):
    """
    Input: A list of strings representing polymer insertion rules. 
    
    Output: A dictionary of polymer insertion rules.
    """
    ruleDict = {}

    for rule in rules:
        pair = rule.split("->")

        ruleDict[pair[0].rstrip()] = pair[1].lstrip()
    
    return ruleDict

def getTemplateDict(template):
    templateDict = {}

    for i in range(len(template) - 1):
        pair = template[i: i + 2]

        if pair not in templateDict:
            templateDict[pair] = 1
        else:
            templateDict[pair] += 1
    
    return templateDict

def applySteps(template, ruleDict, numSteps):
    templateDict = getTemplateDict(template)

    for _ in range(numSteps):
        templateDict = applyStep(templateDict, ruleDict)
    
    return templateDict

def updatePair(pair, templateDict, count):
    if pair not in templateDict:
        templateDict[pair] = count
    else:
        templateDict[pair] += count
    
def applyStep(templateDict, ruleDict):
    """
    Models a single step in the polymer reaction.
    
    Input: the polymer template (string) and the rule dictionary.
    
    Output: the modified polymer template (string) after the polymer reactions have been applied.
    """
    templateDictCopy = templateDict.copy()

    for pair in templateDict:
        count = templateDict[pair]

        # get the character that is inserted and the new pairs
        insertP = ruleDict[pair]
        leftPair = pair[0] + insertP
        rightPair = insertP + pair[1]

        # the old pair is broken, update it's count
        templateDictCopy[pair] -= count

        # new pairs are added to the dictionary
        updatePair(leftPair, templateDictCopy, count)
        updatePair(rightPair, templateDictCopy, count)

    return templateDictCopy

def getLetterDict(templateDict):
    letterDict = {}

    nonEmptyPairs = [pair for pair in templateDict.keys()
                        if templateDict[pair] > 0]

    for pair in nonEmptyPairs:
        updateLetterDict(pair[0], letterDict, templateDict[pair])
        updateLetterDict(pair[1], letterDict, templateDict[pair])
    
    for letter in letterDict:
        if letterDict[letter] % 2 == 0:
            letterDict[letter] //= 2
        else:
            letterDict[letter] = (letterDict[letter] // 2 + 1)

    return letterDict

def updateLetterDict(letter, letterDict, count):
    if letter not in letterDict:
        letterDict[letter] = count
    else:
        letterDict[letter] += count

def getFinalResult(letterDict):
    mostCommonElementCount = max(letterDict.values())
    leastCommonElementCount = min(letterDict.values())
    return mostCommonElementCount - leastCommonElementCount

def main():
    PAIR_INSERTION_RULES: Final = "/workspaces/advent2021/src/inputs/day14.txt"
    (template, rules) = getTemplateAndRules(PAIR_INSERTION_RULES)
    ruleDict = getRuleDict(rules)

    # PART 1
    templateDict = applySteps(template, ruleDict, 10)
    letterDict = getLetterDict(templateDict)
    result = getFinalResult(letterDict)
    print("Result after 10 steps = {}".format(result))

    # PART 2
    templateDict = applySteps(template, ruleDict, 40)
    letterDict = getLetterDict(templateDict)
    result = getFinalResult(letterDict)
    print("Result after 40 steps = {}".format(result))

if __name__ == "__main__":
    main()