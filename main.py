with open("input.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line.split(' '))

blocks = array[1:11]
moves = array[11:]

import math
import pdb

x = 0
y = 0
direction = 'north'
currentDirec = ""
maxDis = 0


def setDirection(direction, currentDirec):
    if direction == 'north':
        if currentDirec == "L":
            direction = "west"
        elif currentDirec == "R":
            direction = "east"
    elif direction == 'west':
        if currentDirec == "L":
            direction = "south"
        elif currentDirec == "R":
            direction = "north"
    elif direction == 'south':
        if currentDirec == "L":
            direction = "east"
        elif currentDirec == "R":
            direction = "west"
    elif direction == 'east':
        if currentDirec == "L":
            direction = "north"
        elif currentDirec == "R":
            direction = "south"

    return direction




def getDis(moves, direction, currentDirec, x, y, maxDis):

    for el in moves:
        if el[0][0] == "L":
            currentDirec = "L"
            direction = setDirection(direction, currentDirec)
        elif el[0][0] == "R":
            currentDirec = "R"
            direction = setDirection(direction, currentDirec)
        elif el[0] == "M":
            if direction == "north":
                y += int(el[1])
            elif direction == "south":
                y -= int(el[1])
            elif direction == "east":
                x += int(el[1])
            elif direction == "west":
                x -= int(el[1])

            if math.sqrt(x ** 2 + y ** 2) > maxDis: maxDis = math.sqrt(x ** 2 + y ** 2)

    return maxDis



print(getDis(moves, direction, currentDirec, x, y, maxDis))
