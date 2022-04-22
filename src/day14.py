"""
Implementatin of Day 14 of Advent of Code 2021.
More details of the challenge can be found here:
https://adventofcode.com/2021/day/14
"""
from re import template
from typing import Final
from collections import Counter

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

def applySteps(template, ruleDict, numSteps):
    for _ in range(numSteps):
        template = applyStep(template, ruleDict)
    
    return template

def applyStep(template, ruleDict):
    """
    Models a single step in the polymer reaction.
    
    Input: the polymer template (string) and the rule dictionary.
    
    Output: the modified polymer template (string) after the polymer reactions have been applied.
    """
    tempList = list(template)
    index = 1

    for i in range(len(template) - 1):
        pair = template[i: i + 2]

        insertP = ruleDict[pair]

        tempList.insert(index, insertP)
        index += 2
    
    return "".join(tempList)

def getPartOneResult(template):
    counts = Counter(template)
    mostCommonElementCount = max(counts.values())
    leastCommonElementCount = min(counts.values())
    return mostCommonElementCount - leastCommonElementCount

def main():
    PAIR_INSERTION_RULES: Final = "/workspaces/advent2021/src/inputs/day14.txt"
    (template, rules) = getTemplateAndRules(PAIR_INSERTION_RULES)

    # PART 1
    ruleDict = getRuleDict(rules)
    template = applySteps(template, ruleDict, 10)
    result = getPartOneResult(template)
    print("Result = {}".format(result))

if __name__ == "__main__":
    main()